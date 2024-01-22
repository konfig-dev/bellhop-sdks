# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from bellhop.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from bellhop.api_response import AsyncGeneratorResponse
from bellhop import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from bellhop import schemas  # noqa: F401

from bellhop.model.order import Order as OrderSchema

from bellhop.type.order import Order

from ...api_client import Dictionary
from bellhop.pydantic.order import Order as OrderPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = OrderSchema


request_body_order = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationXml = OrderSchema
SchemaFor200ResponseBodyApplicationJson = OrderSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Order


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Order


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXml),
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/xml',
    'application/json',
)


class BaseApi(api_client.Api):

    def _place_order_mapped_args(
        self,
        id: typing.Optional[int] = None,
        pet_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        ship_date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        complete: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if id is not None:
            _body["id"] = id
        if pet_id is not None:
            _body["petId"] = pet_id
        if quantity is not None:
            _body["quantity"] = quantity
        if ship_date is not None:
            _body["shipDate"] = ship_date
        if status is not None:
            _body["status"] = status
        if complete is not None:
            _body["complete"] = complete
        args.body = _body
        return args

    async def _aplace_order_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Place an order for a pet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_order.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _place_order_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Place an order for a pet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_order.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class PlaceOrderRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aplace_order(
        self,
        id: typing.Optional[int] = None,
        pet_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        ship_date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        complete: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._place_order_mapped_args(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
        )
        return await self._aplace_order_oapg(
            body=args.body,
            **kwargs,
        )
    
    def place_order(
        self,
        id: typing.Optional[int] = None,
        pet_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        ship_date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        complete: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._place_order_mapped_args(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
        )
        return self._place_order_oapg(
            body=args.body,
        )

class PlaceOrder(BaseApi):

    async def aplace_order(
        self,
        id: typing.Optional[int] = None,
        pet_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        ship_date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        complete: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> OrderPydantic:
        raw_response = await self.raw.aplace_order(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
            **kwargs,
        )
        if validate:
            return OrderPydantic(**raw_response.body)
        return api_client.construct_model_instance(OrderPydantic, raw_response.body)
    
    
    def place_order(
        self,
        id: typing.Optional[int] = None,
        pet_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        ship_date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        complete: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> OrderPydantic:
        raw_response = self.raw.place_order(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
        )
        if validate:
            return OrderPydantic(**raw_response.body)
        return api_client.construct_model_instance(OrderPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        id: typing.Optional[int] = None,
        pet_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        ship_date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        complete: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._place_order_mapped_args(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
        )
        return await self._aplace_order_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        id: typing.Optional[int] = None,
        pet_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        ship_date: typing.Optional[datetime] = None,
        status: typing.Optional[str] = None,
        complete: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._place_order_mapped_args(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
        )
        return self._place_order_oapg(
            body=args.body,
        )

