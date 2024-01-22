# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import bellhop
from bellhop.paths.user_create_with_array import post
from bellhop import configuration, schemas, api_client

from .. import ApiTestMixin


class TestUserCreateWithArray(ApiTestMixin, unittest.TestCase):
    """
    UserCreateWithArray unit test stubs
        Creates list of users with given input array
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 0
    response_body = ''




if __name__ == '__main__':
    unittest.main()
