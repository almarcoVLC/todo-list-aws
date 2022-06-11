# coding=UTF-8

import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json

import pytest

BASE_URL = os.environ.get("BASE_URL")
#BASE_URL = "https://m0qwfec693.execute-api.us-east-1.amazonaws.com/Prod"
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_translate(self):
        print('---------------------------------------')
        print('Starting - integration test Translate TODO')
        
        #Add TODO
        url = BASE_URL+"/todos"
        data = {
         "text": "hola"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        
        print('Response Add todo: ' + json_response['body'])
        
        jsonbody= json.loads(json_response['body'])
        ID_TODO = jsonbody['id']
        
        print ('ID todo para traducir: ' + ID_TODO)
        
        self.assertEqual(
            response.status_code, 200
        )
        self.assertEqual(
            jsonbody['text'], "hola"
        )
        
        #Translate TODO request
        response = requests.get(url + '/' + ID_TODO + '/en')
        json_response = response.json()
        
        print ('Response Translate Todo: ' + str(json_response))
        self.assertEqual(
            response.status_code, 200
        )
        
        #jsonbody= json.loads(json_response['body'])
        self.assertEqual(
            json_response['text'], "hello"
        )
        
        print('End - integration test Translate TODO')
    