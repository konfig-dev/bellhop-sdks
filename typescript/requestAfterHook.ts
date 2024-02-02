import { RequestArgs } from "./base";
import { Bellhop } from "./client";
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
      const tokenResponse = await axios.post(
        `${configuration.basePath}/authorize`,
        {
          grant_type: "client_credentials",
          client_id: configuration.clientId,
          client_secret: configuration.clientSecret,
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
    if ((decodedToken as any)["expiry"] < currentTime) {
      await authenticate();
    }
  }
}
