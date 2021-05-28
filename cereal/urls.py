from django.urls import path, include
import debug_toolbar
from django.conf import settings
from . import views


urlpatterns = [
    # http://localhost:8000/cereals
    path('', views.index, name="cereal-index"),
    path('catalogue/', views.catalogue, name="catalogue"),
    path('detail/<int:id>', views.details, name="details"),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

    # Checkout
    path('cart/shipping-information/', views.cart_shipping, name='shipping_information'),
    path('cart/payment-information/', views.cart_payment, name='payment_information'),
    path('cart/order-overview/', views.cart_overview, name='order_overview'),
    path('cart/order-confirmation/', views.cart_confirmation, name='order_confirmation'),

    path('search_cereal', views.search_cereal, name='search_cereal'),
    path('__debug__', include(debug_toolbar.urls)),
]
