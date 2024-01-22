/* tslint:disable */
/* eslint-disable */
/*
partner-api

Bellhop's Partner API

The version of the OpenAPI document: 5.0.0
Contact: engineering@bellhop.com

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/

import globalAxios, { AxiosPromise, AxiosInstance, AxiosRequestConfig } from 'axios';
import { Configuration } from '../configuration';
// Some imports not used depending on template conditions
// @ts-ignore
import { DUMMY_BASE_URL, assertParamExists, setApiKeyToObject, setBasicAuthToObject, setBearerAuthToObject, setSearchParams, serializeDataIfNeeded, toPathString, createRequestFunction, isBrowser } from '../common';
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, RequestArgs, BaseAPI, RequiredError } from '../base';
// @ts-ignore
import { CreateQuoteRequest } from '../models';
// @ts-ignore
import { CreateQuoteRequestCustomer } from '../models';
// @ts-ignore
import { HTTPValidationError } from '../models';
// @ts-ignore
import { LocationRequest } from '../models';
// @ts-ignore
import { QuoteResponse } from '../models';
import { paginate } from "../pagination/paginate";
import type * as buffer from "buffer"
import { requestBeforeHook } from '../requestBeforeHook';
/**
 * QuotesApi - axios parameter creator
 * @export
 */
export const QuotesApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * Creates a quote  Creates a quote for a given customer using the provided locations and service code. The LOCALFULLSERVICE service code will generate a service group with LOADINGUNLOADING and TRANSIT services. All other service codes generate service groups with a single service.
         * @summary Create Quote
         * @param {CreateQuoteRequest} createQuoteRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        create: async (createQuoteRequest: CreateQuoteRequest, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'createQuoteRequest' is not null or undefined
            assertParamExists('create', 'createQuoteRequest', createQuoteRequest)
            const localVarPath = `/quotes`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication Auth0HTTPBearer required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

    
            localVarHeaderParameter['Content-Type'] = 'application/json';


            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                requestBody: createQuoteRequest,
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });
            localVarRequestOptions.data = serializeDataIfNeeded(createQuoteRequest, localVarRequestOptions, configuration)

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * QuotesApi - functional programming interface
 * @export
 */
export const QuotesApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = QuotesApiAxiosParamCreator(configuration)
    return {
        /**
         * Creates a quote  Creates a quote for a given customer using the provided locations and service code. The LOCALFULLSERVICE service code will generate a service group with LOADINGUNLOADING and TRANSIT services. All other service codes generate service groups with a single service.
         * @summary Create Quote
         * @param {QuotesApiCreateRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async create(requestParameters: QuotesApiCreateRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<QuoteResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.create(requestParameters, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * QuotesApi - factory interface
 * @export
 */
export const QuotesApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = QuotesApiFp(configuration)
    return {
        /**
         * Creates a quote  Creates a quote for a given customer using the provided locations and service code. The LOCALFULLSERVICE service code will generate a service group with LOADINGUNLOADING and TRANSIT services. All other service codes generate service groups with a single service.
         * @summary Create Quote
         * @param {QuotesApiCreateRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        create(requestParameters: QuotesApiCreateRequest, options?: AxiosRequestConfig): AxiosPromise<QuoteResponse> {
            return localVarFp.create(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for create operation in QuotesApi.
 * @export
 * @interface QuotesApiCreateRequest
 */
export type QuotesApiCreateRequest = {
    
} & CreateQuoteRequest

/**
 * QuotesApiGenerated - object-oriented interface
 * @export
 * @class QuotesApiGenerated
 * @extends {BaseAPI}
 */
export class QuotesApiGenerated extends BaseAPI {
    /**
     * Creates a quote  Creates a quote for a given customer using the provided locations and service code. The LOCALFULLSERVICE service code will generate a service group with LOADINGUNLOADING and TRANSIT services. All other service codes generate service groups with a single service.
     * @summary Create Quote
     * @param {QuotesApiCreateRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof QuotesApiGenerated
     */
    public create(requestParameters: QuotesApiCreateRequest, options?: AxiosRequestConfig) {
        return QuotesApiFp(this.configuration).create(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}
