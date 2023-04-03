"""
Tests for Modules
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


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
        """test new user with empty email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'password')
