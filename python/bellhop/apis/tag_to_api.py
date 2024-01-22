import typing_extensions

from bellhop.apis.tags import TagValues
from bellhop.apis.tags.pet_api import PetApi
from bellhop.apis.tags.user_api import UserApi
from bellhop.apis.tags.store_api import StoreApi
from bellhop.apis.tags.miscellaneous_api import MiscellaneousApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PET: PetApi,
        TagValues.USER: UserApi,
        TagValues.STORE: StoreApi,
        TagValues.MISCELLANEOUS: MiscellaneousApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PET: PetApi,
        TagValues.USER: UserApi,
        TagValues.STORE: StoreApi,
        TagValues.MISCELLANEOUS: MiscellaneousApi,
    }
)
