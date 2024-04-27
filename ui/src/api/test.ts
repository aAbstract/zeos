import { make_fetch_request } from "./api_utils";
import { ZEOS_IP, ZEOS_HTTP_PORT } from "../lib/defines";
import { Result } from "../lib/defines";

export async function test_zeos_backend(): Promise<Result> {
    return await make_fetch_request(
        `http://${ZEOS_IP}:${ZEOS_HTTP_PORT}/test`,
    );
}