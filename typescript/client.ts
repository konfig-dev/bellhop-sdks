/*
partner-api

Bellhop's Partner API

The version of the OpenAPI document: 5
Contact: engineering@bellhop.com

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/

import { AxiosRequestConfig } from "axios";
import {
  LeadApi,
  LocationApi,
  OrderApi,
  PostalCodeApi,
  QuoteApi,
  QuoteServiceGroupApi,
} from "./api";
import { Configuration, ConfigurationParameters } from "./configuration";
import { BellhopCustom } from "./client-custom";

export class Bellhop extends BellhopCustom {
  readonly lead: LeadApi;
  readonly location: LocationApi;
  readonly order: OrderApi;
  readonly postalCode: PostalCodeApi;
  readonly quote: QuoteApi;
  readonly quoteServiceGroup: QuoteServiceGroupApi;

  constructor(configurationParameters: ConfigurationParameters) {
    super(configurationParameters);
    const configuration = new Configuration(configurationParameters);
    this.lead = new LeadApi(configuration);
    this.location = new LocationApi(configuration);
    this.order = new OrderApi(configuration);
    this.postalCode = new PostalCodeApi(configuration);
    this.quote = new QuoteApi(configuration);
    this.quoteServiceGroup = new QuoteServiceGroupApi(configuration);
  }

}
