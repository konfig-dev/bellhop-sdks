/*
partner-api

Bellhop's Partner API

The version of the OpenAPI document: 5
Contact: engineering@bellhop.com

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"


/**
 * 
 * @export
 * @interface BodyGetAuthTokenAuthorizePost
 */
export interface BodyGetAuthTokenAuthorizePost {
    /**
     * 
     * @type {string}
     * @memberof BodyGetAuthTokenAuthorizePost
     */
    'grant_type'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof BodyGetAuthTokenAuthorizePost
     */
    'scope'?: string;
    /**
     * 
     * @type {string}
     * @memberof BodyGetAuthTokenAuthorizePost
     */
    'client_id'?: string;
    /**
     * 
     * @type {string}
     * @memberof BodyGetAuthTokenAuthorizePost
     */
    'client_secret'?: string;
}

