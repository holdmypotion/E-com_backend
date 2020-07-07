from rest_framework import serializers

from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    """Serializer for Address object"""

    class Meta:
        model = Address
        fields = (
            'id', 'address1',
            'address2', 'zip_code',
            'city', 'state', 'country',
        )
        read_only_fields = ('id',)
