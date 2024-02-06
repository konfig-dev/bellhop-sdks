/* tslint:disable */
/* eslint-disable */
/*
partner-api

Bellhop's Partner API

The version of the OpenAPI document: 5
Contact: engineering@bellhop.com

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/

import globalAxios, { AxiosPromise, AxiosInstance, AxiosRequestConfig } from 'axios';
import { Configuration } from '../configuration';
// Some imports not used depending on template conditions
// @ts-ignore
import { DUMMY_BASE_URL, assertParamExists, setApiKeyToObject, setBasicAuthToObject, setBearerAuthToObject, setSearchParams, serializeDataIfNeeded, toPathString, createRequestFunction, isBrowser } from '../common';
import { setOAuthToObject } from '../common';
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, RequestArgs, BaseAPI, RequiredError } from '../base';
// @ts-ignore
import { HTTPValidationError } from '../models';
// @ts-ignore
import { OrderResponseV2 } from '../models';
import { paginate } from "../pagination/paginate";
import type * as buffer from "buffer"
import { requestBeforeHook } from '../requestBeforeHook';
/**
 * OrderApi - axios parameter creator
 * @export
 */
export const OrderApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * Creates an order from a quote
         * @summary Create Order
         * @param {string} quoteId Quote ID to generate order from
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        create: async (quoteId: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'quoteId' is not null or undefined
            assertParamExists('create', 'quoteId', quoteId)
            const localVarPath = `/orders/{quote_id}`
                .replace(`{${"quote_id"}}`, encodeURIComponent(String(quoteId !== undefined ? quoteId : `-quote_id-`)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2ClientCredentialsBearer required
            // oauth required
            await setOAuthToObject(localVarHeaderParameter, "OAuth2ClientCredentialsBearer", ["orders:create"], configuration)

    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * OrderApi - functional programming interface
 * @export
 */
export const OrderApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = OrderApiAxiosParamCreator(configuration)
    return {
        /**
         * Creates an order from a quote
         * @summary Create Order
         * @param {OrderApiCreateRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async create(requestParameters: OrderApiCreateRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<OrderResponseV2>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.create(requestParameters.quoteId, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * OrderApi - factory interface
 * @export
 */
export const OrderApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = OrderApiFp(configuration)
    return {
        /**
         * Creates an order from a quote
         * @summary Create Order
         * @param {OrderApiCreateRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        create(requestParameters: OrderApiCreateRequest, options?: AxiosRequestConfig): AxiosPromise<OrderResponseV2> {
            return localVarFp.create(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for create operation in OrderApi.
 * @export
 * @interface OrderApiCreateRequest
 */
export type OrderApiCreateRequest = {
    
    /**
    * Quote ID to generate order from
    * @type {string}
    * @memberof OrderApiCreate
    */
    readonly quoteId: string
    
}

/**
 * OrderApiGenerated - object-oriented interface
 * @export
 * @class OrderApiGenerated
 * @extends {BaseAPI}
 */
export class OrderApiGenerated extends BaseAPI {
    /**
     * Creates an order from a quote
     * @summary Create Order
     * @param {OrderApiCreateRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof OrderApiGenerated
     */
    public create(requestParameters: OrderApiCreateRequest, options?: AxiosRequestConfig) {
        return OrderApiFp(this.configuration).create(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}