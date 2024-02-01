/*
partner-api

Bellhop's Partner API

The version of the OpenAPI document: 5
Contact: engineering@bellhop.com

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"

import { AccessFlagsResponseNullable } from './access-flags-response-nullable';
import { ExtraDataResponseNullable } from './extra-data-response-nullable';
import { InventoryItem } from './inventory-item';

/**
 * Quote Inventory object
 * @export
 * @interface InventoryResponseNullable
 */
export interface InventoryResponseNullable {
    /**
     * 
     * @type {boolean}
     * @memberof InventoryResponseNullable
     */
    'is_room_based_inventory': boolean;
    /**
     * 
     * @type {string}
     * @memberof InventoryResponseNullable
     */
    'intent'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof InventoryResponseNullable
     */
    'area'?: number | null;
    /**
     * 
     * @type {AccessFlagsResponseNullable}
     * @memberof InventoryResponseNullable
     */
    'access_flags'?: AccessFlagsResponseNullable | null;
    /**
     * 
     * @type {ExtraDataResponseNullable}
     * @memberof InventoryResponseNullable
     */
    'extra_data'?: ExtraDataResponseNullable | null;
    /**
     * 
     * @type {Array<InventoryItem>}
     * @memberof InventoryResponseNullable
     */
    'additional_items'?: Array<InventoryItem> | null;
    /**
     * 
     * @type {Array<InventoryItem>}
     * @memberof InventoryResponseNullable
     */
    'rooms'?: Array<InventoryItem> | null;
    /**
     * 
     * @type {string}
     * @memberof InventoryResponseNullable
     */
    'notes'?: string | null;
}

