from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from address.api import serializers
from address.models import Address


class AddressViewSet(viewsets.ModelViewSet):
    """ViewSet for Address Model"""
    serializer_class = serializers.AddressSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()

    def get_queryset(self):
        """Returns objects for the current authenticated user only"""
        return self.request.user.addresses.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)
