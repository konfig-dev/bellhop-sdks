import { RequestArgs } from "./base";
import { Configuration } from "./configuration";
import { jwtDecode } from "jwt-decode";
import axios from "axios";

export async function requestAfterHook({
  configuration,
  axiosArgs,
}: {
  axiosArgs: RequestArgs;
  basePath: string;
  url: string;
  configuration?: Configuration;
}): Promise<void> {
  const authenticate = async () => {
    if (
      configuration?.clientId !== undefined &&
      configuration?.clientSecret !== undefined &&
      configuration?.accessToken === undefined
    ) {
      // remove subpath from base path
      // e.g. https://partners.bellhops.dev/v5 -> https://partners.bellhops.dev
      const audience = configuration.basePath.split("/").slice(0, 3).join("/");

      const tokenResponse = await axios.post(
        `${configuration.basePath}/authorize?use_cache=true`,
        {
          client_id: configuration.clientId,
          client_secret: configuration.clientSecret,
          audience,
        }
      );
      const token = tokenResponse.data.token;
      configuration.accessToken = token;
      axiosArgs.options.headers = {
        ...axiosArgs.options.headers,
        Authorization: `Bearer ${token}`,
      };
    }
  };
  if (configuration?.accessToken === undefined) {
    await authenticate();
  } else if (
    configuration?.accessToken !== undefined &&
    typeof configuration.accessToken === "string"
  ) {
    // check if access token is expired
    const token = configuration.accessToken;
    const decodedToken = jwtDecode(token);
    const currentTime = Date.now() / 1000;
    if ((decodedToken as any)["exp"] < currentTime) {
      await authenticate();
    }
  }
}
