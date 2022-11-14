from django.test import TestCase

# Create your tests here.

import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from core.utils import *
from .models import *
from .serializers import *
from core.models import *
client = Client()
from rest_framework.test import APIClient

class UserLoginTest(TestCase):
    """ Test module for GET all Restaurent  API """

    # @property
    # def bearer_token(self):
    #     # assuming there is a user in User model
    #     user = UserAccount.objects.create(
    #         email='test@user.me', password='12345678'
    #     )
    #     refresh = generate_access_token(user)
    #     return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        self.valid_payload = {

    "email":"manjughorse2@gmail.com",
    "password" :"abc1234"

        }
    def test_create_valid_employee(self):
       
        response = client.post(
            reverse('sign-in'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserSignUpTest(TestCase):
    """ Test module for GET all Restaurent  API """

    # @property
    # def bearer_token(self):
    #     # assuming there is a user in User model
    #     user = UserAccount.objects.create(
    #         email='test@user.me', password='12345678'
    #     )
    #     refresh = generate_access_token(user)
    #     return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        self.valid_payload = {

    "email":"manjughorse2@gmail.com",
    "password" :"abc1234",'username':"abc"

        }
    def test_create_valid_employee(self):
       
        response = client.post(
            reverse('sign-up'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)