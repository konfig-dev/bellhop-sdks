/*
partner-api

Bellhop's Partner API

The version of the OpenAPI document: 5
Contact: engineering@bellhop.com

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"


/**
 * Response for computed quote totals (populated by Quote.totals property)
 * @export
 * @interface Totals
 */
export interface Totals {
    /**
     * 
     * @type {number}
     * @memberof Totals
     */
    'service_total': number;
    /**
     * 
     * @type {number}
     * @memberof Totals
     */
    'product_total': number;
    /**
     * 
     * @type {number}
     * @memberof Totals
     */
    'fee_total': number;
    /**
     * 
     * @type {number}
     * @memberof Totals
     */
    'subtotal': number;
    /**
     * 
     * @type {number}
     * @memberof Totals
     */
    'discount_total': number;
    /**
     * 
     * @type {number}
     * @memberof Totals
     */
    'total': number;
    /**
     * 
     * @type {number}
     * @memberof Totals
     */
    'deposit_amount': number;
}

