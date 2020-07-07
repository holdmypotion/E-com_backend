from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from address.models import Address


CREATE_ADDRESS_URL = reverse('address:create')

def create_user(**params):
    """Helper function to create user"""
    get_user_model().objects.create_user(**params)

def sample_address(user, **params):
    """
        Creates a sample address for testing
    """
    defaults = {
        'address1': '409',
        'address2': 'whatever',
        'state': 'Whateeverstate',
        'country': 'Whatevercountry',
    }
    defaults.update(params)

    return Address.objects.create(user=user, **defaults)


class PublicAddressApiTest(TestCase):
    """Test the publically available Address API"""

    def setup(self):
        self.client = APIClient()
    
    def test_required_auth_for_creating(self):
        res = self.client.post(CREATE_ADDRESS_URL, )