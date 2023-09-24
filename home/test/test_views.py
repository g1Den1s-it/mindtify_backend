from django.test import TestCase
from django.shortcuts import reverse
from rest_framework.test import APIClient
from rest_framework import status

from home.models import Test
from user.models import User


class TestTakeTestView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='Den1s',
            email='test@test.com',
            password='Q1w2e3r4t5y6_'
        )

        self.test_model = Test.objects.create(
            title='My test',
            description='test my model test',
            owner=self.user
        )

    def test_get_test(self):
        url = reverse('take-test', kwargs={'slug': self.test_model.slug})
        res = self.client.get(url)

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data['title'], 'My test')

    def test_get_invalid_test(self):
        url = reverse('take-test', kwargs={'slug': 'test'})

        res = self.client.get(url)

        self.assertEquals(res.status_code, status.HTTP_404_NOT_FOUND)
