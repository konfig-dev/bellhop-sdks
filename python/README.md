<div align="center">

[![Visit Bellhop](https://raw.githubusercontent.com/konfig-dev/bellhop-sdks/HEAD/python/header.png)](https://www.getbellhops.com)

# Bellhop<a id="bellhop"></a>

This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.


[![PyPI](https://img.shields.io/badge/PyPI-v1.0.0-blue)](https://pypi.org/project/bellhop-python-sdk/1.0.0)
[![README.md](https://img.shields.io/badge/README-Click%20Here-green)](https://github.com/konfig-dev/bellhop-sdks/tree/main/python#readme)

</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installing](#installing)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`bellhop.miscellaneous.paginate`](#bellhopmiscellaneouspaginate)
  * [`bellhop.pet.add`](#bellhoppetadd)
  * [`bellhop.pet.delete`](#bellhoppetdelete)
  * [`bellhop.pet.find_by_status`](#bellhoppetfind_by_status)
  * [`bellhop.pet.find_by_tags`](#bellhoppetfind_by_tags)
  * [`bellhop.pet.get_by_id`](#bellhoppetget_by_id)
  * [`bellhop.pet.update`](#bellhoppetupdate)
  * [`bellhop.pet.update_with_form`](#bellhoppetupdate_with_form)
  * [`bellhop.pet.upload_image`](#bellhoppetupload_image)
  * [`bellhop.store.delete_order`](#bellhopstoredelete_order)
  * [`bellhop.store.get_inventory`](#bellhopstoreget_inventory)
  * [`bellhop.store.get_order_by_id`](#bellhopstoreget_order_by_id)
  * [`bellhop.store.place_order`](#bellhopstoreplace_order)
  * [`bellhop.user.create`](#bellhopusercreate)
  * [`bellhop.user.create_with_array`](#bellhopusercreate_with_array)
  * [`bellhop.user.create_with_list`](#bellhopusercreate_with_list)
  * [`bellhop.user.delete`](#bellhopuserdelete)
  * [`bellhop.user.get_by_name`](#bellhopuserget_by_name)
  * [`bellhop.user.login`](#bellhopuserlogin)
  * [`bellhop.user.logout`](#bellhopuserlogout)
  * [`bellhop.user.update`](#bellhopuserupdate)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installing<a id="installing"></a>

```sh
pip install bellhop-python-sdk==1.0.0
```

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from bellhop import Bellhop, ApiException

bellhop = Bellhop()

try:
    # Pagination sandbox
    paginate_response = bellhop.miscellaneous.paginate(
        first=1,
        after="string_example",
    )
    print(paginate_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi.paginate: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from bellhop import Bellhop, ApiException

bellhop = Bellhop()


async def main():
    try:
        # Pagination sandbox
        paginate_response = await bellhop.miscellaneous.apaginate(
            first=1,
            after="string_example",
        )
        print(paginate_response)
    except ApiException as e:
        print("Exception when calling MiscellaneousApi.paginate: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from bellhop import Bellhop, ApiException

bellhop = Bellhop()

try:
    # Pagination sandbox
    paginate_response = bellhop.miscellaneous.raw.paginate(
        first=1,
        after="string_example",
    )
    pprint(paginate_response.body)
    pprint(paginate_response.body["edges"])
    pprint(paginate_response.body["page_info"])
    pprint(paginate_response.headers)
    pprint(paginate_response.status)
    pprint(paginate_response.round_trip_time)
except ApiException as e:
    print("Exception when calling MiscellaneousApi.paginate: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `bellhop.miscellaneous.paginate`<a id="bellhopmiscellaneouspaginate"></a>

Iterate through a bunch of items

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paginate_response = bellhop.miscellaneous.paginate(
    first=1,
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first: `int`<a id="first-int"></a>

##### after: `str`<a id="after-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaginateRequest`](./bellhop/type/paginate_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaginateResponse`](./bellhop/pydantic/paginate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pagination` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.pet.add`<a id="bellhoppetadd"></a>

test 2

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_response = bellhop.pet.add(
    name="doggie",
    photo_urls=["string_example"],
    tags=[{}],
    id=1,
    category={},
    status="available",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### photo_urls: [`PetPhotoUrls`](./bellhop/type/pet_photo_urls.py)<a id="photo_urls-petphotourlsbellhoptypepet_photo_urlspy"></a>

##### tags: List[`Tag`]<a id="tags-listtag"></a>

##### id: `int`<a id="id-int"></a>

##### category: [`Category`](./bellhop/type/category.py)<a id="category-categorybellhoptypecategorypy"></a>


##### status: `str`<a id="status-str"></a>

pet status in the store

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Pet`](./bellhop/type/pet.py)
Pet object that needs to be added to the store

#### 🔄 Return<a id="🔄-return"></a>

[`Pet`](./bellhop/pydantic/pet.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.pet.delete`<a id="bellhoppetdelete"></a>

Deletes a pet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.pet.delete(
    pet_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pet_id: `int`<a id="pet_id-int"></a>

Pet id to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/{petId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.pet.find_by_status`<a id="bellhoppetfind_by_status"></a>

Multiple status values can be provided with comma separated strings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_status_response = bellhop.pet.find_by_status(
    status=["available"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: List[`str`]<a id="status-liststr"></a>

Status values that need to be considered for filter

#### 🔄 Return<a id="🔄-return"></a>

[`FindByStatusResponse`](./bellhop/pydantic/find_by_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/findByStatus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.pet.find_by_tags`<a id="bellhoppetfind_by_tags"></a>

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_tags_response = bellhop.pet.find_by_tags(
    tags=["tags_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: List[`str`]<a id="tags-liststr"></a>

Tags to filter by

#### 🔄 Return<a id="🔄-return"></a>

[`FindByTagsResponse`](./bellhop/pydantic/find_by_tags_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/findByTags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.pet.get_by_id`<a id="bellhoppetget_by_id"></a>

Returns a single pet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = bellhop.pet.get_by_id(
    pet_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pet_id: `int`<a id="pet_id-int"></a>

ID of pet to return

#### 🔄 Return<a id="🔄-return"></a>

[`Pet`](./bellhop/pydantic/pet.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/{petId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.pet.update`<a id="bellhoppetupdate"></a>

Update an existing pet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = bellhop.pet.update(
    name="doggie",
    photo_urls=["string_example"],
    tags=[{}],
    id=1,
    category={},
    status="available",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### photo_urls: [`PetPhotoUrls`](./bellhop/type/pet_photo_urls.py)<a id="photo_urls-petphotourlsbellhoptypepet_photo_urlspy"></a>

##### tags: List[`Tag`]<a id="tags-listtag"></a>

##### id: `int`<a id="id-int"></a>

##### category: [`Category`](./bellhop/type/category.py)<a id="category-categorybellhoptypecategorypy"></a>


##### status: `str`<a id="status-str"></a>

pet status in the store

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Pet`](./bellhop/type/pet.py)
Pet object that needs to be added to the store

#### 🔄 Return<a id="🔄-return"></a>

[`Pet`](./bellhop/pydantic/pet.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.pet.update_with_form`<a id="bellhoppetupdate_with_form"></a>

Updates a pet in the store with form data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.pet.update_with_form(
    pet_id=1,
    name="string_example",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pet_id: `int`<a id="pet_id-int"></a>

ID of pet that needs to be updated

##### name: `str`<a id="name-str"></a>

Updated name of the pet

##### status: `str`<a id="status-str"></a>

Updated status of the pet

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateWithFormRequest`](./bellhop/type/update_with_form_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/{petId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.pet.upload_image`<a id="bellhoppetupload_image"></a>

uploads an image

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_image_response = bellhop.pet.upload_image(
    pet_id=1,
    additional_metadata="string_example",
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pet_id: `int`<a id="pet_id-int"></a>

ID of pet to update

##### additional_metadata: `str`<a id="additional_metadata-str"></a>

Additional data to pass to server

##### file: `IO`<a id="file-io"></a>

file to upload

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadImageRequest`](./bellhop/type/upload_image_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApiResponse`](./bellhop/pydantic/api_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/{petId}/uploadImage` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.store.delete_order`<a id="bellhopstoredelete_order"></a>

For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.store.delete_order(
    order_id="orderId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### order_id: `str`<a id="order_id-str"></a>

ID of the order that needs to be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/store/order/{orderId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.store.get_inventory`<a id="bellhopstoreget_inventory"></a>

Returns a map of status codes to quantities

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_inventory_response = bellhop.store.get_inventory()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetInventoryResponse`](./bellhop/pydantic/get_inventory_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/store/inventory` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.store.get_order_by_id`<a id="bellhopstoreget_order_by_id"></a>

For valid response try integer IDs with value <= 5 or > 10. Other values will generated exceptions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_order_by_id_response = bellhop.store.get_order_by_id(
    order_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### order_id: `int`<a id="order_id-int"></a>

ID of pet that needs to be fetched

#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./bellhop/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/store/order/{orderId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.store.place_order`<a id="bellhopstoreplace_order"></a>

Place an order for a pet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
place_order_response = bellhop.store.place_order(
    id=1,
    pet_id=1,
    quantity=1,
    ship_date="1970-01-01T00:00:00.00Z",
    status="placed",
    complete=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### pet_id: `int`<a id="pet_id-int"></a>

##### quantity: `int`<a id="quantity-int"></a>

##### ship_date: `datetime`<a id="ship_date-datetime"></a>

##### status: `str`<a id="status-str"></a>

Order Status

##### complete: `bool`<a id="complete-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Order`](./bellhop/type/order.py)
order placed for purchasing the pet

#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./bellhop/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/store/order` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.user.create`<a id="bellhopusercreate"></a>

This can only be done by the logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.user.create(
    id=1,
    username="string_example",
    first_name="string_example",
    last_name="string_example",
    email="string_example",
    password="string_example",
    phone="string_example",
    user_status=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### username: `str`<a id="username-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email: `str`<a id="email-str"></a>

##### password: `str`<a id="password-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### user_status: `int`<a id="user_status-int"></a>

User Status

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`User`](./bellhop/type/user.py)
Created user object

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.user.create_with_array`<a id="bellhopusercreate_with_array"></a>

Creates list of users with given input array

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.user.create_with_array(
    body=[{}],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateWithArrayRequest`](./bellhop/type/create_with_array_request.py)
List of user object

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/createWithArray` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.user.create_with_list`<a id="bellhopusercreate_with_list"></a>

Creates list of users with given input array

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.user.create_with_list(
    body=[{}],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateWithArrayRequest`](./bellhop/type/create_with_array_request.py)
List of user object

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/createWithList` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.user.delete`<a id="bellhopuserdelete"></a>

This can only be done by the logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.user.delete(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

The name that needs to be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/{username}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.user.get_by_name`<a id="bellhopuserget_by_name"></a>

Get user by user name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_name_response = bellhop.user.get_by_name(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

The name that needs to be fetched. Use user1 for testing.

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./bellhop/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/{username}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.user.login`<a id="bellhopuserlogin"></a>

Logs user into the system

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
login_response = bellhop.user.login(
    username="CbUUGjjNSwg0_bs9ZayIMrKdgNvb6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz.5awLMdeXylwK0lMGUSM4jsrh4dstlnQUN5vVdMLPA",
    password="password_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

The user name for login

##### password: `str`<a id="password-str"></a>

The password for login in clear text

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/login` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.user.logout`<a id="bellhopuserlogout"></a>

Logs out current logged in user session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.user.logout()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/logout` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bellhop.user.update`<a id="bellhopuserupdate"></a>

This can only be done by the logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bellhop.user.update(
    username="username_example",
    id=1,
    first_name="string_example",
    last_name="string_example",
    email="string_example",
    password="string_example",
    phone="string_example",
    user_status=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

name that need to be deleted

##### id: `int`<a id="id-int"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email: `str`<a id="email-str"></a>

##### password: `str`<a id="password-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### user_status: `int`<a id="user_status-int"></a>

User Status

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserCreateRequest`](./bellhop/type/user_create_request.py)
Updated user object

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/{username}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
