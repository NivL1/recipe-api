"""
Tests for Modules
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(email='test@example.com', password='password1'):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """Test creating user with an email is successful"""
        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_formatting(self):
        """Test format email at create user"""
        emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@ExaMple.com', 'Test2@example.com'],
            ['TEST3@examPLE.COM', 'TEST3@example.com'],
        ]
        for email, expected in emails:
            user = get_user_model().objects.create_user(email, 'password')
            self.assertEqual(user.email, expected)

    def test_new_user_with_empty_email_raises_error(self):
        """Test new user with empty email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'password')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'password',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test create a recipe is succesful"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'password1',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Test Recipe Name',
            time_minutes=10,
            price=Decimal('10.20'),
            description='Test Recipe Description',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a tag is successful"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)
