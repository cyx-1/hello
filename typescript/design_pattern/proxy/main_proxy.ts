/**
 * Proxy Design Pattern Implementation in TypeScript
 *
 * This example demonstrates three types of proxies in a Document Management System:
 * 1. Virtual Proxy - Lazy loading of expensive document content
 * 2. Protection Proxy - Access control based on user roles
 * 3. Logging Proxy - Audit trail for all document operations
 */

// [Line 11] Subject Interface - defines common interface for RealSubject and Proxy
interface Document {
  getTitle(): string;
  getContent(): string;
  setContent(content: string): void;
  getMetadata(): DocumentMetadata;
}

// [Line 18] Metadata interface for document information
interface DocumentMetadata {
  id: string;
  title: string;
  author: string;
  createdAt: Date;
  size: number;
  accessLevel: 'public' | 'internal' | 'confidential';
}

// [Line 27] User interface for access control
interface User {
  id: string;
  name: string;
  role: 'guest' | 'employee' | 'manager' | 'admin';
}

// [Line 33] RealSubject - The actual document with expensive operations
class RealDocument implements Document {
  private title: string;
  private content: string;
  private metadata: DocumentMetadata;

  constructor(metadata: DocumentMetadata) {
    this.metadata = metadata;
    this.title = metadata.title;
    // [Line 42] Simulate expensive content loading from database/storage
    console.log(`  [Line 42] Loading document "${this.title}" from storage...`);
    this.simulateExpensiveLoad();
    this.content = `Full content of "${this.title}". This is a detailed document with ${metadata.size} bytes of data.`;
    console.log(`  [Line 45] Document "${this.title}" loaded successfully`);
  }

  private simulateExpensiveLoad(): void {
    // [Line 49] Simulate network/disk latency
    const start = Date.now();
    while (Date.now() - start < 100) {
      // Busy wait to simulate loading delay
    }
  }

  getTitle(): string {
    return this.title;
  }

  getContent(): string {
    return this.content;
  }

  setContent(content: string): void {
    this.content = content;
    console.log(`  [Line 64] Content updated for document "${this.title}"`);
  }

  getMetadata(): DocumentMetadata {
    return this.metadata;
  }
}

// =============================================================================
// VIRTUAL PROXY - Lazy Loading
// =============================================================================

// [Line 75] Virtual Proxy - Delays expensive object creation until needed
class VirtualDocumentProxy implements Document {
  private realDocument: RealDocument | null = null;
  private metadata: DocumentMetadata;

  constructor(metadata: DocumentMetadata) {
    this.metadata = metadata;
    console.log(`  [Line 82] Virtual proxy created for "${metadata.title}" (not loaded yet)`);
  }

  // [Line 85] Lazy initialization - creates real object only when needed
  private getRealDocument(): RealDocument {
    if (this.realDocument === null) {
      console.log(`  [Line 88] First access - initializing real document...`);
      this.realDocument = new RealDocument(this.metadata);
    }
    return this.realDocument;
  }

  getTitle(): string {
    // [Line 94] Title can be returned from metadata without loading full document
    return this.metadata.title;
  }

  getContent(): string {
    // [Line 99] Content requires full document loading
    console.log(`  [Line 99] Content requested - triggering lazy load`);
    return this.getRealDocument().getContent();
  }

  setContent(content: string): void {
    this.getRealDocument().setContent(content);
  }

  getMetadata(): DocumentMetadata {
    // [Line 108] Metadata available without loading full document
    return this.metadata;
  }
}

// =============================================================================
// PROTECTION PROXY - Access Control
// =============================================================================

// [Line 116] Protection Proxy - Controls access based on user permissions
class ProtectionDocumentProxy implements Document {
  private document: Document;
  private user: User;

  constructor(document: Document, user: User) {
    this.document = document;
    this.user = user;
    console.log(`  [Line 124] Protection proxy created for user "${user.name}" (${user.role})`);
  }

  // [Line 127] Check if user has read access
  private canRead(): boolean {
    const accessLevel = this.document.getMetadata().accessLevel;

    if (accessLevel === 'public') return true;
    if (accessLevel === 'internal' && this.user.role !== 'guest') return true;
    if (accessLevel === 'confidential' &&
        (this.user.role === 'manager' || this.user.role === 'admin')) return true;

    return false;
  }

  // [Line 138] Check if user has write access
  private canWrite(): boolean {
    return this.user.role === 'manager' || this.user.role === 'admin';
  }

  getTitle(): string {
    // [Line 144] Title is always accessible
    return this.document.getTitle();
  }

  getContent(): string {
    // [Line 149] Content requires read permission
    if (!this.canRead()) {
      const msg = `Access denied: User "${this.user.name}" cannot read confidential document`;
      console.log(`  [Line 151] ${msg}`);
      throw new Error(msg);
    }
    console.log(`  [Line 154] Access granted: User "${this.user.name}" reading document`);
    return this.document.getContent();
  }

  setContent(content: string): void {
    // [Line 159] Writing requires write permission
    if (!this.canWrite()) {
      const msg = `Access denied: User "${this.user.name}" (${this.user.role}) cannot modify document`;
      console.log(`  [Line 161] ${msg}`);
      throw new Error(msg);
    }
    console.log(`  [Line 164] Access granted: User "${this.user.name}" modifying document`);
    this.document.setContent(content);
  }

  getMetadata(): DocumentMetadata {
    return this.document.getMetadata();
  }
}

// =============================================================================
// LOGGING PROXY - Audit Trail
// =============================================================================

// [Line 176] Logging Proxy - Records all operations for audit trail
class LoggingDocumentProxy implements Document {
  private document: Document;
  private operationLog: string[] = [];

  constructor(document: Document) {
    this.document = document;
    this.log('Proxy initialized');
    console.log(`  [Line 184] Logging proxy created for "${document.getTitle()}"`);
  }

  // [Line 187] Log operation with timestamp
  private log(operation: string): void {
    const timestamp = new Date().toISOString();
    const entry = `[${timestamp}] ${operation}`;
    this.operationLog.push(entry);
  }

  getTitle(): string {
    this.log(`getTitle() called`);
    const result = this.document.getTitle();
    console.log(`  [Line 197] Logged: getTitle() -> "${result}"`);
    return result;
  }

  getContent(): string {
    this.log(`getContent() called`);
    const result = this.document.getContent();
    const preview = result.substring(0, 30) + '...';
    console.log(`  [Line 205] Logged: getContent() -> "${preview}"`);
    return result;
  }

  setContent(content: string): void {
    this.log(`setContent() called with ${content.length} characters`);
    console.log(`  [Line 211] Logged: setContent() with ${content.length} chars`);
    this.document.setContent(content);
  }

  getMetadata(): DocumentMetadata {
    this.log(`getMetadata() called`);
    return this.document.getMetadata();
  }

  // [Line 219] Get audit log for review
  getAuditLog(): string[] {
    return [...this.operationLog];
  }
}

// =============================================================================
// COMBINED PROXY - Demonstrates proxy chaining
// =============================================================================

// [Line 228] Document Management System - Factory for creating proxied documents
class DocumentManagementSystem {
  private documents: Map<string, DocumentMetadata> = new Map();

  constructor() {
    // [Line 233] Initialize with sample documents
    this.registerDocument({
      id: 'doc-001',
      title: 'Public Report',
      author: 'John Smith',
      createdAt: new Date('2024-01-15'),
      size: 15000,
      accessLevel: 'public'
    });

    this.registerDocument({
      id: 'doc-002',
      title: 'Internal Strategy',
      author: 'Jane Doe',
      createdAt: new Date('2024-02-20'),
      size: 45000,
      accessLevel: 'internal'
    });

    this.registerDocument({
      id: 'doc-003',
      title: 'Confidential Financials',
      author: 'CFO Office',
      createdAt: new Date('2024-03-10'),
      size: 120000,
      accessLevel: 'confidential'
    });
  }

  private registerDocument(metadata: DocumentMetadata): void {
    this.documents.set(metadata.id, metadata);
  }

  // [Line 263] Get document with all proxy layers
  getDocument(docId: string, user: User): Document | null {
    const metadata = this.documents.get(docId);
    if (!metadata) {
      console.log(`  [Line 266] Document "${docId}" not found`);
      return null;
    }

    console.log(`  [Line 270] Creating proxied document for "${metadata.title}"`);

    // [Line 272] Chain proxies: Virtual -> Protection -> Logging
    // Order matters: Logging wraps Protection wraps Virtual
    const virtualProxy = new VirtualDocumentProxy(metadata);
    const protectionProxy = new ProtectionDocumentProxy(virtualProxy, user);
    const loggingProxy = new LoggingDocumentProxy(protectionProxy);

    return loggingProxy;
  }

  listDocuments(): DocumentMetadata[] {
    return Array.from(this.documents.values());
  }
}

// =============================================================================
// DEMONSTRATION
// =============================================================================

function main(): void {
  console.log('='.repeat(70));
  console.log('[Line 289] PROXY DESIGN PATTERN DEMONSTRATION');
  console.log('='.repeat(70));

  // [Line 292] Create document management system
  console.log('\n[Line 293] Initializing Document Management System...\n');
  const dms = new DocumentManagementSystem();

  // [Line 296] Create test users with different roles
  const users: User[] = [
    { id: 'u1', name: 'Alice', role: 'guest' },
    { id: 'u2', name: 'Bob', role: 'employee' },
    { id: 'u3', name: 'Carol', role: 'manager' },
    { id: 'u4', name: 'Dave', role: 'admin' }
  ];

  // =========================================================================
  // Demo 1: Virtual Proxy - Lazy Loading
  // =========================================================================
  console.log('\n' + '='.repeat(70));
  console.log('[Line 308] DEMO 1: VIRTUAL PROXY - LAZY LOADING');
  console.log('='.repeat(70));

  console.log('\n[Line 311] Creating virtual proxy for document...');
  const metadata: DocumentMetadata = {
    id: 'test-001',
    title: 'Test Document',
    author: 'Test Author',
    createdAt: new Date(),
    size: 5000,
    accessLevel: 'public'
  };

  const virtualDoc = new VirtualDocumentProxy(metadata);

  console.log('\n[Line 323] Getting title (no loading required):');
  console.log(`  Result: "${virtualDoc.getTitle()}"`);

  console.log('\n[Line 326] Getting metadata (no loading required):');
  console.log(`  Result: Size = ${virtualDoc.getMetadata().size} bytes`);

  console.log('\n[Line 329] Getting content (triggers lazy loading):');
  const content = virtualDoc.getContent();
  console.log(`  Result: "${content.substring(0, 50)}..."`);

  console.log('\n[Line 333] Getting content again (already loaded):');
  virtualDoc.getContent();
  console.log('  Result: Retrieved from cached instance');

  // =========================================================================
  // Demo 2: Protection Proxy - Access Control
  // =========================================================================
  console.log('\n' + '='.repeat(70));
  console.log('[Line 341] DEMO 2: PROTECTION PROXY - ACCESS CONTROL');
  console.log('='.repeat(70));

  const manager = users[2]; // Carol - manager
  const employee = users[1]; // Bob - employee

  console.log('\n[Line 347] Testing access to confidential document...');

  // [Line 349] Manager accessing confidential document
  console.log(`\n[Line 350] Manager "${manager.name}" accessing confidential doc:`);
  const managerDoc = dms.getDocument('doc-003', manager);
  if (managerDoc) {
    try {
      const title = managerDoc.getTitle();
      console.log(`  Title: "${title}"`);
      managerDoc.getContent();
    } catch (e) {
      console.log(`  Error: ${(e as Error).message}`);
    }
  }

  // [Line 361] Employee attempting to access confidential document
  console.log(`\n[Line 362] Employee "${employee.name}" accessing confidential doc:`);
  const employeeDoc = dms.getDocument('doc-003', employee);
  if (employeeDoc) {
    try {
      const title = employeeDoc.getTitle();
      console.log(`  Title: "${title}"`);
      employeeDoc.getContent();
    } catch (e) {
      console.log(`  Error: ${(e as Error).message}`);
    }
  }

  // [Line 373] Employee accessing internal document (should work)
  console.log(`\n[Line 374] Employee "${employee.name}" accessing internal doc:`);
  const internalDoc = dms.getDocument('doc-002', employee);
  if (internalDoc) {
    try {
      const title = internalDoc.getTitle();
      console.log(`  Title: "${title}"`);
      internalDoc.getContent();
    } catch (e) {
      console.log(`  Error: ${(e as Error).message}`);
    }
  }

  // =========================================================================
  // Demo 3: Logging Proxy - Audit Trail
  // =========================================================================
  console.log('\n' + '='.repeat(70));
  console.log('[Line 390] DEMO 3: LOGGING PROXY - AUDIT TRAIL');
  console.log('='.repeat(70));

  console.log('\n[Line 393] Creating document with logging proxy...');
  const simpleMetadata: DocumentMetadata = {
    id: 'audit-001',
    title: 'Audited Document',
    author: 'Audit Team',
    createdAt: new Date(),
    size: 3000,
    accessLevel: 'public'
  };

  const realDoc = new RealDocument(simpleMetadata);
  const loggedDoc = new LoggingDocumentProxy(realDoc);

  console.log('\n[Line 406] Performing operations...');
  loggedDoc.getTitle();
  loggedDoc.getContent();
  loggedDoc.setContent('Updated content for audit trail demonstration');
  loggedDoc.getMetadata();

  console.log('\n[Line 412] Retrieving audit log:');
  const auditLog = loggedDoc.getAuditLog();
  auditLog.forEach((entry, index) => {
    console.log(`  ${index + 1}. ${entry}`);
  });

  // =========================================================================
  // Demo 4: Write Access Control
  // =========================================================================
  console.log('\n' + '='.repeat(70));
  console.log('[Line 422] DEMO 4: WRITE ACCESS CONTROL');
  console.log('='.repeat(70));

  const admin = users[3]; // Dave - admin
  const guest = users[0]; // Alice - guest

  console.log(`\n[Line 428] Admin "${admin.name}" modifying public document:`);
  const adminDoc = dms.getDocument('doc-001', admin);
  if (adminDoc) {
    try {
      adminDoc.setContent('New content added by admin');
      console.log('  Modification successful!');
    } catch (e) {
      console.log(`  Error: ${(e as Error).message}`);
    }
  }

  console.log(`\n[Line 439] Guest "${guest.name}" attempting to modify document:`);
  const guestDoc = dms.getDocument('doc-001', guest);
  if (guestDoc) {
    try {
      guestDoc.setContent('Unauthorized modification attempt');
      console.log('  Modification successful!');
    } catch (e) {
      console.log(`  Error: ${(e as Error).message}`);
    }
  }

  // =========================================================================
  // Summary
  // =========================================================================
  console.log('\n' + '='.repeat(70));
  console.log('[Line 454] PROXY PATTERN SUMMARY');
  console.log('='.repeat(70));
  console.log(`
Key Benefits Demonstrated:
1. Virtual Proxy: Deferred expensive operations until actually needed
2. Protection Proxy: Enforced access control without modifying real object
3. Logging Proxy: Added audit capabilities transparently
4. Proxy Chaining: Combined multiple proxy types for comprehensive control

The Proxy pattern allows us to control access to objects while maintaining
the same interface, enabling lazy loading, security, and monitoring.
`);
}

// [Line 467] Run the demonstration
main();
