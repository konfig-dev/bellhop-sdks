# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from bellhop.paths.user.post import Create
from bellhop.paths.user_create_with_array.post import CreateWithArray
from bellhop.paths.user_create_with_list.post import CreateWithList
from bellhop.paths.user_username.delete import Delete
from bellhop.paths.user_username.get import GetByName
from bellhop.paths.user_login.get import Login
from bellhop.paths.user_logout.get import Logout
from bellhop.paths.user_username.put import Update
from bellhop.apis.tags.user_api_raw import UserApiRaw


class UserApi(
    Create,
    CreateWithArray,
    CreateWithList,
    Delete,
    GetByName,
    Login,
    Logout,
    Update,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UserApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UserApiRaw(api_client)