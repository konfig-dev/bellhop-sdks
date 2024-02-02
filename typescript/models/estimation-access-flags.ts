/*
partner-api

Bellhop's Partner API

The version of the OpenAPI document: 5
Contact: engineering@bellhop.com

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"


/**
 * TODO
 * @export
 * @interface EstimationAccessFlags
 */
export interface EstimationAccessFlags {
    /**
     * 
     * @type {boolean}
     * @memberof EstimationAccessFlags
     */
    'elevator': boolean;
    /**
     * 
     * @type {boolean}
     * @memberof EstimationAccessFlags
     */
    'elevator_reserved': boolean;
    /**
     * 
     * @type {boolean}
     * @memberof EstimationAccessFlags
     */
    'long_walk_to_truck': boolean;
    /**
     * 
     * @type {number}
     * @memberof EstimationAccessFlags
     */
    'stair_flights': number;
}
