from django.urls import path

from carts.views import (
    cart, cart_update
    )

urlpatterns = [
    path('', cart, name='home'),
    path('update/', cart_update, name='update'),
]

app_name = 'cart'