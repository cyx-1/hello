# Chain of Responsibility Design Pattern in TypeScript

The Chain of Responsibility pattern passes a request along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain. This behavioral design pattern decouples the sender of a request from its receivers by giving multiple objects a chance to handle the request.

## Key Benefits

- **Decoupling**: The sender doesn't need to know which handler will process the request
- **Flexibility**: You can add or remove handlers dynamically
- **Single Responsibility**: Each handler focuses on one specific type of processing
- **Open/Closed**: New handlers can be added without modifying existing code

## Requirements

- Node.js 18+
- TypeScript 5.3+

## How to Run

```bash
npm install
npm run start
```

## Source Code

```typescript
1   /**
2    * Chain of Responsibility Design Pattern in TypeScript
3    *
4    * The Chain of Responsibility pattern passes a request along a chain of handlers.
5    * Each handler decides either to process the request or to pass it to the next
6    * handler in the chain. This decouples the sender from receivers and allows
7    * multiple objects to handle the request.
8    */
9
10  // ============================================================
11  // Example 1: Expense Approval System
12  // ============================================================
13
14  // Request interface
15  interface ExpenseRequest {
16      id: string;
17      description: string;
18      amount: number;
19      requester: string;
20  }
21
22  // Abstract Handler
23  abstract class ExpenseApprover {
24      protected nextApprover: ExpenseApprover | null = null;
25      protected approverName: string;
26      protected approvalLimit: number;
27
28      constructor(name: string, limit: number) {
29          this.approverName = name;
30          this.approvalLimit = limit;
31      }
32
33      setNext(approver: ExpenseApprover): ExpenseApprover {
34          this.nextApprover = approver;
35          return approver;
36      }
37
38      handle(request: ExpenseRequest): void {
39          console.log(`[Line 37] ${this.approverName}: Reviewing expense #${request.id} for $${request.amount}`);
40
41          if (request.amount <= this.approvalLimit) {
42              this.approve(request);
43          } else if (this.nextApprover) {
44              console.log(`[Line 42] ${this.approverName}: Amount exceeds my limit of $${this.approvalLimit}, escalating...`);
45              this.nextApprover.handle(request);
46          } else {
47              this.reject(request);
48          }
49      }
50
51      protected approve(request: ExpenseRequest): void {
52          console.log(`[Line 49] ${this.approverName}: APPROVED expense #${request.id} - "${request.description}" for $${request.amount}`);
53      }
54
55      protected reject(request: ExpenseRequest): void {
56          console.log(`[Line 53] ${this.approverName}: REJECTED expense #${request.id} - Amount $${request.amount} exceeds all approval limits`);
57      }
58  }
59
60  // Concrete Handlers
61  class TeamLead extends ExpenseApprover {
62      constructor() {
63          super("Team Lead", 500);
64          console.log("[Line 61] TeamLead: Initialized with approval limit of $500");
65      }
66  }
67
68  class Manager extends ExpenseApprover {
69      constructor() {
70          super("Manager", 2500);
71          console.log("[Line 68] Manager: Initialized with approval limit of $2,500");
72      }
73  }
74
75  class Director extends ExpenseApprover {
76      constructor() {
77          super("Director", 10000);
78          console.log("[Line 75] Director: Initialized with approval limit of $10,000");
79      }
80  }
81
82  class VicePresident extends ExpenseApprover {
83      constructor() {
84          super("Vice President", 50000);
85          console.log("[Line 82] VicePresident: Initialized with approval limit of $50,000");
86      }
87  }
88
89  class CEO extends ExpenseApprover {
90      constructor() {
91          super("CEO", 100000);
92          console.log("[Line 89] CEO: Initialized with approval limit of $100,000");
93      }
94  }
95
96  // ============================================================
97  // Example 2: Support Ticket Handling
98  // ============================================================
99
100 // Support ticket levels
101 enum TicketPriority {
102     LOW = "LOW",
103     MEDIUM = "MEDIUM",
104     HIGH = "HIGH",
105     CRITICAL = "CRITICAL"
106 }
107
108 interface SupportTicket {
109     id: string;
110     title: string;
111     priority: TicketPriority;
112     description: string;
113 }
114
115 // Abstract Handler for Support
116 abstract class SupportHandler {
117     protected nextHandler: SupportHandler | null = null;
118     protected handlerName: string;
119     protected handledPriorities: TicketPriority[];
120
121     constructor(name: string, priorities: TicketPriority[]) {
122         this.handlerName = name;
123         this.handledPriorities = priorities;
124     }
125
126     setNext(handler: SupportHandler): SupportHandler {
127         this.nextHandler = handler;
128         return handler;
129     }
130
131     handle(ticket: SupportTicket): void {
132         console.log(`[Line 126] ${this.handlerName}: Received ticket #${ticket.id} [${ticket.priority}] - "${ticket.title}"`);
133
134         if (this.canHandle(ticket)) {
135             this.processTicket(ticket);
136         } else if (this.nextHandler) {
137             console.log(`[Line 131] ${this.handlerName}: Cannot handle ${ticket.priority} priority, passing to next level...`);
138             this.nextHandler.handle(ticket);
139         } else {
140             console.log(`[Line 134] ${this.handlerName}: No handler available for ticket #${ticket.id}`);
141         }
142     }
143
144     protected canHandle(ticket: SupportTicket): boolean {
145         return this.handledPriorities.includes(ticket.priority);
146     }
147
148     protected abstract processTicket(ticket: SupportTicket): void;
149 }
150
151 // Concrete Support Handlers
152 class HelpDesk extends SupportHandler {
153     constructor() {
154         super("Help Desk", [TicketPriority.LOW]);
155         console.log("[Line 149] HelpDesk: Initialized to handle LOW priority tickets");
156     }
157
158     protected processTicket(ticket: SupportTicket): void {
159         console.log(`[Line 153] HelpDesk: RESOLVED ticket #${ticket.id} - Basic support provided for "${ticket.title}"`);
160     }
161 }
162
163 class TechnicalSupport extends SupportHandler {
164     constructor() {
165         super("Technical Support", [TicketPriority.MEDIUM]);
166         console.log("[Line 160] TechnicalSupport: Initialized to handle MEDIUM priority tickets");
167     }
168
169     protected processTicket(ticket: SupportTicket): void {
170         console.log(`[Line 164] TechnicalSupport: RESOLVED ticket #${ticket.id} - Technical investigation completed for "${ticket.title}"`);
171     }
172 }
173
174 class SeniorEngineer extends SupportHandler {
175     constructor() {
176         super("Senior Engineer", [TicketPriority.HIGH]);
177         console.log("[Line 171] SeniorEngineer: Initialized to handle HIGH priority tickets");
178     }
179
180     protected processTicket(ticket: SupportTicket): void {
181         console.log(`[Line 175] SeniorEngineer: RESOLVED ticket #${ticket.id} - Expert analysis completed for "${ticket.title}"`);
182     }
183 }
184
185 class EmergencyTeam extends SupportHandler {
186     constructor() {
187         super("Emergency Team", [TicketPriority.CRITICAL]);
188         console.log("[Line 182] EmergencyTeam: Initialized to handle CRITICAL priority tickets");
189     }
190
191     protected processTicket(ticket: SupportTicket): void {
192         console.log(`[Line 186] EmergencyTeam: EMERGENCY RESPONSE for ticket #${ticket.id} - Immediate action taken for "${ticket.title}"`);
193     }
194 }
195
196 // ============================================================
197 // Example 3: Authentication Middleware Chain
198 // ============================================================
199
200 interface AuthRequest {
201     userId: string;
202     token: string;
203     role: string;
204     ipAddress: string;
205     resource: string;
206 }
207
208 interface AuthResult {
209     success: boolean;
210     message: string;
211 }
212
213 abstract class AuthMiddleware {
214     protected next: AuthMiddleware | null = null;
215     protected middlewareName: string;
216
217     constructor(name: string) {
218         this.middlewareName = name;
219     }
220
221     setNext(middleware: AuthMiddleware): AuthMiddleware {
222         this.next = middleware;
223         return middleware;
224     }
225
226     handle(request: AuthRequest): AuthResult {
227         console.log(`[Line 219] ${this.middlewareName}: Processing request from user "${request.userId}"`);
228
229         const result = this.check(request);
230         if (!result.success) {
231             console.log(`[Line 223] ${this.middlewareName}: BLOCKED - ${result.message}`);
232             return result;
233         }
234
235         console.log(`[Line 227] ${this.middlewareName}: PASSED - ${result.message}`);
236
237         if (this.next) {
238             return this.next.handle(request);
239         }
240
241         return { success: true, message: "All authentication checks passed" };
242     }
243
244     protected abstract check(request: AuthRequest): AuthResult;
245 }
246
247 // Concrete Authentication Middleware
248 class IPWhitelistMiddleware extends AuthMiddleware {
249     private whitelist: string[] = ["192.168.1.1", "10.0.0.1", "127.0.0.1"];
250
251     constructor() {
252         super("IP Whitelist");
253         console.log("[Line 244] IPWhitelistMiddleware: Initialized with whitelist");
254     }
255
256     protected check(request: AuthRequest): AuthResult {
257         if (this.whitelist.includes(request.ipAddress)) {
258             return { success: true, message: `IP ${request.ipAddress} is whitelisted` };
259         }
260         return { success: false, message: `IP ${request.ipAddress} is not in whitelist` };
261     }
262 }
263
264 class TokenValidationMiddleware extends AuthMiddleware {
265     constructor() {
266         super("Token Validation");
267         console.log("[Line 258] TokenValidationMiddleware: Initialized");
268     }
269
270     protected check(request: AuthRequest): AuthResult {
271         if (request.token && request.token.startsWith("valid-")) {
272             return { success: true, message: "Token is valid" };
273         }
274         return { success: false, message: "Invalid or expired token" };
275     }
276 }
277
278 class RoleAuthorizationMiddleware extends AuthMiddleware {
279     private resourcePermissions: Map<string, string[]> = new Map([
280         ["admin-panel", ["admin"]],
281         ["user-data", ["admin", "manager"]],
282         ["public-api", ["admin", "manager", "user"]]
283     ]);
284
285     constructor() {
286         super("Role Authorization");
287         console.log("[Line 278] RoleAuthorizationMiddleware: Initialized with role permissions");
288     }
289
290     protected check(request: AuthRequest): AuthResult {
291         const allowedRoles = this.resourcePermissions.get(request.resource);
292         if (!allowedRoles) {
293             return { success: true, message: `Resource "${request.resource}" has no restrictions` };
294         }
295         if (allowedRoles.includes(request.role)) {
296             return { success: true, message: `Role "${request.role}" authorized for "${request.resource}"` };
297         }
298         return { success: false, message: `Role "${request.role}" not authorized for "${request.resource}"` };
299     }
300 }
301
302 class RateLimitMiddleware extends AuthMiddleware {
303     private requestCounts: Map<string, number> = new Map();
304     private limit: number = 100;
305
306     constructor() {
307         super("Rate Limiter");
308         console.log("[Line 298] RateLimitMiddleware: Initialized with limit of 100 requests");
309     }
310
311     protected check(request: AuthRequest): AuthResult {
312         const count = this.requestCounts.get(request.userId) || 0;
313         if (count >= this.limit) {
314             return { success: false, message: `Rate limit exceeded for user "${request.userId}"` };
315         }
316         this.requestCounts.set(request.userId, count + 1);
317         return { success: true, message: `Request count: ${count + 1}/${this.limit}` };
318     }
319 }
```

## Program Output

```
=== Chain of Responsibility Pattern Demonstration ===

--- Demo 1: Expense Approval System ---

Setting up approval chain...

[Line 61] TeamLead: Initialized with approval limit of $500
[Line 68] Manager: Initialized with approval limit of $2,500
[Line 75] Director: Initialized with approval limit of $10,000
[Line 82] VicePresident: Initialized with approval limit of $50,000
[Line 89] CEO: Initialized with approval limit of $100,000

[Line 329] Chain established: Team Lead -> Manager -> Director -> VP -> CEO

Processing expense from Alice:
[Line 37] Team Lead: Reviewing expense #EXP-001 for $250
[Line 49] Team Lead: APPROVED expense #EXP-001 - "Office supplies" for $250

Processing expense from Bob:
[Line 37] Team Lead: Reviewing expense #EXP-002 for $800
[Line 42] Team Lead: Amount exceeds my limit of $500, escalating...
[Line 37] Manager: Reviewing expense #EXP-002 for $800
[Line 49] Manager: APPROVED expense #EXP-002 - "Team lunch" for $800

Processing expense from Charlie:
[Line 37] Team Lead: Reviewing expense #EXP-003 for $5000
[Line 42] Team Lead: Amount exceeds my limit of $500, escalating...
[Line 37] Manager: Reviewing expense #EXP-003 for $5000
[Line 42] Manager: Amount exceeds my limit of $2500, escalating...
[Line 37] Director: Reviewing expense #EXP-003 for $5000
[Line 49] Director: APPROVED expense #EXP-003 - "Conference tickets" for $5000

Processing expense from Diana:
[Line 37] Team Lead: Reviewing expense #EXP-004 for $25000
[Line 42] Team Lead: Amount exceeds my limit of $500, escalating...
[Line 37] Manager: Reviewing expense #EXP-004 for $25000
[Line 42] Manager: Amount exceeds my limit of $2500, escalating...
[Line 37] Director: Reviewing expense #EXP-004 for $25000
[Line 42] Director: Amount exceeds my limit of $10000, escalating...
[Line 37] Vice President: Reviewing expense #EXP-004 for $25000
[Line 49] Vice President: APPROVED expense #EXP-004 - "Server upgrade" for $25000

Processing expense from Eve:
[Line 37] Team Lead: Reviewing expense #EXP-005 for $75000
[Line 42] Team Lead: Amount exceeds my limit of $500, escalating...
[Line 37] Manager: Reviewing expense #EXP-005 for $75000
[Line 42] Manager: Amount exceeds my limit of $2500, escalating...
[Line 37] Director: Reviewing expense #EXP-005 for $75000
[Line 42] Director: Amount exceeds my limit of $10000, escalating...
[Line 37] Vice President: Reviewing expense #EXP-005 for $75000
[Line 42] Vice President: Amount exceeds my limit of $50000, escalating...
[Line 37] CEO: Reviewing expense #EXP-005 for $75000
[Line 49] CEO: APPROVED expense #EXP-005 - "Office renovation" for $75000

Processing expense from Frank:
[Line 37] Team Lead: Reviewing expense #EXP-006 for $150000
[Line 42] Team Lead: Amount exceeds my limit of $500, escalating...
[Line 37] Manager: Reviewing expense #EXP-006 for $150000
[Line 42] Manager: Amount exceeds my limit of $2500, escalating...
[Line 37] Director: Reviewing expense #EXP-006 for $150000
[Line 42] Director: Amount exceeds my limit of $10000, escalating...
[Line 37] Vice President: Reviewing expense #EXP-006 for $150000
[Line 42] Vice President: Amount exceeds my limit of $50000, escalating...
[Line 37] CEO: Reviewing expense #EXP-006 for $150000
[Line 53] CEO: REJECTED expense #EXP-006 - Amount $150000 exceeds all approval limits


--- Demo 2: Support Ticket Handling ---

Setting up support chain...

[Line 149] HelpDesk: Initialized to handle LOW priority tickets
[Line 160] TechnicalSupport: Initialized to handle MEDIUM priority tickets
[Line 171] SeniorEngineer: Initialized to handle HIGH priority tickets
[Line 182] EmergencyTeam: Initialized to handle CRITICAL priority tickets

[Line 356] Chain established: Help Desk -> Tech Support -> Senior Engineer -> Emergency Team

Processing ticket from queue:
[Line 126] Help Desk: Received ticket #TKT-001 [LOW] - "Password reset"
[Line 153] HelpDesk: RESOLVED ticket #TKT-001 - Basic support provided for "Password reset"

Processing ticket from queue:
[Line 126] Help Desk: Received ticket #TKT-002 [MEDIUM] - "Slow application"
[Line 131] Help Desk: Cannot handle MEDIUM priority, passing to next level...
[Line 126] Technical Support: Received ticket #TKT-002 [MEDIUM] - "Slow application"
[Line 164] TechnicalSupport: RESOLVED ticket #TKT-002 - Technical investigation completed for "Slow application"

Processing ticket from queue:
[Line 126] Help Desk: Received ticket #TKT-003 [HIGH] - "Data corruption"
[Line 131] Help Desk: Cannot handle HIGH priority, passing to next level...
[Line 126] Technical Support: Received ticket #TKT-003 [HIGH] - "Data corruption"
[Line 131] Technical Support: Cannot handle HIGH priority, passing to next level...
[Line 126] Senior Engineer: Received ticket #TKT-003 [HIGH] - "Data corruption"
[Line 175] SeniorEngineer: RESOLVED ticket #TKT-003 - Expert analysis completed for "Data corruption"

Processing ticket from queue:
[Line 126] Help Desk: Received ticket #TKT-004 [CRITICAL] - "System outage"
[Line 131] Help Desk: Cannot handle CRITICAL priority, passing to next level...
[Line 126] Technical Support: Received ticket #TKT-004 [CRITICAL] - "System outage"
[Line 131] Technical Support: Cannot handle CRITICAL priority, passing to next level...
[Line 126] Senior Engineer: Received ticket #TKT-004 [CRITICAL] - "System outage"
[Line 131] Senior Engineer: Cannot handle CRITICAL priority, passing to next level...
[Line 126] Emergency Team: Received ticket #TKT-004 [CRITICAL] - "System outage"
[Line 186] EmergencyTeam: EMERGENCY RESPONSE for ticket #TKT-004 - Immediate action taken for "System outage"


--- Demo 3: Authentication Middleware Chain ---

Setting up authentication middleware...

[Line 244] IPWhitelistMiddleware: Initialized with whitelist
[Line 258] TokenValidationMiddleware: Initialized
[Line 278] RoleAuthorizationMiddleware: Initialized with role permissions
[Line 298] RateLimitMiddleware: Initialized with limit of 100 requests

[Line 382] Chain established: IP Whitelist -> Token Validation -> Role Authorization -> Rate Limiter

[Line 393] Auth Request 1: User "user1" accessing "admin-panel"
[Line 219] IP Whitelist: Processing request from user "user1"
[Line 227] IP Whitelist: PASSED - IP 192.168.1.1 is whitelisted
[Line 219] Token Validation: Processing request from user "user1"
[Line 227] Token Validation: PASSED - Token is valid
[Line 219] Role Authorization: Processing request from user "user1"
[Line 227] Role Authorization: PASSED - Role "admin" authorized for "admin-panel"
[Line 219] Rate Limiter: Processing request from user "user1"
[Line 227] Rate Limiter: PASSED - Request count: 1/100
[Line 395] Final Result: ACCESS GRANTED - All authentication checks passed

[Line 393] Auth Request 2: User "user2" accessing "admin-panel"
[Line 219] IP Whitelist: Processing request from user "user2"
[Line 227] IP Whitelist: PASSED - IP 127.0.0.1 is whitelisted
[Line 219] Token Validation: Processing request from user "user2"
[Line 227] Token Validation: PASSED - Token is valid
[Line 219] Role Authorization: Processing request from user "user2"
[Line 223] Role Authorization: BLOCKED - Role "user" not authorized for "admin-panel"
[Line 395] Final Result: ACCESS DENIED - Role "user" not authorized for "admin-panel"

[Line 393] Auth Request 3: User "user3" accessing "user-data"
[Line 219] IP Whitelist: Processing request from user "user3"
[Line 227] IP Whitelist: PASSED - IP 10.0.0.1 is whitelisted
[Line 219] Token Validation: Processing request from user "user3"
[Line 223] Token Validation: BLOCKED - Invalid or expired token
[Line 395] Final Result: ACCESS DENIED - Invalid or expired token

[Line 393] Auth Request 4: User "user4" accessing "public-api"
[Line 219] IP Whitelist: Processing request from user "user4"
[Line 223] IP Whitelist: BLOCKED - IP 8.8.8.8 is not in whitelist
[Line 395] Final Result: ACCESS DENIED - IP 8.8.8.8 is not in whitelist

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### 1. Handler Interface/Abstract Class
Defines the interface for handling requests and maintains a reference to the next handler.

| Component | Lines | Purpose |
|-----------|-------|---------|
| `ExpenseApprover` | 23-58 | Abstract handler for expense approval chain |
| `SupportHandler` | 116-149 | Abstract handler for support ticket chain |
| `AuthMiddleware` | 213-245 | Abstract handler for authentication middleware chain |

#### 2. Concrete Handlers
Implement the actual request handling logic.

| Handler Class | Lines | Responsibility |
|---------------|-------|----------------|
| `TeamLead` | 61-66 | Approves expenses up to $500 |
| `Manager` | 68-73 | Approves expenses up to $2,500 |
| `Director` | 75-80 | Approves expenses up to $10,000 |
| `VicePresident` | 82-87 | Approves expenses up to $50,000 |
| `CEO` | 89-94 | Approves expenses up to $100,000 |
| `HelpDesk` | 152-161 | Handles LOW priority tickets |
| `TechnicalSupport` | 163-172 | Handles MEDIUM priority tickets |
| `SeniorEngineer` | 174-183 | Handles HIGH priority tickets |
| `EmergencyTeam` | 185-194 | Handles CRITICAL priority tickets |
| `IPWhitelistMiddleware` | 248-262 | Validates IP addresses |
| `TokenValidationMiddleware` | 264-276 | Validates authentication tokens |
| `RoleAuthorizationMiddleware` | 278-300 | Checks role-based permissions |
| `RateLimitMiddleware` | 302-319 | Enforces rate limiting |

### Output Correlation

#### Expense Approval System

| Output Message | Source Line | Explanation |
|----------------|-------------|-------------|
| `TeamLead: Initialized with approval limit of $500` | Line 61 | Handler construction logging |
| `Team Lead: Reviewing expense #EXP-001 for $250` | Line 37 | Handle method entry point |
| `Team Lead: APPROVED expense #EXP-001` | Line 49 | Request processed by first handler |
| `Team Lead: Amount exceeds my limit of $500, escalating...` | Line 42 | Request passed to next handler |
| `Manager: APPROVED expense #EXP-002` | Line 49 | Request processed by second handler |
| `CEO: REJECTED expense #EXP-006` | Line 53 | No handler in chain can process request |

#### Support Ticket Handling

| Output Message | Source Line | Explanation |
|----------------|-------------|-------------|
| `HelpDesk: Initialized to handle LOW priority tickets` | Line 149 | Handler announces its capability |
| `Help Desk: Received ticket #TKT-001 [LOW]` | Line 126 | Ticket received by handler |
| `Help Desk: Cannot handle MEDIUM priority, passing to next level...` | Line 131 | Handler delegates to next |
| `TechnicalSupport: RESOLVED ticket #TKT-002` | Line 164 | Appropriate handler processes ticket |
| `EmergencyTeam: EMERGENCY RESPONSE for ticket #TKT-004` | Line 186 | Critical ticket handled by specialized team |

#### Authentication Middleware

| Output Message | Source Line | Explanation |
|----------------|-------------|-------------|
| `IP Whitelist: Processing request from user "user1"` | Line 219 | Middleware receives request |
| `IP Whitelist: PASSED - IP 192.168.1.1 is whitelisted` | Line 227 | Check succeeded, continues chain |
| `Role Authorization: BLOCKED - Role "user" not authorized` | Line 223 | Check failed, chain stops |
| `Final Result: ACCESS GRANTED - All authentication checks passed` | Line 395 | All middleware passed |

### Chain Flow Analysis

#### Example: EXP-003 ($5,000 Conference Tickets)

| Step | Handler | Action | Result |
|------|---------|--------|--------|
| 1 | Team Lead | Check if $5,000 <= $500 | NO - escalate |
| 2 | Manager | Check if $5,000 <= $2,500 | NO - escalate |
| 3 | Director | Check if $5,000 <= $10,000 | YES - approve |

#### Example: TKT-004 (CRITICAL System Outage)

| Step | Handler | Action | Result |
|------|---------|--------|--------|
| 1 | Help Desk | Check if CRITICAL in [LOW] | NO - pass |
| 2 | Technical Support | Check if CRITICAL in [MEDIUM] | NO - pass |
| 3 | Senior Engineer | Check if CRITICAL in [HIGH] | NO - pass |
| 4 | Emergency Team | Check if CRITICAL in [CRITICAL] | YES - process |

#### Example: Auth Request 2 (user2 accessing admin-panel)

| Step | Middleware | Check | Result |
|------|------------|-------|--------|
| 1 | IP Whitelist | 127.0.0.1 in whitelist | PASS |
| 2 | Token Validation | Token starts with "valid-" | PASS |
| 3 | Role Authorization | "user" role for "admin-panel" | BLOCKED |
| - | (chain stops) | - | ACCESS DENIED |

### Key Implementation Details

#### Chain Building (Lines 33-36, 126-129, 221-224)
The `setNext()` method returns the next handler, enabling fluent chain construction:
```typescript
teamLead.setNext(manager).setNext(director).setNext(vp).setNext(ceo);
```

#### Decision Logic Variations

1. **Expense Approval** (Lines 41-48): Amount-based threshold checking
2. **Support Tickets** (Lines 134-141): Priority-based capability matching
3. **Auth Middleware** (Lines 229-241): Pass/fail pipeline with early termination

### Design Pattern Characteristics Demonstrated

1. **Loose Coupling**: Client only knows about the first handler in the chain
2. **Single Responsibility**: Each handler has one specific criteria to check
3. **Open/Closed Principle**: New handlers can be added without modifying existing code
4. **Runtime Flexibility**: Chain can be assembled dynamically at runtime

### Use Cases

- **Expense/Purchase Approval**: Multi-level approval workflows
- **Support Escalation**: Ticket routing based on severity
- **Authentication/Authorization**: Security middleware pipelines
- **Event Processing**: Multiple listeners for event handling
- **Logging**: Different log levels to different destinations
- **Input Validation**: Sequential validation checks
