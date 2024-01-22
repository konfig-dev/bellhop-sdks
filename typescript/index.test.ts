import { Bellhop } from "./index";

describe("bellhop-typescript-sdk", () => {
    it("initialize client", async () => {
        const bellhop = new Bellhop({
            apiKey: "API_KEY",
        });
    });
});
