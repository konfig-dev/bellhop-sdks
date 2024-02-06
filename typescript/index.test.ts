import { Bellhop } from "./index";

describe("bellhop-partners-typescript", () => {
  it.skip("initialize client", async () => {
    const bellhop = new Bellhop({});
  });
  it("List Leads OAuth", async () => {
    const bellhop = new Bellhop({
      oauthClientId: process.env.BELLHOP_CLIENT_ID,
      oauthClientSecret: process.env.BELLHOP_CLIENT_SECRET,
      basePath: "https://partners.bellhops.dev/v5",
    });
    const response = await bellhop.lead.list();
    console.log(response.data);

    // second one should check expiry
    const response2 = await bellhop.lead.list();
    console.log(response2.data);
  });
});
