from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for order object"""

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'product',
            'quantity',
            'shipping_total',
            'total',
        )
        read_only_fields = ('id',)