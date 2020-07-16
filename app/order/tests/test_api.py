from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from order.models import Order
from order.api.serializers import OrderSerializer
from product.models import Product, Section


ORDER_URL = reverse('order:order-list')

def sample_section(**params):
    """Section Section"""
    defaults = {'title': 'SampleSection'}
    defaults.update(params)

    return Section.objects.create(**defaults)


def sample_product(**params):
    """Sample Product"""
    section = sample_section()
    itr = itr + 1
    defaults = {
        'title': 'SampleProduct',
        'slug': 'sampleproduct',
    }
    defaults.update(params)  # For overriding the defaults with the params
    
    return Product.objects.create(section=section, **defaults)


def sample_order(user, **params):
    product = sample_product()
    defaults = {
        'quantity': '50 whatever',
    }
    defaults.update(**params)

    return Order.objects.create(user=user, product=product, **defaults)


class PublicOrderApiTest(TestCase):
    """Test the publicly available Order API"""

    def setUp(self):
        self.client = APIClient()

    def test_required_auth(self):
        """Test the authorization is required"""
        res = self.client.get(ORDER_URL)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class PrivateOrderApiTest(TestCase):
    """Test the private order api for an authenticated user"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_orders_limited_to_user(self):
        """Test retrieving order for the currently authenticated user"""
        user2 = get_user_model().objects.create_user(
            'otheruser@gmail.com',
            'testuser'
        )
        sample_order(user=self.user)
        sample_order(user=self.user)
        sample_order(user=user2)

        res = self.client.get(ORDER_URL)

        orders = Order.objects.filter(user=self.user)
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data, serializer.data)