import json
import unittest
from rest_framework import status
from django.test import Client
from django.urls import reverse
from django.conf import settings
from decimal import Decimal

from rest_framework.test import APITestCase
# initialize the APIClient app
# client = Client()

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

class APIViewTest(APITestCase):
    """ Test module for GET all products API """
    test_data = None

    @classmethod
    def setUpClass(cls):
        if not cls.test_data:
            raise unittest.SkipTest("For some reason")
        super().setUpClass()
        "Child classes must override this method and define cls.test_data, model, serializer, list_view and detail_view"
        

    def setUp(self):
        self.test_data.initializeData()

    def test_get_model_first_page(self):
        # get API response
        response = self.client.get(reverse(self.list_view))
        # get data from db
        page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
        objects = self.model.objects.all()[:page_size]
        serializer = self.serializer(objects, many=True)
        print('REPONSE CONTENT')
        print(response.content)
        serializer_data = json.dumps(serializer.data, cls=JSONEncoder)
        response_data = json.loads(response.content)['results']
        
        print('-'*20)
        print(response_data)
        print(serializer_data)
        print('-'*20)
        print(response_data == serializer_data)
        self.assertEqual(response_data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_object(self):
        # get data from db
        object = self.model.objects.first()
        id = object.id

        # get API response
        response = self.client.get(reverse(self.detail_view,kwargs={'pk': id}))
        
        serializer = self.serializer(object)
        serializer_data = json.dumps(serializer.data, cls=JSONEncoder)
        self.assertEqual(json.loads(response.content), serializer_data )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_object(self):
        # get API response
        id = 30000
        response = self.client.get(reverse(self.detail_view,kwargs={'pk': id}))
        # get data from db
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
