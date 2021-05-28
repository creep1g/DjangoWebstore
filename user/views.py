from django.shortcuts import render, redirect
from user.forms.profile_form import ProfileForm, RegistrationForm
from user.models import Profile, Searches
from cereal.models import Order
from django.contrib.auth import authenticate, login
from datetime import datetime
import json


# View for registration page
# Saves user profile information
def register(request):
    '''Registers user, first an auth user is created, next an instance of user profile
        is created to go with the user account'''
    if request.method == 'POST':
        print(request.POST['country'])
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid() :
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            print(request.POST.keys())
            profile = Profile.objects.filter(user=request.user).first()
            profile.set_street_name(request.POST['street_name'])
            profile.profile_image = form.cleaned_data['profile_image']
            profile.set_house_number(request.POST['house_number'])
            profile.set_zip(request.POST['zipcode'])
            profile.set_city(request.POST['city'])
            profile.set_country(request.POST['country'])
            profile.save()
            return redirect('cereal-index')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


# View for editing profile information
def profile(request):
    '''User edit profile view'''
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            print("Profile updated")
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'user/profile.html', {'form': form})


# View for viewing profile
def profile_view(request):
    '''User profile home page'''
    user_profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'user/profile_view.html', context={'user_profile': user_profile})


# View for users search history
def search_history_view(request):
    '''Shows authenticated users their search history'''
    search_history = Searches.objects.filter(user=Profile.objects.get(user=request.user)).order_by('-time')
    return render(request, 'user/searchhistory.html', context={'search_history': search_history})


# View for users order history
# Fetches data and processes it for use in the template
def order_history_view(request):
    '''Shows authenticated users their order history'''
    order_history = Order.objects.filter(user_id=Profile.objects.get(user=request.user)).order_by('-time')
    orders = dict()
    for order in order_history:
        cart = json.loads(order.items)
        order_total = 0
        for key, value in cart.items():
            value['item_total'] = float(value['quantity']) * float(value['price'])
            order_total += value['item_total']
        cart['order_total'] = order_total
        cart['order_time'] = order.time
        orders[str(order.id)] = cart

    return render(request, 'user/order_history.html', context={'orders': orders})


def cart_total(cart):
    '''Gets total from users shopping cart'''
    sum = 0
    for key, value in cart.items():
        price = 0
        quantity = 0
        for inner_key, inner_value in value.items():
            if inner_key == 'price':
                price = float(inner_value)
            elif inner_key == 'quantity':
                quantity = float(inner_value)
        sum += price * quantity
    return sum
