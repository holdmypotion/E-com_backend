from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.api.views import OrderViewSet


router = DefaultRouter()
router.register('orders', OrderViewSet)

app_name = 'order'

urlpatterns = [
    path('', include(router.urls))
]