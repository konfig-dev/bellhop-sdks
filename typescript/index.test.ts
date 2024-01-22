import { Bellhop } from "./index";

describe("bellhop-partners-typescript", () => {
  it("initialize client", async () => {
    const bellhop = new Bellhop({});
  });
  it("Create Lead", async () => {
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
  it("Get Auth token", async () => {
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
  it("Create New Service Group", async () => {
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
});
