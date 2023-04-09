"""
Tests for the Django admin modifications
"""
from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSitesTests(TestCase):
    """Tests for Django admin"""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admintest@example.com',
            password='password1',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='usertest@example.com',
            password='password1',
            name='Test User'
        )

    def test_users_lists(self):
        """Test users are listed on page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
