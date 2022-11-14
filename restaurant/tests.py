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

class GetAllRestaurantTest(TestCase):
    """ Test module for GET all Restaurent  API """

    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = UserAccount.objects.create(
            email='test@user.me', password='12345678'
        )
        refresh = generate_access_token(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        pass

    def test_get_all_restaurant(self):
        url = reverse('get_restaurant')
        response = self.client.get((reverse('get_restaurant')), **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
class CreateNewRestaurentTest(TestCase):
    """ Test module for inserting a new Restaturent """
    @property
    def bearer_token(self):
       
        user = UserAccount.objects.create(
            email='test@user.me', password='12345678'
        )

        refresh = generate_access_token(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}
    def setUp(self):
        self.valid_payload = {
            'name': 'Dutt Guru Kripa1',
            'point': 4,        
        }
    def test_create_valid_restaurant(self):
       
        response = client.post(
            reverse('add_restaurant'),
            data=json.dumps(self.valid_payload),
            content_type='application/json', **self.bearer_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class GetRestaurantFoodItemTest(TestCase):
    """ Test module for GET all Restaurent Food Item API """

    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = UserAccount.objects.create(
            email='test@user.me', password='12345678'
        )
        refresh = generate_access_token(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        pass

    def test_get_all_restaurant(self):
      
        response = self.client.get((reverse('get_restaurant_food_item',kwargs={'restaurant_id': 1})), **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    

class AddRestaurantFoodItemTest(TestCase):
    """ Test module for GET all Restaurent Food Item API """

    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = UserAccount.objects.create(
            email='test@user.me', password='12345678'
        )
        refresh = generate_access_token(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        self.valid_payload = {
            'restaurant_id': 1,
            'name': "panner",        
        }
        

    def test_get_all_restaurant(self):
        response = client.post(
            reverse('add_restaurant_food_item'),
            data=json.dumps(self.valid_payload),
            content_type='application/json', **self.bearer_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
      
class AddRestaurantMenuTest(TestCase):
    """ Test module for GET all Restaurent Food Item API """

    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = UserAccount.objects.create(
            email='test@user.me', password='12345678'
        )
        refresh = generate_access_token(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        self.valid_payload ={
         "restaurant_id":2,
            "food_item":[1,2,4],
                    "date" :"2022-11-15"
            }
        

    def test_get_all_restaurant(self):
        response = client.post(
            reverse('add_restaurant_menu'),
            data=json.dumps(self.valid_payload),
            content_type='application/json', **self.bearer_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AddRestaurantMenuVoteTest(TestCase):
    """ Test module for GET all Restaurent Food Item API """

    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = UserAccount.objects.create(
            email='test@user.me', password='12345678'
        )
        refresh = generate_access_token(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        self.valid_payload ={
            "restaurent_menu_id":[31],
        "user_id":2,
            "date" :"2022-11-14"
            }
        

    def test_get_all_restaurant(self):
        response = client.post(
            reverse('add_restaurant_menu_vote'),
            data=json.dumps(self.valid_payload),
            content_type='application/json', **self.bearer_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class AddRestaurantMenuVoteV2Test(TestCase):
    """ Test module for GET all Restaurent Food Item API """

    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = UserAccount.objects.create(
            email='test@user.me', password='12345678'
        )
        refresh = generate_access_token(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        self.valid_payload ={
            "restaurent_menu_id":[38,39,40,41],
        "user_id":1,
            "date" :"2022-11-16"
            }
        

    def test_get_all_restaurant(self):
        response = client.post(
            reverse('add_restaurant_menu_vote_v2'),
            data=json.dumps(self.valid_payload),
            content_type='application/json', **self.bearer_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        

class GetCurrentResultTest(TestCase):
    """ Test module for GET all Restaurent  API """

    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = UserAccount.objects.create(
            email='test@user.me', password='12345678'
        )
        refresh = generate_access_token(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh}'}

    def setUp(self):
        pass

    def test_get_all_restaurant(self):
        # url = reverse('get_restaurant')
        url = '{url}?{filter}={value}'.format(
        url=reverse('get_result'),
        filter='date', value='2022-11-14')
        response = self.client.get(url, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    


        