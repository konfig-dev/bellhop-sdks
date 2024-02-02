import { Bellhop } from "./index";

describe("bellhop-partners-typescript", () => {
  it.skip("initialize client", async () => {
    const bellhop = new Bellhop({});
  });
  it.skip("Get Auth token", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const token = await bellhop.authorization.getAuthToken({
      client_id: "CLIENT_ID",
      client_secret: "CLIENT_SECRET",
      audience: "Dev",
    });
    console.log(token.data);
  });
  it.skip("Cancel Lead", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const lead = await bellhop.leads.cancel({
      code: "CODE",
    });
    console.log(lead.data);
  });
  it.skip("Create Lead", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const lead = await bellhop.leads.create({
      first_name: "John",
      last_name: "Doe",
      lead_type: "Zillow",
      lead_record_type: "Potential Customer",
    });
    console.log(lead.data);
  });
  it.skip("List Leads", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const leads = await bellhop.leads.list();
    console.log(leads.data);
  });
  it("List Leads OAuth", async () => {
    const bellhop = new Bellhop({
      clientId: process.env.BELLHOP_CLIENT_ID,
      clientSecret: process.env.BELLHOP_CLIENT_SECRET,
      basePath: "https://partners.bellhops.dev/v5",
    });
    const response = await bellhop.leads.list();
    console.log(response.data);

    // second one should check expiry
    const response2 = await bellhop.leads.list();
    console.log(response2.data);
  });
  it.skip("Leads Update", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const lead = await bellhop.leads.update({
      code: "CODE",
      description: "DESCRIPTION",
    });
    console.log(lead.data);
  });
  it.skip("Creating Quoting Locaoion Object", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const createQuotingResponse = await bellhop.locations.createQuoting({
      line_1: "line_1_example",
      city: "city_example",
      state: "state_example",
      postal_code: "postal_code_example",
      country: "US",
      property_type: "APARTMENT",
    });
    console.log(createQuotingResponse.data);
  });
  it.skip("Create an order from quote", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const createResponse = await bellhop.orders.create({
      quoteId: "quoteId_example",
    });
    console.log(createResponse.data);
  });
  it.skip("Get Postal Codes Serviceability", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const getServiceabilityResponse =
      await bellhop.postalCodes.getServiceability({
        originPostalCode: "originPostalCode_example",
      });
    console.log(getServiceabilityResponse.data);
  });
  it.skip("Overwrite locations on service group", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const changeLocationsResponse =
      await bellhop.quoteServiceGroups.changeLocations({
        serviceGroupId: "service_group_id_example",
        requestBody: [
          "a627084cd72247bf9217363f8772aa5f",
          "12fb179d05294c3e8f433c315966a515",
        ],
      });
    console.log(changeLocationsResponse.data);
  });
  it.skip("Create New Service Group", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });

    const serviceGroup = await bellhop.quoteServiceGroups.create({
      quoteId: "QUOTE_ID",
      service_codes: ["LOADING"],
      locations: ["LOCATION_ID"],
      start_datetime: new Date().toISOString(),
    });

    console.log(serviceGroup.data);
  });
  it.skip("Create flexible service groups", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const createFlexibleResponse =
      await bellhop.quoteServiceGroups.createFlexible({
        quoteId: "quoteId_example",
        serviceGroupId: "serviceGroupId_example",
        start_date: "1970-01-01",
        end_date: "1970-01-01",
        local_hours: [8, 9, 10, 11, 12],
      });
    console.log(createFlexibleResponse.data);
  });
  it.skip("Delete service group by id", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const deleteResponse = await bellhop.quoteServiceGroups.delete({
      quoteId: "quoteId_example",
      serviceGroupId: "serviceGroupId_example",
    });
    console.log(deleteResponse.data);
  });
  it.skip("Fetch service group by quote ID and service group ID", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const deleteResponse = await bellhop.quoteServiceGroups.delete({
      quoteId: "quoteId_example",
      serviceGroupId: "serviceGroupId_example",
    });
    console.log(deleteResponse.data);
  });
  it.skip("Replace service group with flexible service group", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const replaceResponse = await bellhop.quoteServiceGroups.replace({
      quoteId: "quoteId_example",
      serviceGroupId: "serviceGroupId_example",
      flexible_quote_id: "flexible_quote_id_example",
    });
    console.log(replaceResponse.data);
  });
  it.skip("Update service configuration on a service group", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const updateResponse = await bellhop.quoteServiceGroups.update({
      quoteId: "quoteId_example",
      serviceGroupId: "serviceGroupId_example",
      service_workers: [
        {
          service_code: "CARSHIPPING",
          workers: 1,
        },
      ],
    });
    console.log(updateResponse.data);
  });
  it.skip("Create a quote for a given customer", async () => {
    const bellhop = new Bellhop({
      accessToken: "ACCESS_TOKEN",
      basePath: "http://127.0.0.1:4010",
    });
    const createResponse = await bellhop.quotes.create({
      customer: {
        first_name: "first_name_example",
        last_name: "last_name_example",
        phone: "phone_example",
        email: "test@test.com",
      },
      start_datetime: new Date().toISOString(),
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
    console.log(createResponse.data);
  });
});
