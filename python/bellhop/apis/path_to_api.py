import typing_extensions

from bellhop.paths import PathValues
from bellhop.apis.paths.pagination import Pagination
from bellhop.apis.paths.pet import Pet
from bellhop.apis.paths.pet_find_by_status import PetFindByStatus
from bellhop.apis.paths.pet_find_by_tags import PetFindByTags
from bellhop.apis.paths.pet_pet_id import PetPetId
from bellhop.apis.paths.pet_pet_id_upload_image import PetPetIdUploadImage
from bellhop.apis.paths.store_inventory import StoreInventory
from bellhop.apis.paths.store_order import StoreOrder
from bellhop.apis.paths.store_order_order_id import StoreOrderOrderId
from bellhop.apis.paths.user import User
from bellhop.apis.paths.user_create_with_array import UserCreateWithArray
from bellhop.apis.paths.user_create_with_list import UserCreateWithList
from bellhop.apis.paths.user_login import UserLogin
from bellhop.apis.paths.user_logout import UserLogout
from bellhop.apis.paths.user_username import UserUsername

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PAGINATION: Pagination,
        PathValues.PET: Pet,
        PathValues.PET_FIND_BY_STATUS: PetFindByStatus,
        PathValues.PET_FIND_BY_TAGS: PetFindByTags,
        PathValues.PET_PET_ID: PetPetId,
        PathValues.PET_PET_ID_UPLOAD_IMAGE: PetPetIdUploadImage,
        PathValues.STORE_INVENTORY: StoreInventory,
        PathValues.STORE_ORDER: StoreOrder,
        PathValues.STORE_ORDER_ORDER_ID: StoreOrderOrderId,
        PathValues.USER: User,
        PathValues.USER_CREATE_WITH_ARRAY: UserCreateWithArray,
        PathValues.USER_CREATE_WITH_LIST: UserCreateWithList,
        PathValues.USER_LOGIN: UserLogin,
        PathValues.USER_LOGOUT: UserLogout,
        PathValues.USER_USERNAME: UserUsername,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PAGINATION: Pagination,
        PathValues.PET: Pet,
        PathValues.PET_FIND_BY_STATUS: PetFindByStatus,
        PathValues.PET_FIND_BY_TAGS: PetFindByTags,
        PathValues.PET_PET_ID: PetPetId,
        PathValues.PET_PET_ID_UPLOAD_IMAGE: PetPetIdUploadImage,
        PathValues.STORE_INVENTORY: StoreInventory,
        PathValues.STORE_ORDER: StoreOrder,
        PathValues.STORE_ORDER_ORDER_ID: StoreOrderOrderId,
        PathValues.USER: User,
        PathValues.USER_CREATE_WITH_ARRAY: UserCreateWithArray,
        PathValues.USER_CREATE_WITH_LIST: UserCreateWithList,
        PathValues.USER_LOGIN: UserLogin,
        PathValues.USER_LOGOUT: UserLogout,
        PathValues.USER_USERNAME: UserUsername,
    }
)
