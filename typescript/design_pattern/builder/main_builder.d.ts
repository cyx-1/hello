/**
 * Builder Design Pattern - HTTP Request Builder Example
 *
 * The Builder pattern separates the construction of a complex object from its
 * representation, allowing the same construction process to create different
 * representations.
 */
interface HttpHeader {
    name: string;
    value: string;
}
interface QueryParam {
    key: string;
    value: string;
}
declare class HttpRequest {
    method: string;
    url: string;
    headers: HttpHeader[];
    queryParams: QueryParam[];
    body: string | null;
    timeout: number;
    retries: number;
    authentication: {
        type: string;
        credentials: string;
    } | null;
    describe(): string;
    getFullDetails(): string[];
}
interface HttpRequestBuilder {
    reset(): HttpRequestBuilder;
    setUrl(url: string): HttpRequestBuilder;
    addHeader(name: string, value: string): HttpRequestBuilder;
    addQueryParam(key: string, value: string): HttpRequestBuilder;
    setBody(body: string): HttpRequestBuilder;
    setTimeout(timeout: number): HttpRequestBuilder;
    setRetries(retries: number): HttpRequestBuilder;
    setAuthentication(type: string, credentials: string): HttpRequestBuilder;
    build(): HttpRequest;
}
declare class GetRequestBuilder implements HttpRequestBuilder {
    private request;
    constructor();
    reset(): HttpRequestBuilder;
    setUrl(url: string): HttpRequestBuilder;
    addHeader(name: string, value: string): HttpRequestBuilder;
    addQueryParam(key: string, value: string): HttpRequestBuilder;
    setBody(body: string): HttpRequestBuilder;
    setTimeout(timeout: number): HttpRequestBuilder;
    setRetries(retries: number): HttpRequestBuilder;
    setAuthentication(type: string, credentials: string): HttpRequestBuilder;
    build(): HttpRequest;
}
declare class PostRequestBuilder implements HttpRequestBuilder {
    private request;
    constructor();
    reset(): HttpRequestBuilder;
    setUrl(url: string): HttpRequestBuilder;
    addHeader(name: string, value: string): HttpRequestBuilder;
    addQueryParam(key: string, value: string): HttpRequestBuilder;
    setBody(body: string): HttpRequestBuilder;
    setTimeout(timeout: number): HttpRequestBuilder;
    setRetries(retries: number): HttpRequestBuilder;
    setAuthentication(type: string, credentials: string): HttpRequestBuilder;
    build(): HttpRequest;
}
declare class PutRequestBuilder implements HttpRequestBuilder {
    private request;
    constructor();
    reset(): HttpRequestBuilder;
    setUrl(url: string): HttpRequestBuilder;
    addHeader(name: string, value: string): HttpRequestBuilder;
    addQueryParam(key: string, value: string): HttpRequestBuilder;
    setBody(body: string): HttpRequestBuilder;
    setTimeout(timeout: number): HttpRequestBuilder;
    setRetries(retries: number): HttpRequestBuilder;
    setAuthentication(type: string, credentials: string): HttpRequestBuilder;
    build(): HttpRequest;
}
declare class ApiRequestDirector {
    private builder;
    constructor(builder: HttpRequestBuilder);
    setBuilder(builder: HttpRequestBuilder): void;
    buildHealthCheck(baseUrl: string): HttpRequest;
    buildAuthenticatedRequest(url: string, token: string): HttpRequest;
    buildPaginatedListRequest(baseUrl: string, resource: string, page: number, limit: number): HttpRequest;
    buildCreateResourceRequest(baseUrl: string, resource: string, data: object, token: string): HttpRequest;
    buildUpdateResourceRequest(baseUrl: string, resource: string, id: string, data: object, token: string): HttpRequest;
}
declare function main(): void;
//# sourceMappingURL=main_builder.d.ts.map