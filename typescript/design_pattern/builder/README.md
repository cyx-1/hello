# Builder Design Pattern - TypeScript Implementation

## Pattern Description

The **Builder** design pattern is a creational pattern that separates the construction of a complex object from its representation. It allows the same construction process to create different representations of an object.

### Key Components

1. **Product** (`HttpRequest`): The complex object being built
2. **Builder Interface** (`HttpRequestBuilder`): Declares the building steps
3. **Concrete Builders** (`GetRequestBuilder`, `PostRequestBuilder`, `PutRequestBuilder`): Implement the building steps
4. **Director** (`ApiRequestDirector`): Orchestrates the building process with predefined configurations

### When to Use

- When you need to create complex objects with many optional parameters
- When the construction process should allow different representations
- When you want to construct objects step-by-step
- When you need to isolate complex construction code from business logic

## Requirements

- **Node.js**: 18.0 or higher
- **TypeScript**: 5.3.0 or higher

## How to Run

```bash
# Install dependencies
npm install

# Compile and run
npm run start

# Or for development with ts-node (if installed globally)
npm run dev
```

---

## Source Code

**File: `main_builder.ts`**

```typescript
     1	/**
     2	 * Builder Design Pattern - HTTP Request Builder Example
     3	 *
     4	 * The Builder pattern separates the construction of a complex object from its
     5	 * representation, allowing the same construction process to create different
     6	 * representations.
     7	 */
     8
     9	// =============================================================================
    10	// Product: The complex object being built
    11	// =============================================================================
    12
    13	interface HttpHeader {
    14	  name: string;
    15	  value: string;
    16	}
    17
    18	interface QueryParam {
    19	  key: string;
    20	  value: string;
    21	}
    22
    23	class HttpRequest {
    24	  public method: string = 'GET';
    25	  public url: string = '';
    26	  public headers: HttpHeader[] = [];
    27	  public queryParams: QueryParam[] = [];
    28	  public body: string | null = null;
    29	  public timeout: number = 30000;
    30	  public retries: number = 0;
    31	  public authentication: { type: string; credentials: string } | null = null;
    32
    33	  public describe(): string {
    34	    let description = `${this.method} ${this.url}`;
    35
    36	    if (this.queryParams.length > 0) {
    37	      const params = this.queryParams.map(p => `${p.key}=${p.value}`).join('&');
    38	      description += `?${params}`;
    39	    }
    40
    41	    return description;
    42	  }
    43
    44	  public getFullDetails(): string[] {
    45	    const details: string[] = [];
    46	    details.push(`Method: ${this.method}`);
    47	    details.push(`URL: ${this.url}`);
    48
    49	    if (this.queryParams.length > 0) {
    50	      details.push(`Query Params: ${this.queryParams.map(p => `${p.key}=${p.value}`).join(', ')}`);
    51	    }
    52
    53	    if (this.headers.length > 0) {
    54	      details.push(`Headers: ${this.headers.map(h => `${h.name}: ${h.value}`).join(', ')}`);
    55	    }
    56
    57	    if (this.body) {
    58	      details.push(`Body: ${this.body}`);
    59	    }
    60
    61	    if (this.authentication) {
    62	      details.push(`Auth: ${this.authentication.type}`);
    63	    }
    64
    65	    details.push(`Timeout: ${this.timeout}ms`);
    66	    details.push(`Retries: ${this.retries}`);
    67
    68	    return details;
    69	  }
    70	}
    71
    72	// =============================================================================
    73	// Builder Interface: Declares the building steps
    74	// =============================================================================
    75
    76	interface HttpRequestBuilder {
    77	  reset(): HttpRequestBuilder;
    78	  setUrl(url: string): HttpRequestBuilder;
    79	  addHeader(name: string, value: string): HttpRequestBuilder;
    80	  addQueryParam(key: string, value: string): HttpRequestBuilder;
    81	  setBody(body: string): HttpRequestBuilder;
    82	  setTimeout(timeout: number): HttpRequestBuilder;
    83	  setRetries(retries: number): HttpRequestBuilder;
    84	  setAuthentication(type: string, credentials: string): HttpRequestBuilder;
    85	  build(): HttpRequest;
    86	}
    87
    88	// =============================================================================
    89	// Concrete Builder: GET Request Builder
    90	// =============================================================================
    91
    92	class GetRequestBuilder implements HttpRequestBuilder {
    93	  private request: HttpRequest;
    94
    95	  constructor() {
    96	    this.request = new HttpRequest();
    97	    this.request.method = 'GET';
    98	  }
    99
   100	  public reset(): HttpRequestBuilder {
   101	    this.request = new HttpRequest();
   102	    this.request.method = 'GET';
   103	    return this;
   104	  }
   105
   106	  public setUrl(url: string): HttpRequestBuilder {
   107	    this.request.url = url;
   108	    return this;
   109	  }
   110
   111	  public addHeader(name: string, value: string): HttpRequestBuilder {
   112	    this.request.headers.push({ name, value });
   113	    return this;
   114	  }
   115
   116	  public addQueryParam(key: string, value: string): HttpRequestBuilder {
   117	    this.request.queryParams.push({ key, value });
   118	    return this;
   119	  }
   120
   121	  public setBody(body: string): HttpRequestBuilder {
   122	    // GET requests typically don't have a body, but we allow it for flexibility
   123	    console.log('[Line 106] Warning: GET requests typically should not have a body');
   124	    this.request.body = body;
   125	    return this;
   126	  }
   127
   128	  public setTimeout(timeout: number): HttpRequestBuilder {
   129	    this.request.timeout = timeout;
   130	    return this;
   131	  }
   132
   133	  public setRetries(retries: number): HttpRequestBuilder {
   134	    this.request.retries = retries;
   135	    return this;
   136	  }
   137
   138	  public setAuthentication(type: string, credentials: string): HttpRequestBuilder {
   139	    this.request.authentication = { type, credentials };
   140	    return this;
   141	  }
   142
   143	  public build(): HttpRequest {
   144	    const result = this.request;
   145	    this.reset();
   146	    return result;
   147	  }
   148	}
   149
   150	// =============================================================================
   151	// Concrete Builder: POST Request Builder
   152	// =============================================================================
   153
   154	class PostRequestBuilder implements HttpRequestBuilder {
   155	  private request: HttpRequest;
   156
   157	  constructor() {
   158	    this.request = new HttpRequest();
   159	    this.request.method = 'POST';
   160	    // POST requests commonly use JSON content type
   161	    this.request.headers.push({ name: 'Content-Type', value: 'application/json' });
   162	  }
   163
   164	  public reset(): HttpRequestBuilder {
   165	    this.request = new HttpRequest();
   166	    this.request.method = 'POST';
   167	    this.request.headers.push({ name: 'Content-Type', value: 'application/json' });
   168	    return this;
   169	  }
   170
   171	  public setUrl(url: string): HttpRequestBuilder {
   172	    this.request.url = url;
   173	    return this;
   174	  }
   175
   176	  public addHeader(name: string, value: string): HttpRequestBuilder {
   177	    this.request.headers.push({ name, value });
   178	    return this;
   179	  }
   180
   181	  public addQueryParam(key: string, value: string): HttpRequestBuilder {
   182	    this.request.queryParams.push({ key, value });
   183	    return this;
   184	  }
   185
   186	  public setBody(body: string): HttpRequestBuilder {
   187	    this.request.body = body;
   188	    return this;
   189	  }
   190
   191	  public setTimeout(timeout: number): HttpRequestBuilder {
   192	    this.request.timeout = timeout;
   193	    return this;
   194	  }
   195
   196	  public setRetries(retries: number): HttpRequestBuilder {
   197	    this.request.retries = retries;
   198	    return this;
   199	  }
   200
   201	  public setAuthentication(type: string, credentials: string): HttpRequestBuilder {
   202	    this.request.authentication = { type, credentials };
   203	    return this;
   204	  }
   205
   206	  public build(): HttpRequest {
   207	    const result = this.request;
   208	    this.reset();
   209	    return result;
   210	  }
   211	}
   212
   213	// =============================================================================
   214	// Concrete Builder: PUT Request Builder
   215	// =============================================================================
   216
   217	class PutRequestBuilder implements HttpRequestBuilder {
   218	  private request: HttpRequest;
   219
   220	  constructor() {
   221	    this.request = new HttpRequest();
   222	    this.request.method = 'PUT';
   223	    this.request.headers.push({ name: 'Content-Type', value: 'application/json' });
   224	  }
   225
   226	  public reset(): HttpRequestBuilder {
   227	    this.request = new HttpRequest();
   228	    this.request.method = 'PUT';
   229	    this.request.headers.push({ name: 'Content-Type', value: 'application/json' });
   230	    return this;
   231	  }
   232
   233	  public setUrl(url: string): HttpRequestBuilder {
   234	    this.request.url = url;
   235	    return this;
   236	  }
   237
   238	  public addHeader(name: string, value: string): HttpRequestBuilder {
   239	    this.request.headers.push({ name, value });
   240	    return this;
   241	  }
   242
   243	  public addQueryParam(key: string, value: string): HttpRequestBuilder {
   244	    this.request.queryParams.push({ key, value });
   245	    return this;
   246	  }
   247
   248	  public setBody(body: string): HttpRequestBuilder {
   249	    this.request.body = body;
   250	    return this;
   251	  }
   252
   253	  public setTimeout(timeout: number): HttpRequestBuilder {
   254	    this.request.timeout = timeout;
   255	    return this;
   256	  }
   257
   258	  public setRetries(retries: number): HttpRequestBuilder {
   259	    this.request.retries = retries;
   260	    return this;
   261	  }
   262
   263	  public setAuthentication(type: string, credentials: string): HttpRequestBuilder {
   264	    this.request.authentication = { type, credentials };
   265	    return this;
   266	  }
   267
   268	  public build(): HttpRequest {
   269	    const result = this.request;
   270	    this.reset();
   271	    return result;
   272	  }
   273	}
   274
   275	// =============================================================================
   276	// Director: Orchestrates the building process with predefined configurations
   277	// =============================================================================
   278
   279	class ApiRequestDirector {
   280	  private builder: HttpRequestBuilder;
   281
   282	  constructor(builder: HttpRequestBuilder) {
   283	    this.builder = builder;
   284	  }
   285
   286	  public setBuilder(builder: HttpRequestBuilder): void {
   287	    this.builder = builder;
   288	  }
   289
   290	  // Build a simple API health check request
   291	  public buildHealthCheck(baseUrl: string): HttpRequest {
   292	    return this.builder
   293	      .reset()
   294	      .setUrl(`${baseUrl}/health`)
   295	      .setTimeout(5000)
   296	      .setRetries(3)
   297	      .build();
   298	  }
   299
   300	  // Build an authenticated API request with standard headers
   301	  public buildAuthenticatedRequest(url: string, token: string): HttpRequest {
   302	    return this.builder
   303	      .reset()
   304	      .setUrl(url)
   305	      .addHeader('Accept', 'application/json')
   306	      .addHeader('X-Request-ID', crypto.randomUUID())
   307	      .setAuthentication('Bearer', token)
   308	      .setTimeout(10000)
   309	      .setRetries(2)
   310	      .build();
   311	  }
   312
   313	  // Build a paginated list request
   314	  public buildPaginatedListRequest(
   315	    baseUrl: string,
   316	    resource: string,
   317	    page: number,
   318	    limit: number
   319	  ): HttpRequest {
   320	    return this.builder
   321	      .reset()
   322	      .setUrl(`${baseUrl}/${resource}`)
   323	      .addQueryParam('page', page.toString())
   324	      .addQueryParam('limit', limit.toString())
   325	      .addHeader('Accept', 'application/json')
   326	      .setTimeout(15000)
   327	      .build();
   328	  }
   329
   330	  // Build a create resource request (for POST builder)
   331	  public buildCreateResourceRequest(
   332	    baseUrl: string,
   333	    resource: string,
   334	    data: object,
   335	    token: string
   336	  ): HttpRequest {
   337	    return this.builder
   338	      .reset()
   339	      .setUrl(`${baseUrl}/${resource}`)
   340	      .setBody(JSON.stringify(data))
   341	      .setAuthentication('Bearer', token)
   342	      .addHeader('X-Request-ID', crypto.randomUUID())
   343	      .setTimeout(20000)
   344	      .setRetries(1)
   345	      .build();
   346	  }
   347
   348	  // Build an update resource request (for PUT builder)
   349	  public buildUpdateResourceRequest(
   350	    baseUrl: string,
   351	    resource: string,
   352	    id: string,
   353	    data: object,
   354	    token: string
   355	  ): HttpRequest {
   356	    return this.builder
   357	      .reset()
   358	      .setUrl(`${baseUrl}/${resource}/${id}`)
   359	      .setBody(JSON.stringify(data))
   360	      .setAuthentication('Bearer', token)
   361	      .setTimeout(20000)
   362	      .setRetries(1)
   363	      .build();
   364	  }
   365	}
   366
   367	// =============================================================================
   368	// Main: Demonstration of the Builder Pattern
   369	// =============================================================================
   370
   371	function main(): void {
   372	  console.log('='.repeat(70));
   373	  console.log('[Line 301] Builder Design Pattern - HTTP Request Builder Demo');
   374	  console.log('='.repeat(70));
   375	  console.log();
   376
   377	  // -------------------------------------------------------------------------
   378	  // Example 1: Using Director with GET Request Builder
   379	  // -------------------------------------------------------------------------
   380	  console.log('[Line 308] Example 1: Director with GET Request Builder');
   381	  console.log('-'.repeat(70));
   382
   383	  const getBuilder = new GetRequestBuilder();
   384	  const director = new ApiRequestDirector(getBuilder);
   385
   386	  // Build a health check request
   387	  console.log('[Line 315] Building health check request...');
   388	  const healthCheck = director.buildHealthCheck('https://api.example.com');
   389	  console.log(`[Line 317] Health Check: ${healthCheck.describe()}`);
   390	  healthCheck.getFullDetails().forEach(detail => console.log(`  ${detail}`));
   391	  console.log();
   392
   393	  // Build a paginated list request
   394	  console.log('[Line 322] Building paginated users list request...');
   395	  const usersList = director.buildPaginatedListRequest(
   396	    'https://api.example.com',
   397	    'users',
   398	    1,
   399	    25
   400	  );
   401	  console.log(`[Line 329] Users List: ${usersList.describe()}`);
   402	  usersList.getFullDetails().forEach(detail => console.log(`  ${detail}`));
   403	  console.log();
   404
   405	  // -------------------------------------------------------------------------
   406	  // Example 2: Using Director with POST Request Builder
   407	  // -------------------------------------------------------------------------
   408	  console.log('[Line 336] Example 2: Director with POST Request Builder');
   409	  console.log('-'.repeat(70));
   410
   411	  const postBuilder = new PostRequestBuilder();
   412	  director.setBuilder(postBuilder);
   413
   414	  // Build a create user request
   415	  console.log('[Line 343] Building create user request...');
   416	  const createUser = director.buildCreateResourceRequest(
   417	    'https://api.example.com',
   418	    'users',
   419	    { name: 'John Doe', email: 'john@example.com', role: 'admin' },
   420	    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
   421	  );
   422	  console.log(`[Line 350] Create User: ${createUser.describe()}`);
   423	  createUser.getFullDetails().forEach(detail => console.log(`  ${detail}`));
   424	  console.log();
   425
   426	  // -------------------------------------------------------------------------
   427	  // Example 3: Using Director with PUT Request Builder
   428	  // -------------------------------------------------------------------------
   429	  console.log('[Line 357] Example 3: Director with PUT Request Builder');
   430	  console.log('-'.repeat(70));
   431
   432	  const putBuilder = new PutRequestBuilder();
   433	  director.setBuilder(putBuilder);
   434
   435	  // Build an update user request
   436	  console.log('[Line 364] Building update user request...');
   437	  const updateUser = director.buildUpdateResourceRequest(
   438	    'https://api.example.com',
   439	    'users',
   440	    '12345',
   441	    { name: 'Jane Doe', email: 'jane@example.com' },
   442	    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
   443	  );
   444	  console.log(`[Line 372] Update User: ${updateUser.describe()}`);
   445	  updateUser.getFullDetails().forEach(detail => console.log(`  ${detail}`));
   446	  console.log();
   447
   448	  // -------------------------------------------------------------------------
   449	  // Example 4: Manual Builder Usage (Fluent Interface)
   450	  // -------------------------------------------------------------------------
   451	  console.log('[Line 379] Example 4: Manual Builder Usage (Fluent Interface)');
   452	  console.log('-'.repeat(70));
   453
   454	  console.log('[Line 382] Building custom search request manually...');
   455	  const customRequest = new GetRequestBuilder()
   456	    .setUrl('https://api.example.com/search')
   457	    .addQueryParam('q', 'typescript builder pattern')
   458	    .addQueryParam('sort', 'relevance')
   459	    .addQueryParam('limit', '50')
   460	    .addHeader('Accept', 'application/json')
   461	    .addHeader('Accept-Language', 'en-US')
   462	    .addHeader('Cache-Control', 'no-cache')
   463	    .setAuthentication('API-Key', 'sk-1234567890abcdef')
   464	    .setTimeout(30000)
   465	    .setRetries(3)
   466	    .build();
   467
   468	  console.log(`[Line 396] Custom Search: ${customRequest.describe()}`);
   469	  customRequest.getFullDetails().forEach(detail => console.log(`  ${detail}`));
   470	  console.log();
   471
   472	  // -------------------------------------------------------------------------
   473	  // Example 5: Building Multiple Requests with Same Builder
   474	  // -------------------------------------------------------------------------
   475	  console.log('[Line 403] Example 5: Building Multiple Requests with Same Builder');
   476	  console.log('-'.repeat(70));
   477
   478	  const reusableBuilder = new PostRequestBuilder();
   479
   480	  console.log('[Line 408] Building first notification request...');
   481	  const notification1 = reusableBuilder
   482	    .setUrl('https://api.example.com/notifications')
   483	    .setBody(JSON.stringify({
   484	      userId: 'user-001',
   485	      message: 'Welcome to the platform!',
   486	      type: 'welcome'
   487	    }))
   488	    .setTimeout(5000)
   489	    .build();
   490	  console.log(`[Line 418] Notification 1: ${notification1.describe()}`);
   491	  console.log(`  Body: ${notification1.body}`);
   492	  console.log();
   493
   494	  console.log('[Line 422] Building second notification request...');
   495	  const notification2 = reusableBuilder
   496	    .setUrl('https://api.example.com/notifications')
   497	    .setBody(JSON.stringify({
   498	      userId: 'user-002',
   499	      message: 'Your order has shipped!',
   500	      type: 'shipping'
   501	    }))
   502	    .setTimeout(5000)
   503	    .build();
   504	  console.log(`[Line 432] Notification 2: ${notification2.describe()}`);
   505	  console.log(`  Body: ${notification2.body}`);
   506	  console.log();
   507
   508	  // -------------------------------------------------------------------------
   509	  // Summary
   510	  // -------------------------------------------------------------------------
   511	  console.log('='.repeat(70));
   512	  console.log('[Line 440] Builder Pattern Benefits Demonstrated:');
   513	  console.log('='.repeat(70));
   514	  console.log('[Line 442] 1. Separation of construction logic from representation');
   515	  console.log('[Line 443] 2. Same construction process creates different representations');
   516	  console.log('[Line 444] 3. Fluent interface enables readable, chainable code');
   517	  console.log('[Line 445] 4. Director encapsulates common construction patterns');
   518	  console.log('[Line 446] 5. Builder can be reused to create multiple objects');
   519	  console.log('[Line 447] 6. Easy to add new builder types (Open/Closed Principle)');
   520	  console.log('='.repeat(70));
   521	}
   522
   523	main();
```

---

## Program Output

```
======================================================================
[Line 301] Builder Design Pattern - HTTP Request Builder Demo
======================================================================

[Line 308] Example 1: Director with GET Request Builder
----------------------------------------------------------------------
[Line 315] Building health check request...
[Line 317] Health Check: GET https://api.example.com/health
  Method: GET
  URL: https://api.example.com/health
  Timeout: 5000ms
  Retries: 3

[Line 322] Building paginated users list request...
[Line 329] Users List: GET https://api.example.com/users?page=1&limit=25
  Method: GET
  URL: https://api.example.com/users
  Query Params: page=1, limit=25
  Headers: Accept: application/json
  Timeout: 15000ms
  Retries: 0

[Line 336] Example 2: Director with POST Request Builder
----------------------------------------------------------------------
[Line 343] Building create user request...
[Line 350] Create User: POST https://api.example.com/users
  Method: POST
  URL: https://api.example.com/users
  Headers: Content-Type: application/json, X-Request-ID: <uuid>
  Body: {"name":"John Doe","email":"john@example.com","role":"admin"}
  Auth: Bearer
  Timeout: 20000ms
  Retries: 1

[Line 357] Example 3: Director with PUT Request Builder
----------------------------------------------------------------------
[Line 364] Building update user request...
[Line 372] Update User: PUT https://api.example.com/users/12345
  Method: PUT
  URL: https://api.example.com/users/12345
  Headers: Content-Type: application/json
  Body: {"name":"Jane Doe","email":"jane@example.com"}
  Auth: Bearer
  Timeout: 20000ms
  Retries: 1

[Line 379] Example 4: Manual Builder Usage (Fluent Interface)
----------------------------------------------------------------------
[Line 382] Building custom search request manually...
[Line 396] Custom Search: GET https://api.example.com/search?q=typescript builder pattern&sort=relevance&limit=50
  Method: GET
  URL: https://api.example.com/search
  Query Params: q=typescript builder pattern, sort=relevance, limit=50
  Headers: Accept: application/json, Accept-Language: en-US, Cache-Control: no-cache
  Auth: API-Key
  Timeout: 30000ms
  Retries: 3

[Line 403] Example 5: Building Multiple Requests with Same Builder
----------------------------------------------------------------------
[Line 408] Building first notification request...
[Line 418] Notification 1: POST https://api.example.com/notifications
  Body: {"userId":"user-001","message":"Welcome to the platform!","type":"welcome"}

[Line 422] Building second notification request...
[Line 432] Notification 2: POST https://api.example.com/notifications
  Body: {"userId":"user-002","message":"Your order has shipped!","type":"shipping"}

======================================================================
[Line 440] Builder Pattern Benefits Demonstrated:
======================================================================
[Line 442] 1. Separation of construction logic from representation
[Line 443] 2. Same construction process creates different representations
[Line 444] 3. Fluent interface enables readable, chainable code
[Line 445] 4. Director encapsulates common construction patterns
[Line 446] 5. Builder can be reused to create multiple objects
[Line 447] 6. Easy to add new builder types (Open/Closed Principle)
======================================================================
```

---

## Code Analysis and Annotations

### Example 1: Director with GET Request Builder

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 308]` | 380 | Announces the start of Example 1, demonstrating Director usage with GET builder |
| `[Line 315]` | 387 | Director's `buildHealthCheck` method is called (Lines 291-298) |
| `[Line 317]` | 389 | Health check request built with 5000ms timeout and 3 retries |
| `[Line 322]` | 394 | Director's `buildPaginatedListRequest` method called (Lines 314-328) |
| `[Line 329]` | 401 | Paginated request includes query params `page=1&limit=25` |

**Key Observations:**
- Lines 383-384: `GetRequestBuilder` is instantiated and passed to Director
- Lines 291-297: Director's `buildHealthCheck` chains `reset()`, `setUrl()`, `setTimeout()`, `setRetries()`, and `build()`
- Lines 320-327: Director's `buildPaginatedListRequest` adds query parameters via `addQueryParam()`

---

### Example 2: Director with POST Request Builder

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 336]` | 408 | Announces Example 2 with POST builder |
| `[Line 343]` | 415 | Director's `buildCreateResourceRequest` called (Lines 331-346) |
| `[Line 350]` | 422 | POST request includes JSON body and Bearer auth |

**Key Observations:**
- Lines 411-412: `PostRequestBuilder` created and set in Director via `setBuilder()`
- Lines 157-162: `PostRequestBuilder` constructor automatically adds `Content-Type: application/json` header
- Lines 337-345: Director chains `setBody()`, `setAuthentication()`, and `addHeader()` for request ID

---

### Example 3: Director with PUT Request Builder

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 357]` | 429 | Announces Example 3 with PUT builder |
| `[Line 364]` | 436 | Director's `buildUpdateResourceRequest` called (Lines 349-364) |
| `[Line 372]` | 444 | PUT request targets specific resource ID in URL path |

**Key Observations:**
- Lines 432-433: `PutRequestBuilder` swapped into Director
- Lines 356-358: URL includes resource ID: `${baseUrl}/${resource}/${id}`
- Lines 220-224: `PutRequestBuilder` also defaults to JSON content type

---

### Example 4: Manual Builder Usage (Fluent Interface)

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 379]` | 451 | Announces manual builder usage without Director |
| `[Line 382]` | 454 | Custom search request built with fluent chaining |
| `[Line 396]` | 468 | Complex request with multiple query params and headers |

**Key Observations:**
- Lines 455-466: Demonstrates fluent interface - each method returns `this`
- Builder methods (Lines 106-141) return `HttpRequestBuilder` enabling chaining
- Three query params, three headers, API-Key auth, 30s timeout, 3 retries all in one chain

---

### Example 5: Builder Reuse

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 403]` | 475 | Announces builder reuse demonstration |
| `[Line 408]` | 480 | First notification request built |
| `[Line 418]` | 490 | Shows welcome notification payload |
| `[Line 422]` | 494 | Second notification request built with same builder |
| `[Line 432]` | 504 | Shows shipping notification payload |

**Key Observations:**
- Line 478: Same `PostRequestBuilder` instance builds multiple requests
- Lines 143-147: `build()` method calls `reset()` internally, preparing builder for next use
- Each notification has different body content but same URL and method

---

### Pattern Benefits Summary

| Output Line | Source Line | Benefit Demonstrated |
|-------------|-------------|----------------------|
| `[Line 442]` | 514 | **Separation of Concerns**: Product class knows nothing about construction |
| `[Line 443]` | 515 | **Multiple Representations**: Same Director builds GET, POST, PUT requests |
| `[Line 444]` | 516 | **Fluent Interface**: Chainable methods improve readability |
| `[Line 445]` | 517 | **Encapsulation**: Director hides complex construction sequences |
| `[Line 446]` | 518 | **Reusability**: Single builder creates multiple products |
| `[Line 447]` | 519 | **Open/Closed**: Add `DeleteRequestBuilder` without modifying existing code |

---

## Class Relationships

```
+---------------------+       +------------------------+
|   HttpRequest       |       | HttpRequestBuilder     |
|   (Product)         |       | (Builder Interface)    |
+---------------------+       +------------------------+
| - method            |       | + reset()              |
| - url               |       | + setUrl()             |
| - headers           |<------| + addHeader()          |
| - queryParams       | builds| + addQueryParam()      |
| - body              |       | + setBody()            |
| - timeout           |       | + setTimeout()         |
| - retries           |       | + setRetries()         |
| - authentication    |       | + setAuthentication()  |
+---------------------+       | + build()              |
                              +------------------------+
                                        ^
                                        | implements
                    +-------------------+-------------------+
                    |                   |                   |
         +------------------+  +------------------+  +------------------+
         | GetRequestBuilder|  |PostRequestBuilder|  | PutRequestBuilder|
         +------------------+  +------------------+  +------------------+
         | method = 'GET'   |  | method = 'POST'  |  | method = 'PUT'   |
         +------------------+  | Content-Type:    |  | Content-Type:    |
                               | application/json |  | application/json |
                               +------------------+  +------------------+

+-------------------------+
| ApiRequestDirector      |
+-------------------------+       uses
| - builder               |--------------> HttpRequestBuilder
+-------------------------+
| + setBuilder()          |
| + buildHealthCheck()    |
| + buildAuthenticatedRequest() |
| + buildPaginatedListRequest() |
| + buildCreateResourceRequest()|
| + buildUpdateResourceRequest()|
+-------------------------+
```

---

## Version Requirements

This code requires:
- **Node.js 18+**: Uses `crypto.randomUUID()` which is available in Node.js 15.6.0+ but stable in 18+
- **TypeScript 5.3+**: Uses modern TypeScript features including strict type checking

---

## Related Patterns

- **Abstract Factory**: Builder focuses on constructing complex objects step by step; Abstract Factory emphasizes families of products
- **Prototype**: Builder constructs objects incrementally; Prototype copies existing objects
- **Composite**: Builders often construct Composite trees
