from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Testing the customizing in the admin interface"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='password55'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='testpssdfsdf',
            name='Test user full name'
        )

    def test_user_listed(self):
        """Test that users are listed on user page"""

        #  url = admin/{{ app_label }}_{{ model_name }}_changelist
        url = reverse('admin:user_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:user_user_change', args=[self.user.pk])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:user_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
