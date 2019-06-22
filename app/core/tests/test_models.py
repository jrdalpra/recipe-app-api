from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test if we are to create a valid user"""
        email = 'jrdalpra@pythonnewbies.com'
        password = 'Test321123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_is_normalized(self):
        """Test if we save e-mail address normalized"""
        email = 'jrdalpra@PythonNewbies.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='anything321123'
        )
        self.assertEqual(user.email, email.lower())

    def test_when_creating_an_user_with_invalid_email_then_must_fail(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='anything321123'
            )

    def test_when_creating_a_new_user_user_result_must_be_valid(self):
        root = get_user_model().objects.create_super_user(
            'root@mycompany.com',
            'anything321123'
        )
        self.assertTrue(root.is_superuser)
        self.assertTrue(root.is_staff)
