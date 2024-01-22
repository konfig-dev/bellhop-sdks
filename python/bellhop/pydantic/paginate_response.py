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

from bellhop.pydantic.paginate_response_edges import PaginateResponseEdges
from bellhop.pydantic.paginate_response_page_info import PaginateResponsePageInfo

class PaginateResponse(BaseModel):
    edges: typing.Optional[PaginateResponseEdges] = Field(None, alias='edges')

    page_info: typing.Optional[PaginateResponsePageInfo] = Field(None, alias='pageInfo')
