from django.shortcuts import render, redirect
from cereal.models import ProductModel as Product
from cereal.models import ProductCategory as Categories, Order
from cereal.forms.forms import ShippingForm, PaymentForm
from user.models import Profile, Searches
from django.http import Http404
from django.contrib.auth.decorators import login_required
from random import randint
from cart.cart import Cart
import json
from django.conf import settings


cereals = Product.objects.all()
category = Categories.objects.all()


# View for landing page
def index(request):
    all_cereals = Product.objects.all()
    rand_cereals = []
    for i in range(4):
        rand_cereals.append(all_cereals[randint(0, len(all_cereals)-1)])
    return render(request, 'cereal/index.html', context={'cereals': rand_cereals})


# View for catalogue page
def catalogue(request):
    order_by = request.GET.get('order_by', '')
    filter = request.GET.get('filter', '')
    cereals = Product.get_by_category(filter) if filter else Product.objects.all()
    cereal_list = cereals.order_by(order_by) if order_by else cereals
    return render(request, 'cereal/catalogue.html', context={'cereals': cereal_list})


# View for product details page
def details(request, id):
    '''Fetches product from datamodel, if not found raise 404 error'''
    cereal = Product.objects.filter(id=id)
    if cereal.first() is None:
        raise Http404
    else:
        return render(request, 'cereal/details.html', context={'cereal': cereal.first() })


# Add to product to cart
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


# Removes a product from cart
@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)

    return redirect("cart_detail")


# Increase amount of a product in the cart
@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


# Decrease the amount of a product in the cart
@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


# Empties the cart
@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


# View for cart details
@login_required(login_url="/users/login")
def cart_detail(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    sum = cart_total(cart)
    return render(request, 'cart/cart_detail.html', context={'sum': sum})


# View for shipping information
# If user profile exists user information is loaded into the form, allows for changes to shipping information
@login_required(login_url="/users/login")
def cart_shipping(request):

    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ShippingForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('payment_information')
    else:
        form = ShippingForm(initial={
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "street_name": profile.street_name,
            "house_number": profile.house_number,
            "city": profile.city,
            "email": profile.email,
            "zipcode": profile.zipcode,
        })
    return render(request, 'cart/cart_shipping.html', context={'form': form})


# View for payment information
# If the user has saved payment information to their profile, information is loaded into the form, cvc excluded
@login_required(login_url="/users/login")
def cart_payment(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PaymentForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('order_overview')
    else:
        form = PaymentForm(initial={
            "card_holder": profile.card_holder,
            "card_number": profile.card_number,
            "card_expiration": profile.card_expiration,
        })
    return render(request, 'cart/cart_payment.html', context={'form': form})


# View for order overview
# Renders the final overview of the order before placing the order
# Shows the items being bought , the total price and the shipping address
@login_required(login_url="/users/login")
def cart_overview(request):
    profile = Profile.objects.filter(user=request.user).first()
    cart = request.session.get(settings.CART_SESSION_ID)
    sum = cart_total(cart)
    return render(request, 'cart/cart_overview.html', context={'user': profile,
                                                               'sum': sum})


# View for order confirmation
# Shows the items that were bought and the address to which the order is sent
@login_required(login_url="/users/login")
def cart_confirmation(request):
    user = Profile.objects.get(user_id=request.user)
    cart = request.session.get(settings.CART_SESSION_ID)
    if str(cart) != '{}':
        create_order(user, cart)
        cart.clear()
        order = Order.objects.filter(user_id=user).order_by('-time').first()
        json_format = json.loads(order.items)
        context = {'order': json_format,
                   'user': user,
                   'order_id': order.id }

        return render(request, 'cart/cart_confirmation.html', context=context)
    else:
        context = {'message': 'Your cart was empty on checkout!'}
        return render(request, 'cart/cart_confirmation.html', context=context)


# Search functionality for the page
# Saves searches to user profile if logged in as a user
def search_cereal(request):
    if request.user.is_authenticated:
            user = Profile.objects.get(user_id=request.user)
            Searches.objects.create(user=user, query=request.POST['searched'])

    if request.method == "POST":
        searched = request.POST['searched']
        cereals = (Product.objects.filter(name__icontains=searched) |
                   Product.objects.filter(description__icontains=searched))

        return render(request, 'cereal/search_cereal.html',
                      {'searched': searched,
                       'cereals': cereals})
    else:
        return render(request, 'cereal/search_cereal.html', {})


# Helper function to save an order to user profile
def create_order(user, cart):
    order = Order.objects.create(user=user, items=json.dumps(cart))
    order.save()


# Helper function which calculates the sum of cart items
def cart_total(cart):
    cart_sum = 0
    for key, value in cart.items():
        price = 0
        quantity = 0
        for inner_key, inner_value in value.items():
            if inner_key == 'price':
                price = float(inner_value)
            elif inner_key == 'quantity':
                quantity = float(inner_value)
        cart_sum += price * quantity
    return cart_sum
