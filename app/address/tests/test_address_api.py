from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from address.models import Address
from address.api.serializers import AddressSerializer


ADDRESS_URL = reverse('address:address-list')


def address_detail_url(address_id):
    """Return address detail URL"""
    return reverse('address:address-detail', args=[address_id])


def create_user(**params):
    """Helper function to create user"""
    get_user_model().objects.create_user(**params)


def sample_address(user, **params):
    """Creates a sample address for testing"""
    defaults = {
        'address1': 'HNO. 454',
        'address2': 'Main St.',
        'zip_code': '165856',
        'city': 'Chandigarh',
        'state': 'CH',
        'country': 'IN',
    }
    defaults.update(params)

    return Address.objects.create(user=user, **defaults)


class PublicAddressApiTest(TestCase):
    """Test the publically available Address API"""

    def setup(self):
        self.client = APIClient()

    def test_required_auth_for_fetching(self):
        """Test fail fetching addresses without auth"""
        res = self.client.get(ADDRESS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_required_auth_for_creating(self):
        """Test fail creating a new address without auth"""
        payload = {
            'address1': 'HNO. 454',
            'address2': 'Main St.',
            'zip_code': '165856',
            'city': 'Chandigarh',
            'state': 'CH',
            'country': 'IN',
        }
        res = self.client.post(ADDRESS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateAddressApiTest(TestCase):
    """Test the private Address Api"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'testpass555'
        )

        self.client.force_authenticate(user=self.user)

    def test_retrieve_addresses(self):
        """Test retrieving addresses for particular user"""
        sample_address(user=self.user)
        sample_address(user=self.user)

        res = self.client.get(ADDRESS_URL)

        addresses = Address.objects.filter(user=self.user)
        serializer = AddressSerializer(addresses, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_address_limited_to_user(self):
        """Test retrieveing addresses for the currently authenticated only"""
        user2 = get_user_model().objects.create_user(
            'otheruser@gmail.com',
            'otherpassword'
        )
        sample_address(user=user2)
        sample_address(user=self.user)

        res = self.client.get(ADDRESS_URL)

        addresses = Address.objects.filter(user=self.user)
        serializer = AddressSerializer(addresses, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(len(res.data), 1)

    def test_view_address_detail(self):
        """Test viewing a address detail"""
        address = sample_address(user=self.user)

        url = address_detail_url(address.id)
        res = self.client.get(url)

        serializer = AddressSerializer(address)
        self.assertEqual(res.data, serializer.data)

    def test_create_address_successful(self):
        """Test creating address by authenticated user"""
        payload = {
            'address1': 'HNO. 454',
            'address2': 'Main St.',
            'zip_code': '165856',
            'city': 'Chandigarh',
            'state': 'CH',
            'country': 'IN',
        }
        res = self.client.post(ADDRESS_URL, payload)

        address = Address.objects.get(pk=res.data['id'])
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        for key in payload.keys():
            self.assertEqual(res.data[key], getattr(address, key))

    def test_partial_update_address(self):
        """Test partially updating an address with patch"""
        address = sample_address(user=self.user)

        payload = {
            'address1': 'HNO. 5875',
            'address2': 'Backer St.',
        }
        url = address_detail_url(address.id)
        res = self.client.patch(url, payload)

        address.refresh_from_db()
        for key in payload.keys():
            self.assertEqual(res.data[key], getattr(address, key))

    def test_full_update_address(self):
        """Test Fully updating an address with put"""
        address = sample_address(user=self.user)

        payload = {
            'address1': 'HNO. 545',
            'address2': 'Back St.',
            'zip_code': '145856',
            'city': 'Panchkula',
            'state': 'HR',
            'country': 'IN',
        }
        url = address_detail_url(address.id)
        res = self.client.put(url, payload)

        address.refresh_from_db()
        for key in payload.keys():
            self.assertEqual(res.data[key], getattr(address, key))
