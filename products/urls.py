from django.urls import path

from products.views import (
    ProductListView, 
    ProductDetailSlugView, 
    )

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
]

app_name = 'products'
