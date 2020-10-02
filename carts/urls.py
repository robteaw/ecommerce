from django.urls import path

from carts.views import (
    cart_home, 
    cart_update,
    checkout_home,
    checkout_done_view
    )

urlpatterns = [
    path('', cart_home, name='home'),
    path('checkout/success/', checkout_done_view, name='success'),
    path('checkout/', checkout_home, name='checkout'),
    path('update/', cart_update, name='update'),
]

app_name = 'cart'