from django.db import models
from django.conf import settings

from product.models import Product
from address.models import Address


class Order(models.Model):
    # order_id = models.CharField(max_length=120, blank=True)
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )
    quantity = models.CharField(max_length=500)
    shipping_total = models.DecimalField(
        default=0.00,
        max_digits=100,
        decimal_places=2
    )
    total = models.DecimalField(
        default=0.00,
        max_digits=100,
        decimal_places=2
    )
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp', '-updated']

    