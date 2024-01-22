# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class User(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    username: typing.Optional[str] = Field(None, alias='username')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    email: typing.Optional[str] = Field(None, alias='email')

    password: typing.Optional[str] = Field(None, alias='password')

    phone: typing.Optional[str] = Field(None, alias='phone')

    # User Status
    user_status: typing.Optional[int] = Field(None, alias='userStatus')
