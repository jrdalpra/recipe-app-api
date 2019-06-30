from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.root = get_user_model().objects.create_superuser(
            email='root@mycompany.com',
            password='anything321123'
        )
        self.client.force_login(self.root)
        self.regular = get_user_model().objects.create_user (
            email='regular@pythonnewbies.com',
            password='Pass123',
            name='Any Name'
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.regular.name)
        self.assertContains(res, self.regular.email)
