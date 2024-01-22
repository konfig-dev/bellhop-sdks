# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from bellhop.paths.store_order_order_id.delete import DeleteOrderRaw
from bellhop.paths.store_inventory.get import GetInventoryRaw
from bellhop.paths.store_order_order_id.get import GetOrderByIdRaw
from bellhop.paths.store_order.post import PlaceOrderRaw


class StoreApiRaw(
    DeleteOrderRaw,
    GetInventoryRaw,
    GetOrderByIdRaw,
    PlaceOrderRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
