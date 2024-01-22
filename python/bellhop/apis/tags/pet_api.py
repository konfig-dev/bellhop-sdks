# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from bellhop.paths.pet.post import Add
from bellhop.paths.pet_pet_id.delete import Delete
from bellhop.paths.pet_find_by_status.get import FindByStatus
from bellhop.paths.pet_find_by_tags.get import FindByTags
from bellhop.paths.pet_pet_id.get import GetById
from bellhop.paths.pet.put import Update
from bellhop.paths.pet_pet_id.post import UpdateWithForm
from bellhop.paths.pet_pet_id_upload_image.post import UploadImage
from bellhop.apis.tags.pet_api_raw import PetApiRaw


class PetApi(
    Add,
    Delete,
    FindByStatus,
    FindByTags,
    GetById,
    Update,
    UpdateWithForm,
    UploadImage,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PetApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PetApiRaw(api_client)