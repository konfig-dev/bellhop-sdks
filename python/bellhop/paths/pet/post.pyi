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

from bellhop.model.pet import Pet as PetSchema
from bellhop.model.category import Category as CategorySchema
from bellhop.model.tag import Tag as TagSchema
from bellhop.model.pet_photo_urls import PetPhotoUrls as PetPhotoUrlsSchema

from bellhop.type.category import Category
from bellhop.type.pet import Pet
from bellhop.type.pet_photo_urls import PetPhotoUrls
from bellhop.type.tag import Tag

from ...api_client import Dictionary
from bellhop.pydantic.pet import Pet as PetPydantic
from bellhop.pydantic.pet_photo_urls import PetPhotoUrls as PetPhotoUrlsPydantic
from bellhop.pydantic.tag import Tag as TagPydantic
from bellhop.pydantic.category import Category as CategoryPydantic

# body param
SchemaForRequestBodyApplicationJson = PetSchema
SchemaForRequestBodyApplicationXml = PetSchema


request_body_pet = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationXml = PetSchema
SchemaFor200ResponseBodyApplicationJson = PetSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Pet


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Pet


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
class ApiResponseFor405(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor405Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    response_cls_async=ApiResponseFor405Async,
)
_all_accept_content_types = (
    'application/xml',
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_mapped_args(
        self,
        name: str,
        photo_urls: PetPhotoUrls,
        tags: typing.Optional[typing.List[Tag]] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[Category] = None,
        status: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if tags is not None:
            _body["tags"] = tags
        if id is not None:
            _body["id"] = id
        if category is not None:
            _body["category"] = category
        if name is not None:
            _body["name"] = name
        if photo_urls is not None:
            _body["photoUrls"] = photo_urls
        if status is not None:
            _body["status"] = status
        args.body = _body
        return args

    async def _aadd_oapg(
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
        Add a new pet to the store
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
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pet.serialize(body, content_type)
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
            auth_settings=_auth,
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


    def _add_oapg(
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
        Add a new pet to the store
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
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pet.serialize(body, content_type)
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
            auth_settings=_auth,
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


class AddRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd(
        self,
        name: str,
        photo_urls: PetPhotoUrls,
        tags: typing.Optional[typing.List[Tag]] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[Category] = None,
        status: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_mapped_args(
            name=name,
            photo_urls=photo_urls,
            tags=tags,
            id=id,
            category=category,
            status=status,
        )
        return await self._aadd_oapg(
            body=args.body,
            **kwargs,
        )
    
    def add(
        self,
        name: str,
        photo_urls: PetPhotoUrls,
        tags: typing.Optional[typing.List[Tag]] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[Category] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_mapped_args(
            name=name,
            photo_urls=photo_urls,
            tags=tags,
            id=id,
            category=category,
            status=status,
        )
        return self._add_oapg(
            body=args.body,
        )

class Add(BaseApi):

    async def aadd(
        self,
        name: str,
        photo_urls: PetPhotoUrls,
        tags: typing.Optional[typing.List[Tag]] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[Category] = None,
        status: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PetPydantic:
        raw_response = await self.raw.aadd(
            name=name,
            photo_urls=photo_urls,
            tags=tags,
            id=id,
            category=category,
            status=status,
            **kwargs,
        )
        if validate:
            return PetPydantic(**raw_response.body)
        return api_client.construct_model_instance(PetPydantic, raw_response.body)
    
    
    def add(
        self,
        name: str,
        photo_urls: PetPhotoUrls,
        tags: typing.Optional[typing.List[Tag]] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[Category] = None,
        status: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PetPydantic:
        raw_response = self.raw.add(
            name=name,
            photo_urls=photo_urls,
            tags=tags,
            id=id,
            category=category,
            status=status,
        )
        if validate:
            return PetPydantic(**raw_response.body)
        return api_client.construct_model_instance(PetPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        photo_urls: PetPhotoUrls,
        tags: typing.Optional[typing.List[Tag]] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[Category] = None,
        status: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_mapped_args(
            name=name,
            photo_urls=photo_urls,
            tags=tags,
            id=id,
            category=category,
            status=status,
        )
        return await self._aadd_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        photo_urls: PetPhotoUrls,
        tags: typing.Optional[typing.List[Tag]] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[Category] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_mapped_args(
            name=name,
            photo_urls=photo_urls,
            tags=tags,
            id=id,
            category=category,
            status=status,
        )
        return self._add_oapg(
            body=args.body,
        )

