from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from order.models import Order
from order.api.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for the order app"""
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication__classess = (JWTAuthentication, )
    serializer_class = OrderSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.request.user.orders.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
