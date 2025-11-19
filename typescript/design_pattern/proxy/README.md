# Proxy Design Pattern in TypeScript

## Pattern Description

The **Proxy pattern** is a structural design pattern that provides a surrogate or placeholder for another object to control access to it. A proxy acts as an intermediary between a client and the real object, allowing you to perform operations before or after the request reaches the target object.

### Types of Proxies Demonstrated

1. **Virtual Proxy**: Delays the creation of expensive objects until they are actually needed (lazy loading)
2. **Protection Proxy**: Controls access to the original object based on access rights
3. **Logging Proxy**: Adds logging/audit functionality without modifying the real object

### Key Participants

- **Subject (Document)**: Common interface for RealSubject and Proxy
- **RealSubject (RealDocument)**: The actual object that the proxy represents
- **Proxy (VirtualDocumentProxy, ProtectionDocumentProxy, LoggingDocumentProxy)**: Controls access to the RealSubject

## Requirements

- **Node.js**: 18.0 or higher
- **TypeScript**: 5.3.0 or higher

## How to Run

```bash
# Install dependencies
npm install

# Run the demonstration
npm run start
```

## Source Code

```typescript
     1→/**
     2→ * Proxy Design Pattern Implementation in TypeScript
     3→ *
     4→ * This example demonstrates three types of proxies in a Document Management System:
     5→ * 1. Virtual Proxy - Lazy loading of expensive document content
     6→ * 2. Protection Proxy - Access control based on user roles
     7→ * 3. Logging Proxy - Audit trail for all document operations
     8→ */
     9→
    10→// [Line 11] Subject Interface - defines common interface for RealSubject and Proxy
    11→interface Document {
    12→  getTitle(): string;
    13→  getContent(): string;
    14→  setContent(content: string): void;
    15→  getMetadata(): DocumentMetadata;
    16→}
    17→
    18→// [Line 18] Metadata interface for document information
    19→interface DocumentMetadata {
    20→  id: string;
    21→  title: string;
    22→  author: string;
    23→  createdAt: Date;
    24→  size: number;
    25→  accessLevel: 'public' | 'internal' | 'confidential';
    26→}
    27→
    28→// [Line 27] User interface for access control
    29→interface User {
    30→  id: string;
    31→  name: string;
    32→  role: 'guest' | 'employee' | 'manager' | 'admin';
    33→}
    34→
    35→// [Line 33] RealSubject - The actual document with expensive operations
    36→class RealDocument implements Document {
    37→  private title: string;
    38→  private content: string;
    39→  private metadata: DocumentMetadata;
    40→
    41→  constructor(metadata: DocumentMetadata) {
    42→    this.metadata = metadata;
    43→    this.title = metadata.title;
    44→    // [Line 42] Simulate expensive content loading from database/storage
    45→    console.log(`  [Line 42] Loading document "${this.title}" from storage...`);
    46→    this.simulateExpensiveLoad();
    47→    this.content = `Full content of "${this.title}". This is a detailed document with ${metadata.size} bytes of data.`;
    48→    console.log(`  [Line 45] Document "${this.title}" loaded successfully`);
    49→  }
    50→
    51→  private simulateExpensiveLoad(): void {
    52→    // [Line 49] Simulate network/disk latency
    53→    const start = Date.now();
    54→    while (Date.now() - start < 100) {
    55→      // Busy wait to simulate loading delay
    56→    }
    57→  }
    58→
    59→  getTitle(): string {
    60→    return this.title;
    61→  }
    62→
    63→  getContent(): string {
    64→    return this.content;
    65→  }
    66→
    67→  setContent(content: string): void {
    68→    this.content = content;
    69→    console.log(`  [Line 64] Content updated for document "${this.title}"`);
    70→  }
    71→
    72→  getMetadata(): DocumentMetadata {
    73→    return this.metadata;
    74→  }
    75→}
    76→
    77→// =============================================================================
    78→// VIRTUAL PROXY - Lazy Loading
    79→// =============================================================================
    80→
    81→// [Line 75] Virtual Proxy - Delays expensive object creation until needed
    82→class VirtualDocumentProxy implements Document {
    83→  private realDocument: RealDocument | null = null;
    84→  private metadata: DocumentMetadata;
    85→
    86→  constructor(metadata: DocumentMetadata) {
    87→    this.metadata = metadata;
    88→    console.log(`  [Line 82] Virtual proxy created for "${metadata.title}" (not loaded yet)`);
    89→  }
    90→
    91→  // [Line 85] Lazy initialization - creates real object only when needed
    92→  private getRealDocument(): RealDocument {
    93→    if (this.realDocument === null) {
    94→      console.log(`  [Line 88] First access - initializing real document...`);
    95→      this.realDocument = new RealDocument(this.metadata);
    96→    }
    97→    return this.realDocument;
    98→  }
    99→
   100→  getTitle(): string {
   101→    // [Line 94] Title can be returned from metadata without loading full document
   102→    return this.metadata.title;
   103→  }
   104→
   105→  getContent(): string {
   106→    // [Line 99] Content requires full document loading
   107→    console.log(`  [Line 99] Content requested - triggering lazy load`);
   108→    return this.getRealDocument().getContent();
   109→  }
   110→
   111→  setContent(content: string): void {
   112→    this.getRealDocument().setContent(content);
   113→  }
   114→
   115→  getMetadata(): DocumentMetadata {
   116→    // [Line 108] Metadata available without loading full document
   117→    return this.metadata;
   118→  }
   119→}
   120→
   121→// =============================================================================
   122→// PROTECTION PROXY - Access Control
   123→// =============================================================================
   124→
   125→// [Line 116] Protection Proxy - Controls access based on user permissions
   126→class ProtectionDocumentProxy implements Document {
   127→  private document: Document;
   128→  private user: User;
   129→
   130→  constructor(document: Document, user: User) {
   131→    this.document = document;
   132→    this.user = user;
   133→    console.log(`  [Line 124] Protection proxy created for user "${user.name}" (${user.role})`);
   134→  }
   135→
   136→  // [Line 127] Check if user has read access
   137→  private canRead(): boolean {
   138→    const accessLevel = this.document.getMetadata().accessLevel;
   139→
   140→    if (accessLevel === 'public') return true;
   141→    if (accessLevel === 'internal' && this.user.role !== 'guest') return true;
   142→    if (accessLevel === 'confidential' &&
   143→        (this.user.role === 'manager' || this.user.role === 'admin')) return true;
   144→
   145→    return false;
   146→  }
   147→
   148→  // [Line 138] Check if user has write access
   149→  private canWrite(): boolean {
   150→    return this.user.role === 'manager' || this.user.role === 'admin';
   151→  }
   152→
   153→  getTitle(): string {
   154→    // [Line 144] Title is always accessible
   155→    return this.document.getTitle();
   156→  }
   157→
   158→  getContent(): string {
   159→    // [Line 149] Content requires read permission
   160→    if (!this.canRead()) {
   161→      const msg = `Access denied: User "${this.user.name}" cannot read confidential document`;
   162→      console.log(`  [Line 151] ${msg}`);
   163→      throw new Error(msg);
   164→    }
   165→    console.log(`  [Line 154] Access granted: User "${this.user.name}" reading document`);
   166→    return this.document.getContent();
   167→  }
   168→
   169→  setContent(content: string): void {
   170→    // [Line 159] Writing requires write permission
   171→    if (!this.canWrite()) {
   172→      const msg = `Access denied: User "${this.user.name}" (${this.user.role}) cannot modify document`;
   173→      console.log(`  [Line 161] ${msg}`);
   174→      throw new Error(msg);
   175→    }
   176→    console.log(`  [Line 164] Access granted: User "${this.user.name}" modifying document`);
   177→    this.document.setContent(content);
   178→  }
   179→
   180→  getMetadata(): DocumentMetadata {
   181→    return this.document.getMetadata();
   182→  }
   183→}
   184→
   185→// =============================================================================
   186→// LOGGING PROXY - Audit Trail
   187→// =============================================================================
   188→
   189→// [Line 176] Logging Proxy - Records all operations for audit trail
   190→class LoggingDocumentProxy implements Document {
   191→  private document: Document;
   192→  private operationLog: string[] = [];
   193→
   194→  constructor(document: Document) {
   195→    this.document = document;
   196→    this.log('Proxy initialized');
   197→    console.log(`  [Line 184] Logging proxy created for "${document.getTitle()}"`);
   198→  }
   199→
   200→  // [Line 187] Log operation with timestamp
   201→  private log(operation: string): void {
   202→    const timestamp = new Date().toISOString();
   203→    const entry = `[${timestamp}] ${operation}`;
   204→    this.operationLog.push(entry);
   205→  }
   206→
   207→  getTitle(): string {
   208→    this.log(`getTitle() called`);
   209→    const result = this.document.getTitle();
   210→    console.log(`  [Line 197] Logged: getTitle() -> "${result}"`);
   211→    return result;
   212→  }
   213→
   214→  getContent(): string {
   215→    this.log(`getContent() called`);
   216→    const result = this.document.getContent();
   217→    const preview = result.substring(0, 30) + '...';
   218→    console.log(`  [Line 205] Logged: getContent() -> "${preview}"`);
   219→    return result;
   220→  }
   221→
   222→  setContent(content: string): void {
   223→    this.log(`setContent() called with ${content.length} characters`);
   224→    console.log(`  [Line 211] Logged: setContent() with ${content.length} chars`);
   225→    this.document.setContent(content);
   226→  }
   227→
   228→  getMetadata(): DocumentMetadata {
   229→    this.log(`getMetadata() called`);
   230→    return this.document.getMetadata();
   231→  }
   232→
   233→  // [Line 219] Get audit log for review
   234→  getAuditLog(): string[] {
   235→    return [...this.operationLog];
   236→  }
   237→}
   238→
   239→// =============================================================================
   240→// COMBINED PROXY - Demonstrates proxy chaining
   241→// =============================================================================
   242→
   243→// [Line 228] Document Management System - Factory for creating proxied documents
   244→class DocumentManagementSystem {
   245→  private documents: Map<string, DocumentMetadata> = new Map();
   246→
   247→  constructor() {
   248→    // [Line 233] Initialize with sample documents
   249→    this.registerDocument({
   250→      id: 'doc-001',
   251→      title: 'Public Report',
   252→      author: 'John Smith',
   253→      createdAt: new Date('2024-01-15'),
   254→      size: 15000,
   255→      accessLevel: 'public'
   256→    });
   257→
   258→    this.registerDocument({
   259→      id: 'doc-002',
   260→      title: 'Internal Strategy',
   261→      author: 'Jane Doe',
   262→      createdAt: new Date('2024-02-20'),
   263→      size: 45000,
   264→      accessLevel: 'internal'
   265→    });
   266→
   267→    this.registerDocument({
   268→      id: 'doc-003',
   269→      title: 'Confidential Financials',
   270→      author: 'CFO Office',
   271→      createdAt: new Date('2024-03-10'),
   272→      size: 120000,
   273→      accessLevel: 'confidential'
   274→    });
   275→  }
   276→
   277→  private registerDocument(metadata: DocumentMetadata): void {
   278→    this.documents.set(metadata.id, metadata);
   279→  }
   280→
   281→  // [Line 263] Get document with all proxy layers
   282→  getDocument(docId: string, user: User): Document | null {
   283→    const metadata = this.documents.get(docId);
   284→    if (!metadata) {
   285→      console.log(`  [Line 266] Document "${docId}" not found`);
   286→      return null;
   287→    }
   288→
   289→    console.log(`  [Line 270] Creating proxied document for "${metadata.title}"`);
   290→
   291→    // [Line 272] Chain proxies: Virtual -> Protection -> Logging
   292→    // Order matters: Logging wraps Protection wraps Virtual
   293→    const virtualProxy = new VirtualDocumentProxy(metadata);
   294→    const protectionProxy = new ProtectionDocumentProxy(virtualProxy, user);
   295→    const loggingProxy = new LoggingDocumentProxy(protectionProxy);
   296→
   297→    return loggingProxy;
   298→  }
   299→
   300→  listDocuments(): DocumentMetadata[] {
   301→    return Array.from(this.documents.values());
   302→  }
   303→}
```

## Program Output

```
======================================================================
[Line 289] PROXY DESIGN PATTERN DEMONSTRATION
======================================================================

[Line 293] Initializing Document Management System...


======================================================================
[Line 308] DEMO 1: VIRTUAL PROXY - LAZY LOADING
======================================================================

[Line 311] Creating virtual proxy for document...
  [Line 82] Virtual proxy created for "Test Document" (not loaded yet)

[Line 323] Getting title (no loading required):
  Result: "Test Document"

[Line 326] Getting metadata (no loading required):
  Result: Size = 5000 bytes

[Line 329] Getting content (triggers lazy loading):
  [Line 99] Content requested - triggering lazy load
  [Line 88] First access - initializing real document...
  [Line 42] Loading document "Test Document" from storage...
  [Line 45] Document "Test Document" loaded successfully
  Result: "Full content of "Test Document". This is a detaile..."

[Line 333] Getting content again (already loaded):
  [Line 99] Content requested - triggering lazy load
  Result: Retrieved from cached instance

======================================================================
[Line 341] DEMO 2: PROTECTION PROXY - ACCESS CONTROL
======================================================================

[Line 347] Testing access to confidential document...

[Line 350] Manager "Carol" accessing confidential doc:
  [Line 270] Creating proxied document for "Confidential Financials"
  [Line 82] Virtual proxy created for "Confidential Financials" (not loaded yet)
  [Line 124] Protection proxy created for user "Carol" (manager)
  [Line 184] Logging proxy created for "Confidential Financials"
  [Line 197] Logged: getTitle() -> "Confidential Financials"
  Title: "Confidential Financials"
  [Line 154] Access granted: User "Carol" reading document
  [Line 99] Content requested - triggering lazy load
  [Line 88] First access - initializing real document...
  [Line 42] Loading document "Confidential Financials" from storage...
  [Line 45] Document "Confidential Financials" loaded successfully
  [Line 205] Logged: getContent() -> "Full content of "Confidential ..."

[Line 362] Employee "Bob" accessing confidential doc:
  [Line 270] Creating proxied document for "Confidential Financials"
  [Line 82] Virtual proxy created for "Confidential Financials" (not loaded yet)
  [Line 124] Protection proxy created for user "Bob" (employee)
  [Line 184] Logging proxy created for "Confidential Financials"
  [Line 197] Logged: getTitle() -> "Confidential Financials"
  Title: "Confidential Financials"
  [Line 151] Access denied: User "Bob" cannot read confidential document
  Error: Access denied: User "Bob" cannot read confidential document

[Line 374] Employee "Bob" accessing internal doc:
  [Line 270] Creating proxied document for "Internal Strategy"
  [Line 82] Virtual proxy created for "Internal Strategy" (not loaded yet)
  [Line 124] Protection proxy created for user "Bob" (employee)
  [Line 184] Logging proxy created for "Internal Strategy"
  [Line 197] Logged: getTitle() -> "Internal Strategy"
  Title: "Internal Strategy"
  [Line 154] Access granted: User "Bob" reading document
  [Line 99] Content requested - triggering lazy load
  [Line 88] First access - initializing real document...
  [Line 42] Loading document "Internal Strategy" from storage...
  [Line 45] Document "Internal Strategy" loaded successfully
  [Line 205] Logged: getContent() -> "Full content of "Internal Stra..."

======================================================================
[Line 390] DEMO 3: LOGGING PROXY - AUDIT TRAIL
======================================================================

[Line 393] Creating document with logging proxy...
  [Line 42] Loading document "Audited Document" from storage...
  [Line 45] Document "Audited Document" loaded successfully
  [Line 184] Logging proxy created for "Audited Document"

[Line 406] Performing operations...
  [Line 197] Logged: getTitle() -> "Audited Document"
  [Line 205] Logged: getContent() -> "Full content of "Audited Docum..."
  [Line 211] Logged: setContent() with 45 chars
  [Line 64] Content updated for document "Audited Document"

[Line 412] Retrieving audit log:
  1. [2025-11-19T00:59:48.143Z] Proxy initialized
  2. [2025-11-19T00:59:48.143Z] getTitle() called
  3. [2025-11-19T00:59:48.143Z] getContent() called
  4. [2025-11-19T00:59:48.143Z] setContent() called with 45 characters
  5. [2025-11-19T00:59:48.143Z] getMetadata() called

======================================================================
[Line 422] DEMO 4: WRITE ACCESS CONTROL
======================================================================

[Line 428] Admin "Dave" modifying public document:
  [Line 270] Creating proxied document for "Public Report"
  [Line 82] Virtual proxy created for "Public Report" (not loaded yet)
  [Line 124] Protection proxy created for user "Dave" (admin)
  [Line 184] Logging proxy created for "Public Report"
  [Line 211] Logged: setContent() with 26 chars
  [Line 164] Access granted: User "Dave" modifying document
  [Line 88] First access - initializing real document...
  [Line 42] Loading document "Public Report" from storage...
  [Line 45] Document "Public Report" loaded successfully
  [Line 64] Content updated for document "Public Report"
  Modification successful!

[Line 439] Guest "Alice" attempting to modify document:
  [Line 270] Creating proxied document for "Public Report"
  [Line 82] Virtual proxy created for "Public Report" (not loaded yet)
  [Line 124] Protection proxy created for user "Alice" (guest)
  [Line 184] Logging proxy created for "Public Report"
  [Line 211] Logged: setContent() with 33 chars
  [Line 161] Access denied: User "Alice" (guest) cannot modify document
  Error: Access denied: User "Alice" (guest) cannot modify document

======================================================================
[Line 454] PROXY PATTERN SUMMARY
======================================================================

Key Benefits Demonstrated:
1. Virtual Proxy: Deferred expensive operations until actually needed
2. Protection Proxy: Enforced access control without modifying real object
3. Logging Proxy: Added audit capabilities transparently
4. Proxy Chaining: Combined multiple proxy types for comprehensive control

The Proxy pattern allows us to control access to objects while maintaining
the same interface, enabling lazy loading, security, and monitoring.
```

## Code Analysis and Annotations

### Demo 1: Virtual Proxy - Lazy Loading

| Output Line | Source Line | Description |
|------------|-------------|-------------|
| `[Line 82] Virtual proxy created for "Test Document"` | Line 82 | VirtualDocumentProxy constructor stores metadata but does NOT create RealDocument yet |
| `Result: "Test Document"` | Line 94 | `getTitle()` returns from metadata directly - no expensive loading needed |
| `Result: Size = 5000 bytes` | Line 108 | `getMetadata()` also uses cached metadata - still no loading |
| `[Line 99] Content requested - triggering lazy load` | Line 99 | `getContent()` requires full document - triggers lazy initialization |
| `[Line 88] First access - initializing real document...` | Line 88 | `getRealDocument()` detects null and creates RealDocument |
| `[Line 42] Loading document "Test Document" from storage...` | Line 42 | RealDocument constructor simulates expensive database/file load |
| `Result: Retrieved from cached instance` | Line 88 | Second `getContent()` call - RealDocument already cached, no reload |

**Key Insight**: The Virtual Proxy defers costly object creation until the first operation that actually requires it.

### Demo 2: Protection Proxy - Access Control

| Output Line | Source Line | Description |
|------------|-------------|-------------|
| `[Line 270] Creating proxied document` | Line 270 | DocumentManagementSystem creates proxy chain |
| `[Line 124] Protection proxy created for user "Carol"` | Line 124 | Protection proxy initialized with user context |
| `[Line 154] Access granted: User "Carol" reading document` | Line 154 | Manager role passes `canRead()` check for confidential docs (Lines 140-145) |
| `[Line 151] Access denied: User "Bob"` | Line 151 | Employee role fails `canRead()` for confidential access level |
| `[Line 154] Access granted: User "Bob" reading document` | Line 154 | Same employee CAN read internal documents - passes role check |

**Access Control Matrix**:

| Document Type | Guest | Employee | Manager | Admin |
|--------------|-------|----------|---------|-------|
| Public | Read | Read | Read/Write | Read/Write |
| Internal | Denied | Read | Read/Write | Read/Write |
| Confidential | Denied | Denied | Read/Write | Read/Write |

### Demo 3: Logging Proxy - Audit Trail

| Output Line | Source Line | Description |
|------------|-------------|-------------|
| `[Line 184] Logging proxy created` | Line 184 | LoggingDocumentProxy wraps document and starts audit log |
| `[Line 197] Logged: getTitle()` | Line 197 | Each operation is logged with timestamp before delegation |
| `[Line 205] Logged: getContent()` | Line 205 | Content access logged with preview |
| `[Line 211] Logged: setContent()` | Line 211 | Write operations logged with content length |
| `Audit log entries 1-5` | Line 219 | `getAuditLog()` returns complete operation history |

**Audit Log Format**: `[ISO Timestamp] Operation Description`

### Demo 4: Write Access Control

| Output Line | Source Line | Description |
|------------|-------------|-------------|
| `[Line 164] Access granted: User "Dave" modifying` | Line 164 | Admin passes `canWrite()` check (Line 149-151) |
| `[Line 88] First access - initializing real document` | Line 88 | Write operation triggers lazy load through VirtualProxy |
| `[Line 64] Content updated for document` | Line 64 | RealDocument's `setContent()` updates internal state |
| `[Line 161] Access denied: User "Alice" (guest)` | Line 161 | Guest role fails `canWrite()` - only managers/admins can write |

### Proxy Chaining Architecture

The DocumentManagementSystem creates a three-layer proxy chain (Lines 291-295):

```
Client -> LoggingProxy -> ProtectionProxy -> VirtualProxy -> RealDocument
```

**Execution Flow for `getContent()`**:

1. **LoggingProxy** (Line 214-219): Logs the operation with timestamp
2. **ProtectionProxy** (Line 158-167): Checks user permissions
3. **VirtualProxy** (Line 105-108): Lazy loads RealDocument if needed
4. **RealDocument** (Line 63-64): Returns actual content

This ordering ensures:
- All operations are logged (even failures)
- Access control is enforced before expensive loading
- Expensive objects are only created when access is granted

## Key Takeaways

### When to Use the Proxy Pattern

1. **Lazy Initialization (Virtual Proxy)**: When you have heavy objects that consume system resources but are rarely used
2. **Access Control (Protection Proxy)**: When you need different access rights for different clients
3. **Logging/Caching (Logging Proxy)**: When you need to add supplementary behavior without modifying the original class
4. **Remote Proxy**: When the real object is in a different address space (not shown in this demo)

### Benefits

- **Single Responsibility**: Each proxy handles one concern (loading, access, logging)
- **Open/Closed**: Add new proxies without modifying existing code
- **Transparency**: Clients use the same interface regardless of proxy presence
- **Composability**: Proxies can be chained for layered functionality

### Considerations

- **Performance**: Each proxy layer adds overhead (minimal but present)
- **Complexity**: Multiple proxy types can make debugging harder
- **Response Time**: Protection checks happen on every access
