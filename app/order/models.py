from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save

from product.models import Product
from address.models import Address
from order.utils import unique_order_id


class Order(models.Model):
    order_id = models.SlugField(
        max_length=120,
        unique=True,
        primary_key=True
    )
    # order_id = models.AutoField(primary_key=True)
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

    
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id(instance)
        
pre_save.connect(pre_save_create_order_id, sender=Order)