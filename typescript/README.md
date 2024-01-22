<div align="center">

[![Visit Bellhop](./header.png)](https://www.getbellhops.com)

# [Bellhop](https://www.getbellhops.com)<a id="bellhop"></a>

This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.

[![npm](https://img.shields.io/badge/npm-v1.0.0-blue)](https://www.npmjs.com/package/bellhop-typescript-sdk/v/1.0.0)

</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Reference](#reference)
  * [`bellhop.miscellaneous.paginate`](#bellhopmiscellaneouspaginate)
  * [`bellhop.pet.add`](#bellhoppetadd)
  * [`bellhop.pet.delete`](#bellhoppetdelete)
  * [`bellhop.pet.findByStatus`](#bellhoppetfindbystatus)
  * [`bellhop.pet.findByTags`](#bellhoppetfindbytags)
  * [`bellhop.pet.getById`](#bellhoppetgetbyid)
  * [`bellhop.pet.update`](#bellhoppetupdate)
  * [`bellhop.pet.updateWithForm`](#bellhoppetupdatewithform)
  * [`bellhop.pet.uploadImage`](#bellhoppetuploadimage)
  * [`bellhop.store.deleteOrder`](#bellhopstoredeleteorder)
  * [`bellhop.store.getInventory`](#bellhopstoregetinventory)
  * [`bellhop.store.getOrderById`](#bellhopstoregetorderbyid)
  * [`bellhop.store.placeOrder`](#bellhopstoreplaceorder)
  * [`bellhop.user.create`](#bellhopusercreate)
  * [`bellhop.user.createWithArray`](#bellhopusercreatewitharray)
  * [`bellhop.user.createWithList`](#bellhopusercreatewithlist)
  * [`bellhop.user.delete`](#bellhopuserdelete)
  * [`bellhop.user.getByName`](#bellhopusergetbyname)
  * [`bellhop.user.login`](#bellhopuserlogin)
  * [`bellhop.user.logout`](#bellhopuserlogout)
  * [`bellhop.user.update`](#bellhopuserupdate)

<!-- tocstop -->

## Installation<a id="installation"></a>

<table>
<tr>
<th width="292px"><code>npm</code></th>
<th width="293px"><code>pnpm</code></th>
<th width="292px"><code>yarn</code></th>
</tr>
<tr>
<td>

```bash
npm i bellhop-typescript-sdk
```

</td>
<td>

```bash
pnpm i bellhop-typescript-sdk
```

</td>
<td>

```bash
yarn add bellhop-typescript-sdk
```

</td>
</tr>
</table>

## Getting Started<a id="getting-started"></a>

```typescript
import { Bellhop } from "bellhop-typescript-sdk";

const bellhop = new Bellhop({
  // Defining the base path is optional and defaults to https://petstore.swagger.io/v2
  // basePath: "https://petstore.swagger.io/v2",
  apiKey: "API_KEY",
  accessToken: "ACCESS_TOKEN",
});

const paginateResponse = await bellhop.miscellaneous.paginate({});

console.log(paginateResponse);
```

## Reference<a id="reference"></a>


### `bellhop.miscellaneous.paginate`<a id="bellhopmiscellaneouspaginate"></a>

Iterate through a bunch of items

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const paginateResponse = await bellhop.miscellaneous.paginate({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first: `number`<a id="first-number"></a>

##### after: `string`<a id="after-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[PaginateResponse](./models/paginate-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pagination` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.pet.add`<a id="bellhoppetadd"></a>

test 2

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const addResponse = await bellhop.pet.add({
  name: "doggie",
  photoUrls: ["photoUrls_example"],
  status: "available",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `string`<a id="name-string"></a>

##### photoUrls: `string`[]<a id="photourls-string"></a>

##### tags: [`Tag`](./models/tag.ts)[]<a id="tags-tagmodelstagts"></a>

##### id: `number`<a id="id-number"></a>

##### category: [`Category`](./models/category.ts)<a id="category-categorymodelscategoryts"></a>

##### status: `string`<a id="status-string"></a>

pet status in the store

#### 🔄 Return<a id="🔄-return"></a>

[Pet](./models/pet.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.pet.delete`<a id="bellhoppetdelete"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await bellhop.pet.delete({
  petId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### petId: `number`<a id="petid-number"></a>

Pet id to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/{petId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.pet.findByStatus`<a id="bellhoppetfindbystatus"></a>

Multiple status values can be provided with comma separated strings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const findByStatusResponse = await bellhop.pet.findByStatus({
  status: ["available"],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `string`[]<a id="status-string"></a>

Status values that need to be considered for filter

#### 🔄 Return<a id="🔄-return"></a>

[Pet](./models/pet.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/findByStatus` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.pet.findByTags`<a id="bellhoppetfindbytags"></a>

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const findByTagsResponse = await bellhop.pet.findByTags({
  tags: ["tags_example"],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: `string`[]<a id="tags-string"></a>

Tags to filter by

#### 🔄 Return<a id="🔄-return"></a>

[Pet](./models/pet.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/findByTags` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.pet.getById`<a id="bellhoppetgetbyid"></a>

Returns a single pet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getByIdResponse = await bellhop.pet.getById({
  petId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### petId: `number`<a id="petid-number"></a>

ID of pet to return

#### 🔄 Return<a id="🔄-return"></a>

[Pet](./models/pet.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/{petId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.pet.update`<a id="bellhoppetupdate"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await bellhop.pet.update({
  name: "doggie",
  photoUrls: ["photoUrls_example"],
  status: "available",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `string`<a id="name-string"></a>

##### photoUrls: `string`[]<a id="photourls-string"></a>

##### tags: [`Tag`](./models/tag.ts)[]<a id="tags-tagmodelstagts"></a>

##### id: `number`<a id="id-number"></a>

##### category: [`Category`](./models/category.ts)<a id="category-categorymodelscategoryts"></a>

##### status: `string`<a id="status-string"></a>

pet status in the store

#### 🔄 Return<a id="🔄-return"></a>

[Pet](./models/pet.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.pet.updateWithForm`<a id="bellhoppetupdatewithform"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateWithFormResponse = await bellhop.pet.updateWithForm({
  petId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### petId: `number`<a id="petid-number"></a>

ID of pet that needs to be updated

##### name: `string`<a id="name-string"></a>

Updated name of the pet

##### status: `string`<a id="status-string"></a>

Updated status of the pet

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/{petId}` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.pet.uploadImage`<a id="bellhoppetuploadimage"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const uploadImageResponse = await bellhop.pet.uploadImage({
  petId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### petId: `number`<a id="petid-number"></a>

ID of pet to update

##### additionalMetadata: `string`<a id="additionalmetadata-string"></a>

Additional data to pass to server

##### file: `Uint8Array | File | buffer.File`<a id="file-uint8array--file--bufferfile"></a>

file to upload

#### 🔄 Return<a id="🔄-return"></a>

[ApiResponse](./models/api-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pet/{petId}/uploadImage` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.store.deleteOrder`<a id="bellhopstoredeleteorder"></a>

For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteOrderResponse = await bellhop.store.deleteOrder({
  orderId: "orderId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### orderId: `string`<a id="orderid-string"></a>

ID of the order that needs to be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/store/order/{orderId}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.store.getInventory`<a id="bellhopstoregetinventory"></a>

Returns a map of status codes to quantities

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getInventoryResponse = await bellhop.store.getInventory();
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/store/inventory` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.store.getOrderById`<a id="bellhopstoregetorderbyid"></a>

For valid response try integer IDs with value <= 5 or > 10. Other values will generated exceptions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getOrderByIdResponse = await bellhop.store.getOrderById({
  orderId: 1,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### orderId: `number`<a id="orderid-number"></a>

ID of pet that needs to be fetched

#### 🔄 Return<a id="🔄-return"></a>

[Order](./models/order.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/store/order/{orderId}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.store.placeOrder`<a id="bellhopstoreplaceorder"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const placeOrderResponse = await bellhop.store.placeOrder({
  status: "placed",
  complete: false,
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `number`<a id="id-number"></a>

##### petId: `number`<a id="petid-number"></a>

##### quantity: `number`<a id="quantity-number"></a>

##### shipDate: `string`<a id="shipdate-string"></a>

##### status: `string`<a id="status-string"></a>

Order Status

##### complete: `boolean`<a id="complete-boolean"></a>

#### 🔄 Return<a id="🔄-return"></a>

[Order](./models/order.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/store/order` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.user.create`<a id="bellhopusercreate"></a>

This can only be done by the logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await bellhop.user.create({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `number`<a id="id-number"></a>

##### username: `string`<a id="username-string"></a>

##### firstName: `string`<a id="firstname-string"></a>

##### lastName: `string`<a id="lastname-string"></a>

##### email: `string`<a id="email-string"></a>

##### password: `string`<a id="password-string"></a>

##### phone: `string`<a id="phone-string"></a>

##### userStatus: `number`<a id="userstatus-number"></a>

User Status

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.user.createWithArray`<a id="bellhopusercreatewitharray"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createWithArrayResponse = await bellhop.user.createWithArray([{}]);
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`User`](./models/user.ts)[]

List of user object

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/createWithArray` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.user.createWithList`<a id="bellhopusercreatewithlist"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createWithListResponse = await bellhop.user.createWithList([{}]);
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`User`](./models/user.ts)[]

List of user object

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/createWithList` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.user.delete`<a id="bellhopuserdelete"></a>

This can only be done by the logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await bellhop.user.delete({
  username: "username_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `string`<a id="username-string"></a>

The name that needs to be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/{username}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.user.getByName`<a id="bellhopusergetbyname"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getByNameResponse = await bellhop.user.getByName({
  username: "username_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `string`<a id="username-string"></a>

The name that needs to be fetched. Use user1 for testing.

#### 🔄 Return<a id="🔄-return"></a>

[User](./models/user.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/{username}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.user.login`<a id="bellhopuserlogin"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const loginResponse = await bellhop.user.login({
  username:
    "CbUUGjjNSwg0_bs9ZayIMrKdgNvb6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz.5awLMdeXylwK0lMGUSM4jsrh4dstlnQUN5vVdMLPA",
  password: "password_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `string`<a id="username-string"></a>

The user name for login

##### password: `string`<a id="password-string"></a>

The password for login in clear text

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/login` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.user.logout`<a id="bellhopuserlogout"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const logoutResponse = await bellhop.user.logout();
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/logout` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.user.update`<a id="bellhopuserupdate"></a>

This can only be done by the logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await bellhop.user.update({
  username: "username_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `string`<a id="username-string"></a>

name that need to be deleted

##### id: `number`<a id="id-number"></a>

##### firstName: `string`<a id="firstname-string"></a>

##### lastName: `string`<a id="lastname-string"></a>

##### email: `string`<a id="email-string"></a>

##### password: `string`<a id="password-string"></a>

##### phone: `string`<a id="phone-string"></a>

##### userStatus: `number`<a id="userstatus-number"></a>

User Status

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/{username}` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This TypeScript package is automatically generated by [Konfig](https://konfigthis.com)
