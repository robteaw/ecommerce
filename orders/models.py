from django.db import models

from carts.models import Cart

class Order(models.Model):
    order_id    = models.CharField(max_length=100)
    # billing_profile = ?
    # shipping_address
    # billing_address
    cart        = models.ForeignKey(Cart)
    status      = models.CharField(max_length=100, default='created')