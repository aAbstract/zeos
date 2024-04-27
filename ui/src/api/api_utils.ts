import { Result } from '../lib/defines';

export async function make_fetch_request(url: string, options?: RequestInit): Promise<Result> {
    // const accessToken = cxStore_getItem('accessToken') ?? '';
    // const request_headers = axios_request_config.headers ?? {};
    // axios_request_config.headers = { ...request_headers, Authorization: `Bearer ${accessToken}` };
    try {
        const fetch_response = await fetch(url, options);
        const resp_json_body = await fetch_response.json();
        if (fetch_response.status !== 200)
            return { error: resp_json_body.detail };
        else
            return { success: resp_json_body };
    } catch (e) {
        const err_obj = e as any;
        return { error: `[ERROR] [${err_obj.code}]: ${err_obj.message}` };
    }
}