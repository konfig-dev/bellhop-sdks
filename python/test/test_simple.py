# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from bellhop import Bellhop

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        bellhop = Bellhop(
        
            api_key = 'YOUR_API_KEY',
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(bellhop)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
