<div align="center">

[![Visit Bellhop](./header.png)](https://www.getbellhops.com)

# [Bellhop](https://www.getbellhops.com)<a id="bellhop"></a>

Bellhop's Partner API

[![npm](https://img.shields.io/badge/npm-v0.1.3-blue)](https://www.npmjs.com/package/bellhop-partners-typescript/v/0.1.3)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](http://www.bellhop.com/)

</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Reference](#reference)
  * [`bellhop.lead.create`](#bellhopleadcreate)
  * [`bellhop.lead.delete`](#bellhopleaddelete)
  * [`bellhop.lead.get`](#bellhopleadget)
  * [`bellhop.lead.list`](#bellhopleadlist)
  * [`bellhop.lead.update`](#bellhopleadupdate)
  * [`bellhop.location.create`](#bellhoplocationcreate)
  * [`bellhop.order.create`](#bellhopordercreate)
  * [`bellhop.postalCode.serviceability`](#bellhoppostalcodeserviceability)
  * [`bellhop.quote.create`](#bellhopquotecreate)
  * [`bellhop.quote.deleteInventory`](#bellhopquotedeleteinventory)
  * [`bellhop.quote.get`](#bellhopquoteget)
  * [`bellhop.quote.getInventory`](#bellhopquotegetinventory)
  * [`bellhop.quote.updateInventory`](#bellhopquoteupdateinventory)
  * [`bellhop.quoteServiceGroup.changeLocations`](#bellhopquoteservicegroupchangelocations)
  * [`bellhop.quoteServiceGroup.create`](#bellhopquoteservicegroupcreate)
  * [`bellhop.quoteServiceGroup.createEstimate`](#bellhopquoteservicegroupcreateestimate)
  * [`bellhop.quoteServiceGroup.createFlexible`](#bellhopquoteservicegroupcreateflexible)
  * [`bellhop.quoteServiceGroup.delete`](#bellhopquoteservicegroupdelete)
  * [`bellhop.quoteServiceGroup.get`](#bellhopquoteservicegroupget)
  * [`bellhop.quoteServiceGroup.update`](#bellhopquoteservicegroupupdate)
  * [`bellhop.quoteServiceGroup.updateServices`](#bellhopquoteservicegroupupdateservices)

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
npm i bellhop-partners-typescript
```

</td>
<td>

```bash
pnpm i bellhop-partners-typescript
```

</td>
<td>

```bash
yarn add bellhop-partners-typescript
```

</td>
</tr>
</table>

## Getting Started<a id="getting-started"></a>

```typescript
import { Bellhop } from "bellhop-partners-typescript";

const bellhop = new Bellhop({
  // Defining the base path is optional and defaults to https://partners.bellhops.dev/v5
  // basePath: "https://partners.bellhops.dev/v5",
  oauthClientId: "CLIENT_ID",
  oauthClientSecret: "CLIENT_SECRET",
});

const createResponse = await bellhop.lead.create({
  first_name: "first_name_example",
  last_name: "last_name_example",
  lead_type: "string_example",
  lead_record_type: "string_example",
  origin_postal_code: "85001",
  origin_state: "AZ",
  destination_postal_code: "85001",
  destination_state: "AZ",
  load_date: "2021-01-01",
  close_date: "2021-01-01",
});

console.log(createResponse);
```

## Reference<a id="reference"></a>


### `bellhop.lead.create`<a id="bellhopleadcreate"></a>

Create Lead

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await bellhop.lead.create({
  first_name: "first_name_example",
  last_name: "last_name_example",
  lead_type: "string_example",
  lead_record_type: "string_example",
  origin_postal_code: "85001",
  origin_state: "AZ",
  destination_postal_code: "85001",
  destination_state: "AZ",
  load_date: "2021-01-01",
  close_date: "2021-01-01",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `string`<a id="first_name-string"></a>

##### last_name: `string`<a id="last_name-string"></a>

##### lead_type: [`LeadType`](./models/lead-type.ts)<a id="lead_type-leadtypemodelslead-typets"></a>

##### lead_record_type: [`LeadRecordType`](./models/lead-record-type.ts)<a id="lead_record_type-leadrecordtypemodelslead-record-typets"></a>

##### description: `string`<a id="description-string"></a>

##### external_id: `string`<a id="external_id-string"></a>

##### lead_source: `string`<a id="lead_source-string"></a>

##### email: `string`<a id="email-string"></a>

##### phone: `string`<a id="phone-string"></a>

##### origin_postal_code: `string`<a id="origin_postal_code-string"></a>

##### origin_street: `string`<a id="origin_street-string"></a>

##### origin_city: `string`<a id="origin_city-string"></a>

##### origin_state: `string`<a id="origin_state-string"></a>

##### origin_square_feet: `number`<a id="origin_square_feet-number"></a>

##### destination_postal_code: `string`<a id="destination_postal_code-string"></a>

##### destination_street: `string`<a id="destination_street-string"></a>

##### destination_city: `string`<a id="destination_city-string"></a>

##### destination_state: `string`<a id="destination_state-string"></a>

##### clickid: `string`<a id="clickid-string"></a>

##### gclid: `string`<a id="gclid-string"></a>

##### utm_medium: `string`<a id="utm_medium-string"></a>

##### utm_source: `string`<a id="utm_source-string"></a>

##### utm_campaign: `string`<a id="utm_campaign-string"></a>

##### msclkid: `string`<a id="msclkid-string"></a>

##### load_date: `string`<a id="load_date-string"></a>

##### close_date: `string`<a id="close_date-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[LeadResponse](./models/lead-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leads` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.lead.delete`<a id="bellhopleaddelete"></a>

Cancel Lead

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await bellhop.lead.delete({
  leadId: "leadId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leadId: `string`<a id="leadid-string"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leads/{lead_id}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.lead.get`<a id="bellhopleadget"></a>

Get Lead

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await bellhop.lead.get({
  leadId: "leadId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leadId: `string`<a id="leadid-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[LeadResponse](./models/lead-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leads/{lead_id}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.lead.list`<a id="bellhopleadlist"></a>

List Leads

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const listResponse = await bellhop.lead.list({});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `string`<a id="email-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[LeadResponse](./models/lead-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leads` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.lead.update`<a id="bellhopleadupdate"></a>

Update attributes of a lead.

:lead_id: The ID of the lead to update. This can be either the bellhop id or the external_id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await bellhop.lead.update({
  leadId: "leadId_example",
  description: "description_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `string`<a id="description-string"></a>

##### leadId: `string`<a id="leadid-string"></a>

##### close_date: `string`<a id="close_date-string"></a>

##### load_date: `string`<a id="load_date-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[LeadResponse](./models/lead-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/leads/{lead_id}` `PATCH`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.location.create`<a id="bellhoplocationcreate"></a>

Create quoting location object from address

Create Quoting Location standardizes input address via USPS and generates
geo-location details Google Maps APIs.
The location id is a hash of the required fields on the location object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await bellhop.location.create({
  line_1: "line_1_example",
  city: "city_example",
  state: "state_example",
  postal_code: "postal_code_example",
  country: "US",
  property_type: "string_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### line_1: `string`<a id="line_1-string"></a>

##### city: `string`<a id="city-string"></a>

##### state: `string`<a id="state-string"></a>

##### postal_code: `string`<a id="postal_code-string"></a>

##### property_type: [`PropertyType`](./models/property-type.ts)<a id="property_type-propertytypemodelsproperty-typets"></a>

Type of the property.

##### line_2: `string`<a id="line_2-string"></a>

##### country: `string`<a id="country-string"></a>

##### rooms: `number`<a id="rooms-number"></a>

Number of rooms in the property.

##### area: `number`<a id="area-number"></a>

Total area of the property in square feet.

##### garage: `boolean`<a id="garage-boolean"></a>

Indicates whether the property has a garage or not.

##### stories: `number`<a id="stories-number"></a>

Number of stories or floors in the property.

##### floor: `number`<a id="floor-number"></a>

Floor number of the property.

##### attic: `boolean`<a id="attic-boolean"></a>

Indicates whether the property has an attic or not.

##### basement: `boolean`<a id="basement-boolean"></a>

Indicates whether the property has a basement or not.

#### 🔄 Return<a id="🔄-return"></a>

[LocationResponse](./models/location-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.order.create`<a id="bellhopordercreate"></a>

Creates an order from a quote

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await bellhop.order.create({
  quoteId: "quoteId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

Quote ID to generate order from

#### 🔄 Return<a id="🔄-return"></a>

[OrderResponseV2](./models/order-response-v2.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders/{quote_id}` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.postalCode.serviceability`<a id="bellhoppostalcodeserviceability"></a>

Get Postal Codes Serviceability V5

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const serviceabilityResponse = await bellhop.postalCode.serviceability({
  originPostalCode: "originPostalCode_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### originPostalCode: `string`<a id="originpostalcode-string"></a>

##### destinationPostalCode: `string`<a id="destinationpostalcode-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[PostalCodesServiceabilityResponse](./models/postal-codes-serviceability-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/postal-codes/serviceability` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quote.create`<a id="bellhopquotecreate"></a>

Creates a quote

Creates a quote for a given customer using the provided locations and service code.
The LOCALFULLSERVICE service code will generate a service group with
LOADINGUNLOADING and TRANSIT services.
All other service codes generate service groups with a single service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await bellhop.quote.create({
  customer: {
    first_name: "first_name_example",
    last_name: "last_name_example",
    phone: "phone_example",
    email: "email_example",
  },
  start_datetime: "2024-02-05T15:50:48.765645",
  service_code: "LOCALFULLSERVICE",
  locations: {
    key: {
      line_1: "line_1_example",
      city: "city_example",
      state: "state_example",
      postal_code: "postal_code_example",
      country: "US",
    },
  },
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer: [`CreateQuoteRequestCustomer`](./models/create-quote-request-customer.ts)<a id="customer-createquoterequestcustomermodelscreate-quote-request-customerts"></a>

##### start_datetime: `string`<a id="start_datetime-string"></a>

Start date and time of the quote

##### service_code: `string`<a id="service_code-string"></a>

Services to be quoted

##### locations: Record<string, [`LocationRequest`](./models/location-request.ts)><a id="locations-record"></a>

Mapping locations and their sequence

##### inventory: [`SetQuoteInventoryRequestNullable`](./models/set-quote-inventory-request-nullable.ts)<a id="inventory-setquoteinventoryrequestnullablemodelsset-quote-inventory-request-nullablets"></a>

#### 🔄 Return<a id="🔄-return"></a>

[QuoteResponse](./models/quote-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quote.deleteInventory`<a id="bellhopquotedeleteinventory"></a>

Delete Quote Inventory

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteInventoryResponse = await bellhop.quote.deleteInventory({
  quoteId: "quoteId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the inventory

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/inventory` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quote.get`<a id="bellhopquoteget"></a>

Fetch a quote by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await bellhop.quote.get({
  quoteId: "quoteId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the quote

#### 🔄 Return<a id="🔄-return"></a>

[QuoteResponse](./models/quote-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quote.getInventory`<a id="bellhopquotegetinventory"></a>

Get Quote Inventory

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getInventoryResponse = await bellhop.quote.getInventory({
  quoteId: "quoteId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the source quote

#### 🔄 Return<a id="🔄-return"></a>

[QuoteInventoryResponse](./models/quote-inventory-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/inventory` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quote.updateInventory`<a id="bellhopquoteupdateinventory"></a>

Update Quote Inventory

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateInventoryResponse = await bellhop.quote.updateInventory({
  quoteId: "quoteId_example",
  area: 1000,
  rooms: [
    {
      slug: "string_example",
      count: 1,
    },
  ],
  access_flags: {
    elevator: true,
    elevator_reserved: true,
    long_walk_to_truck: true,
    stair_flights: 1,
  },
  additional_items: [
    {
      slug: "string_example",
      count: 1,
    },
  ],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### area: `number`<a id="area-number"></a>

The area of the property in square feet.

##### rooms: [`QuoteInventoryRoom`](./models/quote-inventory-room.ts)[]<a id="rooms-quoteinventoryroommodelsquote-inventory-roomts"></a>

List of rooms in the property.

##### access_flags: [`SetQuoteInventoryRequestAccessFlags`](./models/set-quote-inventory-request-access-flags.ts)<a id="access_flags-setquoteinventoryrequestaccessflagsmodelsset-quote-inventory-request-access-flagsts"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the inventory

##### intent: [`MovingIntentNullable`](./models/moving-intent-nullable.ts)<a id="intent-movingintentnullablemodelsmoving-intent-nullablets"></a>

The estimated amount of belongings to move.

##### additional_items: [`QuoteInventoryItem`](./models/quote-inventory-item.ts)[]<a id="additional_items-quoteinventoryitemmodelsquote-inventory-itemts"></a>

List of additional bulky items in the property.

#### 🔄 Return<a id="🔄-return"></a>

[QuoteInventoryResponse](./models/quote-inventory-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/inventory` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quoteServiceGroup.changeLocations`<a id="bellhopquoteservicegroupchangelocations"></a>

Overwrite the locations on a service group

The locations included in the request are overwritten as the locations on
the service group maintaining the sequence in the request.
This action triggers a re-estimation of the service group using the new locations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const changeLocationsResponse = await bellhop.quoteServiceGroup.changeLocations(
  {
    serviceGroupId: "service_group_id_example",
    requestBody: [
      "1a99a4ff641f4040afb2f4f72fe377cc",
      "bb2078b5d93f44c0a98f268d86540450",
    ],
  }
);
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### serviceGroupId: `string`<a id="servicegroupid-string"></a>

UUID of the service group

##### requestBody: `string`[]<a id="requestbody-string"></a>

#### 🔄 Return<a id="🔄-return"></a>

[ServiceGroupResponse](./models/service-group-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/service_groups/{service_group_id}/locations` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quoteServiceGroup.create`<a id="bellhopquoteservicegroupcreate"></a>

Creates a new service group

A service group is a collection of services that are performed at the
same time and location.
The created service group will be created with the provided services,
locations, and start date time.
The workers, duration, and end date time will be estimated based on the
locations and inventory attached to the quote.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createResponse = await bellhop.quoteServiceGroup.create({
  quoteId: "quoteId_example",
  service_codes: ["LOADINGUNLOADING"],
  locations: [
    "a4cef656c2a04ca4aa6d19cee4eb9b7e",
    "b4cef656c2a04ca4aa6d19cee4eb9b7e",
  ],
  start_datetime: "2021-01-01T12:00:00",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the quote

##### service_codes: [`ServiceType`](./models/service-type.ts)[]<a id="service_codes-servicetypemodelsservice-typets"></a>

List of service codes

##### locations: `string`[]<a id="locations-string"></a>

List of location ids

##### start_datetime: `string`<a id="start_datetime-string"></a>

Start datetime of service group

#### 🔄 Return<a id="🔄-return"></a>

[ServiceGroupResponse](./models/service-group-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/service-groups` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quoteServiceGroup.createEstimate`<a id="bellhopquoteservicegroupcreateestimate"></a>

Get Service Group Estimate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createEstimateResponse = await bellhop.quoteServiceGroup.createEstimate({
  serviceGroupId: "serviceGroupId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### serviceGroupId: `string`<a id="servicegroupid-string"></a>

UUID of the service group

#### 🔄 Return<a id="🔄-return"></a>

[EstimationResponse](./models/estimation-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/service-groups/{service_group_id}/estimate` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quoteServiceGroup.createFlexible`<a id="bellhopquoteservicegroupcreateflexible"></a>

Creates an array of flexible service groups from a service group

Generate an array of flexible service groups. The services and locations
will be copied from the source service group.
One flexible service group will be created for each day and hour combination in the input.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const createFlexibleResponse = await bellhop.quoteServiceGroup.createFlexible({
  quoteId: "quoteId_example",
  serviceGroupId: "serviceGroupId_example",
  start_date: "1970-01-01",
  end_date: "1970-01-01",
  local_hours: [8, 9, 10, 11, 12],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `string`<a id="start_date-string"></a>

Date of earliest flexible service quote to generate

##### end_date: `string`<a id="end_date-string"></a>

Date of latest flexible service quote to generate

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the source quote

##### serviceGroupId: `string`<a id="servicegroupid-string"></a>

UUID of the Service Group to use as a template for the flexible service groups

##### local_hours: `number`[]<a id="local_hours-number"></a>

List of hours in local time to generate quotes for: [8, 9, 10, 11, 12]

#### 🔄 Return<a id="🔄-return"></a>

[FlexibleQuoteResponse](./models/flexible-quote-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/service-groups/{service_group_id}/flexible` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quoteServiceGroup.delete`<a id="bellhopquoteservicegroupdelete"></a>

Delete a service group by quote ID and service group ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const deleteResponse = await bellhop.quoteServiceGroup.delete({
  quoteId: "quoteId_example",
  serviceGroupId: "serviceGroupId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the quote

##### serviceGroupId: `string`<a id="servicegroupid-string"></a>

UUID of the service group to be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/service-group/{service_group_id}` `DELETE`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quoteServiceGroup.get`<a id="bellhopquoteservicegroupget"></a>

Fetch a service group by quote ID and service group ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const getResponse = await bellhop.quoteServiceGroup.get({
  quoteId: "quoteId_example",
  serviceGroupId: "serviceGroupId_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the quote

##### serviceGroupId: `string`<a id="servicegroupid-string"></a>

UUID of the service group

#### 🔄 Return<a id="🔄-return"></a>

[ServiceGroupResponse](./models/service-group-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/service-group/{service_group_id}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quoteServiceGroup.update`<a id="bellhopquoteservicegroupupdate"></a>

Replaces a service group with a flexible service group

Replaces the existing service group with the selected flexible service group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateResponse = await bellhop.quoteServiceGroup.update({
  quoteId: "quoteId_example",
  serviceGroupId: "serviceGroupId_example",
  flexible_quote_id: "flexible_quote_id_example",
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### flexible_quote_id: `string`<a id="flexible_quote_id-string"></a>

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the quote

##### serviceGroupId: `string`<a id="servicegroupid-string"></a>

UUID of the service group

#### 🔄 Return<a id="🔄-return"></a>

[ServiceGroupResponse](./models/service-group-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/service-groups/{service_group_id}` `PATCH`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `bellhop.quoteServiceGroup.updateServices`<a id="bellhopquoteservicegroupupdateservices"></a>

Update the service configuration on a service group

Update services, workers and duration on a service group.
the service_workers object is a mapping of service code and number of workers.

Only the included service codes will be retained on the service group.

Any excluded services will be removed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```typescript
const updateServicesResponse = await bellhop.quoteServiceGroup.updateServices({
  quoteId: "quoteId_example",
  serviceGroupId: "serviceGroupId_example",
  service_workers: [
    {
      service_code: "string_example",
      workers: 1,
    },
  ],
});
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### service_workers: [`ServiceWorkers`](./models/service-workers.ts)[]<a id="service_workers-serviceworkersmodelsservice-workersts"></a>

Mapping of service code and number of workers. Only the included service codes will be retained on the service group. Any excluded services will be removed.

##### quoteId: `string`<a id="quoteid-string"></a>

UUID of the quote

##### serviceGroupId: `string`<a id="servicegroupid-string"></a>

UUID of the service group

##### duration: `number`<a id="duration-number"></a>

Duration for all services in group

#### 🔄 Return<a id="🔄-return"></a>

[ServiceGroupResponse](./models/service-group-response.ts)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{quote_id}/service-groups/{service_group_id}/services` `PUT`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This TypeScript package is automatically generated by [Konfig](https://konfigthis.com)
