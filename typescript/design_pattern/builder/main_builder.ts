/**
 * Builder Design Pattern - HTTP Request Builder Example
 *
 * The Builder pattern separates the construction of a complex object from its
 * representation, allowing the same construction process to create different
 * representations.
 */

// =============================================================================
// Product: The complex object being built
// =============================================================================

interface HttpHeader {
  name: string;
  value: string;
}

interface QueryParam {
  key: string;
  value: string;
}

class HttpRequest {
  public method: string = 'GET';
  public url: string = '';
  public headers: HttpHeader[] = [];
  public queryParams: QueryParam[] = [];
  public body: string | null = null;
  public timeout: number = 30000;
  public retries: number = 0;
  public authentication: { type: string; credentials: string } | null = null;

  public describe(): string {
    let description = `${this.method} ${this.url}`;

    if (this.queryParams.length > 0) {
      const params = this.queryParams.map(p => `${p.key}=${p.value}`).join('&');
      description += `?${params}`;
    }

    return description;
  }

  public getFullDetails(): string[] {
    const details: string[] = [];
    details.push(`Method: ${this.method}`);
    details.push(`URL: ${this.url}`);

    if (this.queryParams.length > 0) {
      details.push(`Query Params: ${this.queryParams.map(p => `${p.key}=${p.value}`).join(', ')}`);
    }

    if (this.headers.length > 0) {
      details.push(`Headers: ${this.headers.map(h => `${h.name}: ${h.value}`).join(', ')}`);
    }

    if (this.body) {
      details.push(`Body: ${this.body}`);
    }

    if (this.authentication) {
      details.push(`Auth: ${this.authentication.type}`);
    }

    details.push(`Timeout: ${this.timeout}ms`);
    details.push(`Retries: ${this.retries}`);

    return details;
  }
}

// =============================================================================
// Builder Interface: Declares the building steps
// =============================================================================

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

// =============================================================================
// Concrete Builder: GET Request Builder
// =============================================================================

class GetRequestBuilder implements HttpRequestBuilder {
  private request: HttpRequest;

  constructor() {
    this.request = new HttpRequest();
    this.request.method = 'GET';
  }

  public reset(): HttpRequestBuilder {
    this.request = new HttpRequest();
    this.request.method = 'GET';
    return this;
  }

  public setUrl(url: string): HttpRequestBuilder {
    this.request.url = url;
    return this;
  }

  public addHeader(name: string, value: string): HttpRequestBuilder {
    this.request.headers.push({ name, value });
    return this;
  }

  public addQueryParam(key: string, value: string): HttpRequestBuilder {
    this.request.queryParams.push({ key, value });
    return this;
  }

  public setBody(body: string): HttpRequestBuilder {
    // GET requests typically don't have a body, but we allow it for flexibility
    console.log('[Line 106] Warning: GET requests typically should not have a body');
    this.request.body = body;
    return this;
  }

  public setTimeout(timeout: number): HttpRequestBuilder {
    this.request.timeout = timeout;
    return this;
  }

  public setRetries(retries: number): HttpRequestBuilder {
    this.request.retries = retries;
    return this;
  }

  public setAuthentication(type: string, credentials: string): HttpRequestBuilder {
    this.request.authentication = { type, credentials };
    return this;
  }

  public build(): HttpRequest {
    const result = this.request;
    this.reset();
    return result;
  }
}

// =============================================================================
// Concrete Builder: POST Request Builder
// =============================================================================

class PostRequestBuilder implements HttpRequestBuilder {
  private request: HttpRequest;

  constructor() {
    this.request = new HttpRequest();
    this.request.method = 'POST';
    // POST requests commonly use JSON content type
    this.request.headers.push({ name: 'Content-Type', value: 'application/json' });
  }

  public reset(): HttpRequestBuilder {
    this.request = new HttpRequest();
    this.request.method = 'POST';
    this.request.headers.push({ name: 'Content-Type', value: 'application/json' });
    return this;
  }

  public setUrl(url: string): HttpRequestBuilder {
    this.request.url = url;
    return this;
  }

  public addHeader(name: string, value: string): HttpRequestBuilder {
    this.request.headers.push({ name, value });
    return this;
  }

  public addQueryParam(key: string, value: string): HttpRequestBuilder {
    this.request.queryParams.push({ key, value });
    return this;
  }

  public setBody(body: string): HttpRequestBuilder {
    this.request.body = body;
    return this;
  }

  public setTimeout(timeout: number): HttpRequestBuilder {
    this.request.timeout = timeout;
    return this;
  }

  public setRetries(retries: number): HttpRequestBuilder {
    this.request.retries = retries;
    return this;
  }

  public setAuthentication(type: string, credentials: string): HttpRequestBuilder {
    this.request.authentication = { type, credentials };
    return this;
  }

  public build(): HttpRequest {
    const result = this.request;
    this.reset();
    return result;
  }
}

// =============================================================================
// Concrete Builder: PUT Request Builder
// =============================================================================

class PutRequestBuilder implements HttpRequestBuilder {
  private request: HttpRequest;

  constructor() {
    this.request = new HttpRequest();
    this.request.method = 'PUT';
    this.request.headers.push({ name: 'Content-Type', value: 'application/json' });
  }

  public reset(): HttpRequestBuilder {
    this.request = new HttpRequest();
    this.request.method = 'PUT';
    this.request.headers.push({ name: 'Content-Type', value: 'application/json' });
    return this;
  }

  public setUrl(url: string): HttpRequestBuilder {
    this.request.url = url;
    return this;
  }

  public addHeader(name: string, value: string): HttpRequestBuilder {
    this.request.headers.push({ name, value });
    return this;
  }

  public addQueryParam(key: string, value: string): HttpRequestBuilder {
    this.request.queryParams.push({ key, value });
    return this;
  }

  public setBody(body: string): HttpRequestBuilder {
    this.request.body = body;
    return this;
  }

  public setTimeout(timeout: number): HttpRequestBuilder {
    this.request.timeout = timeout;
    return this;
  }

  public setRetries(retries: number): HttpRequestBuilder {
    this.request.retries = retries;
    return this;
  }

  public setAuthentication(type: string, credentials: string): HttpRequestBuilder {
    this.request.authentication = { type, credentials };
    return this;
  }

  public build(): HttpRequest {
    const result = this.request;
    this.reset();
    return result;
  }
}

// =============================================================================
// Director: Orchestrates the building process with predefined configurations
// =============================================================================

class ApiRequestDirector {
  private builder: HttpRequestBuilder;

  constructor(builder: HttpRequestBuilder) {
    this.builder = builder;
  }

  public setBuilder(builder: HttpRequestBuilder): void {
    this.builder = builder;
  }

  // Build a simple API health check request
  public buildHealthCheck(baseUrl: string): HttpRequest {
    return this.builder
      .reset()
      .setUrl(`${baseUrl}/health`)
      .setTimeout(5000)
      .setRetries(3)
      .build();
  }

  // Build an authenticated API request with standard headers
  public buildAuthenticatedRequest(url: string, token: string): HttpRequest {
    return this.builder
      .reset()
      .setUrl(url)
      .addHeader('Accept', 'application/json')
      .addHeader('X-Request-ID', crypto.randomUUID())
      .setAuthentication('Bearer', token)
      .setTimeout(10000)
      .setRetries(2)
      .build();
  }

  // Build a paginated list request
  public buildPaginatedListRequest(
    baseUrl: string,
    resource: string,
    page: number,
    limit: number
  ): HttpRequest {
    return this.builder
      .reset()
      .setUrl(`${baseUrl}/${resource}`)
      .addQueryParam('page', page.toString())
      .addQueryParam('limit', limit.toString())
      .addHeader('Accept', 'application/json')
      .setTimeout(15000)
      .build();
  }

  // Build a create resource request (for POST builder)
  public buildCreateResourceRequest(
    baseUrl: string,
    resource: string,
    data: object,
    token: string
  ): HttpRequest {
    return this.builder
      .reset()
      .setUrl(`${baseUrl}/${resource}`)
      .setBody(JSON.stringify(data))
      .setAuthentication('Bearer', token)
      .addHeader('X-Request-ID', crypto.randomUUID())
      .setTimeout(20000)
      .setRetries(1)
      .build();
  }

  // Build an update resource request (for PUT builder)
  public buildUpdateResourceRequest(
    baseUrl: string,
    resource: string,
    id: string,
    data: object,
    token: string
  ): HttpRequest {
    return this.builder
      .reset()
      .setUrl(`${baseUrl}/${resource}/${id}`)
      .setBody(JSON.stringify(data))
      .setAuthentication('Bearer', token)
      .setTimeout(20000)
      .setRetries(1)
      .build();
  }
}

// =============================================================================
// Main: Demonstration of the Builder Pattern
// =============================================================================

function main(): void {
  console.log('='.repeat(70));
  console.log('[Line 301] Builder Design Pattern - HTTP Request Builder Demo');
  console.log('='.repeat(70));
  console.log();

  // -------------------------------------------------------------------------
  // Example 1: Using Director with GET Request Builder
  // -------------------------------------------------------------------------
  console.log('[Line 308] Example 1: Director with GET Request Builder');
  console.log('-'.repeat(70));

  const getBuilder = new GetRequestBuilder();
  const director = new ApiRequestDirector(getBuilder);

  // Build a health check request
  console.log('[Line 315] Building health check request...');
  const healthCheck = director.buildHealthCheck('https://api.example.com');
  console.log(`[Line 317] Health Check: ${healthCheck.describe()}`);
  healthCheck.getFullDetails().forEach(detail => console.log(`  ${detail}`));
  console.log();

  // Build a paginated list request
  console.log('[Line 322] Building paginated users list request...');
  const usersList = director.buildPaginatedListRequest(
    'https://api.example.com',
    'users',
    1,
    25
  );
  console.log(`[Line 329] Users List: ${usersList.describe()}`);
  usersList.getFullDetails().forEach(detail => console.log(`  ${detail}`));
  console.log();

  // -------------------------------------------------------------------------
  // Example 2: Using Director with POST Request Builder
  // -------------------------------------------------------------------------
  console.log('[Line 336] Example 2: Director with POST Request Builder');
  console.log('-'.repeat(70));

  const postBuilder = new PostRequestBuilder();
  director.setBuilder(postBuilder);

  // Build a create user request
  console.log('[Line 343] Building create user request...');
  const createUser = director.buildCreateResourceRequest(
    'https://api.example.com',
    'users',
    { name: 'John Doe', email: 'john@example.com', role: 'admin' },
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
  );
  console.log(`[Line 350] Create User: ${createUser.describe()}`);
  createUser.getFullDetails().forEach(detail => console.log(`  ${detail}`));
  console.log();

  // -------------------------------------------------------------------------
  // Example 3: Using Director with PUT Request Builder
  // -------------------------------------------------------------------------
  console.log('[Line 357] Example 3: Director with PUT Request Builder');
  console.log('-'.repeat(70));

  const putBuilder = new PutRequestBuilder();
  director.setBuilder(putBuilder);

  // Build an update user request
  console.log('[Line 364] Building update user request...');
  const updateUser = director.buildUpdateResourceRequest(
    'https://api.example.com',
    'users',
    '12345',
    { name: 'Jane Doe', email: 'jane@example.com' },
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
  );
  console.log(`[Line 372] Update User: ${updateUser.describe()}`);
  updateUser.getFullDetails().forEach(detail => console.log(`  ${detail}`));
  console.log();

  // -------------------------------------------------------------------------
  // Example 4: Manual Builder Usage (Fluent Interface)
  // -------------------------------------------------------------------------
  console.log('[Line 379] Example 4: Manual Builder Usage (Fluent Interface)');
  console.log('-'.repeat(70));

  console.log('[Line 382] Building custom search request manually...');
  const customRequest = new GetRequestBuilder()
    .setUrl('https://api.example.com/search')
    .addQueryParam('q', 'typescript builder pattern')
    .addQueryParam('sort', 'relevance')
    .addQueryParam('limit', '50')
    .addHeader('Accept', 'application/json')
    .addHeader('Accept-Language', 'en-US')
    .addHeader('Cache-Control', 'no-cache')
    .setAuthentication('API-Key', 'sk-1234567890abcdef')
    .setTimeout(30000)
    .setRetries(3)
    .build();

  console.log(`[Line 396] Custom Search: ${customRequest.describe()}`);
  customRequest.getFullDetails().forEach(detail => console.log(`  ${detail}`));
  console.log();

  // -------------------------------------------------------------------------
  // Example 5: Building Multiple Requests with Same Builder
  // -------------------------------------------------------------------------
  console.log('[Line 403] Example 5: Building Multiple Requests with Same Builder');
  console.log('-'.repeat(70));

  const reusableBuilder = new PostRequestBuilder();

  console.log('[Line 408] Building first notification request...');
  const notification1 = reusableBuilder
    .setUrl('https://api.example.com/notifications')
    .setBody(JSON.stringify({
      userId: 'user-001',
      message: 'Welcome to the platform!',
      type: 'welcome'
    }))
    .setTimeout(5000)
    .build();
  console.log(`[Line 418] Notification 1: ${notification1.describe()}`);
  console.log(`  Body: ${notification1.body}`);
  console.log();

  console.log('[Line 422] Building second notification request...');
  const notification2 = reusableBuilder
    .setUrl('https://api.example.com/notifications')
    .setBody(JSON.stringify({
      userId: 'user-002',
      message: 'Your order has shipped!',
      type: 'shipping'
    }))
    .setTimeout(5000)
    .build();
  console.log(`[Line 432] Notification 2: ${notification2.describe()}`);
  console.log(`  Body: ${notification2.body}`);
  console.log();

  // -------------------------------------------------------------------------
  // Summary
  // -------------------------------------------------------------------------
  console.log('='.repeat(70));
  console.log('[Line 440] Builder Pattern Benefits Demonstrated:');
  console.log('='.repeat(70));
  console.log('[Line 442] 1. Separation of construction logic from representation');
  console.log('[Line 443] 2. Same construction process creates different representations');
  console.log('[Line 444] 3. Fluent interface enables readable, chainable code');
  console.log('[Line 445] 4. Director encapsulates common construction patterns');
  console.log('[Line 446] 5. Builder can be reused to create multiple objects');
  console.log('[Line 447] 6. Easy to add new builder types (Open/Closed Principle)');
  console.log('='.repeat(70));
}

main();
