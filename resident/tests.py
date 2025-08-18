from django.test import TestCase, Client

from resident.models import User
from django.urls import reverse

# Create your tests here.


class HouseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@email.com',
            password='password',
            username='JD',
        )

        self.client = Client()

    def test_that_anonymous_user_cannot_add_house_returns_403(self):
        self.client.login(username='JD', password='password')
        url = reverse('add_house')
        data = {
            'house_number': 2,
            'address': 'abule egba',
            'user': self.user.id
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 403)

