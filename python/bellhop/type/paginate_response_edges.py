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

from bellhop.type.paginate_response_edges_node import PaginateResponseEdgesNode

class RequiredPaginateResponseEdges(TypedDict):
    pass

class OptionalPaginateResponseEdges(TypedDict, total=False):
    node: PaginateResponseEdgesNode

class PaginateResponseEdges(RequiredPaginateResponseEdges, OptionalPaginateResponseEdges):
    pass