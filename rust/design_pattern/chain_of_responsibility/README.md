# Chain of Responsibility Design Pattern in Rust

The Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

This implementation demonstrates a **Support Ticket Authentication and Authorization System** where requests must pass through multiple validation stages: authentication, role authorization, priority validation, and finally ticket processing.

## Source Code

```rust
  1  // Chain of Responsibility Design Pattern in Rust
  2  // Example: Support Ticket Authentication and Authorization System
  3
  4  use std::cell::RefCell;
  5  use std::rc::Rc;
  6
  7  // Request structure representing a support ticket with authentication info
  8  #[derive(Clone, Debug)]
  9  struct SupportRequest {
 10      user_id: String,
 11      password: String,
 12      role: String,
 13      ticket_priority: String,
 14      description: String,
 15  }
 16
 17  impl SupportRequest {
 18      fn new(user_id: &str, password: &str, role: &str, priority: &str, desc: &str) -> Self {
 19          SupportRequest {
 20              user_id: user_id.to_string(),
 21              password: password.to_string(),
 22              role: role.to_string(),
 23              ticket_priority: priority.to_string(),
 24              description: desc.to_string(),
 25          }
 26      }
 27  }
 28
 29  // Handler trait defining the chain interface
 30  trait Handler {
 31      fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>);
 32      fn handle(&self, request: &SupportRequest) -> bool;
 33  }
 34
 35  // Base handler with common chain functionality
 36  struct BaseHandler {
 37      next: Option<Rc<RefCell<dyn Handler>>>,
 38  }
 39
 40  impl BaseHandler {
 41      fn new() -> Self {
 42          BaseHandler { next: None }
 43      }
 44
 45      fn handle_next(&self, request: &SupportRequest) -> bool {
 46          if let Some(ref next_handler) = self.next {
 47              return next_handler.borrow().handle(request);
 48          }
 49          println!("  [Chain End] Request processed successfully!");
 50          true
 51      }
 52  }
 53
 54  // Concrete Handler 1: Authentication Handler
 55  struct AuthenticationHandler {
 56      base: BaseHandler,
 57      valid_credentials: Vec<(String, String)>,
 58  }
 59
 60  impl AuthenticationHandler {
 61      fn new() -> Self {
 62          let mut handler = AuthenticationHandler {
 63              base: BaseHandler::new(),
 64              valid_credentials: Vec::new(),
 65          };
 66          // Add some valid credentials
 67          handler.valid_credentials.push(("admin".to_string(), "admin123".to_string()));
 68          handler.valid_credentials.push(("user1".to_string(), "pass123".to_string()));
 69          handler.valid_credentials.push(("support".to_string(), "support456".to_string()));
 70          handler
 71      }
 72  }
 73
 74  impl Handler for AuthenticationHandler {
 75      fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>) {
 76          self.base.next = Some(handler);
 77      }
 78
 79      fn handle(&self, request: &SupportRequest) -> bool {
 80          println!("  [AuthenticationHandler] Checking credentials for user: {}", request.user_id);
 81
 82          let is_valid = self.valid_credentials.iter()
 83              .any(|(user, pass)| user == &request.user_id && pass == &request.password);
 84
 85          if is_valid {
 86              println!("  [AuthenticationHandler] Authentication successful!");
 87              self.base.handle_next(request)
 88          } else {
 89              println!("  [AuthenticationHandler] Authentication FAILED - Invalid credentials");
 90              false
 91          }
 92      }
 93  }
 94
 95  // Concrete Handler 2: Role Authorization Handler
 96  struct RoleAuthorizationHandler {
 97      base: BaseHandler,
 98      allowed_roles: Vec<String>,
 99  }
100
101  impl RoleAuthorizationHandler {
102      fn new() -> Self {
103          let mut handler = RoleAuthorizationHandler {
104              base: BaseHandler::new(),
105              allowed_roles: Vec::new(),
106          };
107          handler.allowed_roles.push("admin".to_string());
108          handler.allowed_roles.push("support_agent".to_string());
109          handler.allowed_roles.push("premium_user".to_string());
110          handler
111      }
112  }
113
114  impl Handler for RoleAuthorizationHandler {
115      fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>) {
116          self.base.next = Some(handler);
117      }
118
119      fn handle(&self, request: &SupportRequest) -> bool {
120          println!("  [RoleAuthorizationHandler] Checking role: {}", request.role);
121
122          if self.allowed_roles.contains(&request.role) {
123              println!("  [RoleAuthorizationHandler] Role '{}' is authorized!", request.role);
124              self.base.handle_next(request)
125          } else {
126              println!("  [RoleAuthorizationHandler] Role '{}' is NOT authorized", request.role);
127              false
128          }
129      }
130  }
131
132  // Concrete Handler 3: Priority Handler (checks if user can submit priority tickets)
133  struct PriorityHandler {
134      base: BaseHandler,
135  }
136
137  impl PriorityHandler {
138      fn new() -> Self {
139          PriorityHandler {
140              base: BaseHandler::new(),
141          }
142      }
143  }
144
145  impl Handler for PriorityHandler {
146      fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>) {
147          self.base.next = Some(handler);
148      }
149
150      fn handle(&self, request: &SupportRequest) -> bool {
151          println!("  [PriorityHandler] Checking ticket priority: {}", request.ticket_priority);
152
153          // Only admin and support_agent can submit critical tickets
154          let can_submit_critical = request.role == "admin" || request.role == "support_agent";
155
156          if request.ticket_priority == "critical" && !can_submit_critical {
157              println!("  [PriorityHandler] Only admin/support can submit critical tickets");
158              false
159          } else {
160              println!("  [PriorityHandler] Priority level '{}' approved!", request.ticket_priority);
161              self.base.handle_next(request)
162          }
163      }
164  }
165
166  // Concrete Handler 4: Ticket Processing Handler (final handler)
167  struct TicketProcessingHandler {
168      base: BaseHandler,
169  }
170
171  impl TicketProcessingHandler {
172      fn new() -> Self {
173          TicketProcessingHandler {
174              base: BaseHandler::new(),
175          }
176      }
177  }
178
179  impl Handler for TicketProcessingHandler {
180      fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>) {
181          self.base.next = Some(handler);
182      }
183
184      fn handle(&self, request: &SupportRequest) -> bool {
185          println!("  [TicketProcessingHandler] Processing ticket: '{}'", request.description);
186          println!("  [TicketProcessingHandler] Ticket created successfully for user '{}'", request.user_id);
187          self.base.handle_next(request)
188      }
189  }
190
191  // Helper function to build the handler chain
192  fn build_handler_chain() -> Rc<RefCell<dyn Handler>> {
193      let auth_handler = Rc::new(RefCell::new(AuthenticationHandler::new()));
194      let role_handler = Rc::new(RefCell::new(RoleAuthorizationHandler::new()));
195      let priority_handler = Rc::new(RefCell::new(PriorityHandler::new()));
196      let ticket_handler = Rc::new(RefCell::new(TicketProcessingHandler::new()));
197
198      // Build the chain: Auth -> Role -> Priority -> Ticket
199      priority_handler.borrow_mut().set_next(ticket_handler);
200      role_handler.borrow_mut().set_next(priority_handler);
201      auth_handler.borrow_mut().set_next(role_handler);
202
203      auth_handler
204  }
205
206  fn main() {
207      println!("=== Chain of Responsibility Pattern Demo ===");
208      println!("Support Ticket Authentication & Authorization System\n");
209
210      // Build the handler chain
211      let handler_chain = build_handler_chain();
212
213      // Test Case 1: Successful request from admin
214      println!("--- Test 1: Admin submitting critical ticket ---");
215      let request1 = SupportRequest::new(
216          "admin",
217          "admin123",
218          "admin",
219          "critical",
220          "Server outage in production"
221      );
222      let result1 = handler_chain.borrow().handle(&request1);
223      println!("Result: {}\n", if result1 { "SUCCESS" } else { "FAILED" });
224
225      // Test Case 2: Authentication failure
226      println!("--- Test 2: Invalid credentials ---");
227      let request2 = SupportRequest::new(
228          "hacker",
229          "wrongpass",
230          "admin",
231          "low",
232          "Suspicious request"
233      );
234      let result2 = handler_chain.borrow().handle(&request2);
235      println!("Result: {}\n", if result2 { "SUCCESS" } else { "FAILED" });
236
237      // Test Case 3: Role authorization failure
238      println!("--- Test 3: Unauthorized role ---");
239      let request3 = SupportRequest::new(
240          "user1",
241          "pass123",
242          "guest",
243          "medium",
244          "Need help with login"
245      );
246      let result3 = handler_chain.borrow().handle(&request3);
247      println!("Result: {}\n", if result3 { "SUCCESS" } else { "FAILED" });
248
249      // Test Case 4: Priority check failure
250      println!("--- Test 4: Premium user trying critical priority ---");
251      let request4 = SupportRequest::new(
252          "support",
253          "support456",
254          "premium_user",
255          "critical",
256          "Urgent billing issue"
257      );
258      let result4 = handler_chain.borrow().handle(&request4);
259      println!("Result: {}\n", if result4 { "SUCCESS" } else { "FAILED" });
260
261      // Test Case 5: Successful request from support agent
262      println!("--- Test 5: Support agent with normal priority ---");
263      let request5 = SupportRequest::new(
264          "support",
265          "support456",
266          "support_agent",
267          "high",
268          "Customer escalation"
269      );
270      let result5 = handler_chain.borrow().handle(&request5);
271      println!("Result: {}\n", if result5 { "SUCCESS" } else { "FAILED" });
272
273      println!("=== Demo Complete ===");
274  }
```

## Program Output

```
=== Chain of Responsibility Pattern Demo ===
Support Ticket Authentication & Authorization System

--- Test 1: Admin submitting critical ticket ---
  [AuthenticationHandler] Checking credentials for user: admin
  [AuthenticationHandler] Authentication successful!
  [RoleAuthorizationHandler] Checking role: admin
  [RoleAuthorizationHandler] Role 'admin' is authorized!
  [PriorityHandler] Checking ticket priority: critical
  [PriorityHandler] Priority level 'critical' approved!
  [TicketProcessingHandler] Processing ticket: 'Server outage in production'
  [TicketProcessingHandler] Ticket created successfully for user 'admin'
  [Chain End] Request processed successfully!
Result: SUCCESS

--- Test 2: Invalid credentials ---
  [AuthenticationHandler] Checking credentials for user: hacker
  [AuthenticationHandler] Authentication FAILED - Invalid credentials
Result: FAILED

--- Test 3: Unauthorized role ---
  [AuthenticationHandler] Checking credentials for user: user1
  [AuthenticationHandler] Authentication successful!
  [RoleAuthorizationHandler] Checking role: guest
  [RoleAuthorizationHandler] Role 'guest' is NOT authorized
Result: FAILED

--- Test 4: Premium user trying critical priority ---
  [AuthenticationHandler] Checking credentials for user: support
  [AuthenticationHandler] Authentication successful!
  [RoleAuthorizationHandler] Checking role: premium_user
  [RoleAuthorizationHandler] Role 'premium_user' is authorized!
  [PriorityHandler] Checking ticket priority: critical
  [PriorityHandler] Only admin/support can submit critical tickets
Result: FAILED

--- Test 5: Support agent with normal priority ---
  [AuthenticationHandler] Checking credentials for user: support
  [AuthenticationHandler] Authentication successful!
  [RoleAuthorizationHandler] Checking role: support_agent
  [RoleAuthorizationHandler] Role 'support_agent' is authorized!
  [PriorityHandler] Checking ticket priority: high
  [PriorityHandler] Priority level 'high' approved!
  [TicketProcessingHandler] Processing ticket: 'Customer escalation'
  [TicketProcessingHandler] Ticket created successfully for user 'support'
  [Chain End] Request processed successfully!
Result: SUCCESS

=== Demo Complete ===
```

## Code Annotations

### Key Sections Explained

#### Lines 4-5: Smart Pointer Imports
```rust
use std::cell::RefCell;
use std::rc::Rc;
```
These are essential for the Chain of Responsibility pattern in Rust. `Rc` (Reference Counted) allows multiple ownership of handlers, while `RefCell` enables interior mutability for runtime borrow checking.

#### Lines 7-27: Request Structure
The `SupportRequest` struct encapsulates all data needed for processing: user credentials, role, ticket priority, and description. This is the object that passes through the entire chain.

#### Lines 29-33: Handler Trait
```rust
trait Handler {
    fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>);
    fn handle(&self, request: &SupportRequest) -> bool;
}
```
The core abstraction defining two key methods:
- `set_next`: Links handlers together in a chain
- `handle`: Processes the request and decides whether to continue

#### Lines 35-52: BaseHandler
Contains the common chain traversal logic. The `handle_next` method (lines 45-51) either forwards to the next handler or marks the end of the chain successfully.

#### Lines 54-93: AuthenticationHandler
First handler in the chain that validates user credentials against a whitelist. On failure (line 89-90), it stops the chain by returning `false`.

#### Lines 95-130: RoleAuthorizationHandler
Second handler that checks if the user's role is in the allowed roles list. Demonstrates how each handler has its own validation logic.

#### Lines 132-164: PriorityHandler
Third handler implementing business logic: only admin and support_agent roles can submit critical tickets. Shows conditional validation based on multiple fields.

#### Lines 166-189: TicketProcessingHandler
Final handler that performs the actual ticket creation. In a real system, this would persist data to a database.

#### Lines 191-204: Chain Construction
```rust
fn build_handler_chain() -> Rc<RefCell<dyn Handler>> {
    // ...
    priority_handler.borrow_mut().set_next(ticket_handler);
    role_handler.borrow_mut().set_next(priority_handler);
    auth_handler.borrow_mut().set_next(role_handler);
    auth_handler
}
```
Builds the chain in reverse order (from last to first) and returns the head of the chain.

### Output to Source Code Correlation

| Output | Source Lines | Description |
|--------|--------------|-------------|
| `[AuthenticationHandler] Checking credentials...` | 80 | First handler begins validation |
| `[AuthenticationHandler] Authentication successful!` | 86 | Credentials match, passes to next |
| `[AuthenticationHandler] Authentication FAILED...` | 89 | Chain stops at first handler |
| `[RoleAuthorizationHandler] Checking role...` | 120 | Second handler validates role |
| `[RoleAuthorizationHandler] Role '...' is authorized!` | 123 | Role valid, continues chain |
| `[RoleAuthorizationHandler] Role '...' is NOT authorized` | 126 | Chain stops at second handler |
| `[PriorityHandler] Checking ticket priority...` | 151 | Third handler checks priority |
| `[PriorityHandler] Priority level '...' approved!` | 160 | Priority valid, continues chain |
| `[PriorityHandler] Only admin/support can submit...` | 157 | Chain stops at third handler |
| `[TicketProcessingHandler] Processing ticket...` | 185 | Final handler processes request |
| `[TicketProcessingHandler] Ticket created successfully...` | 186 | Ticket creation completed |
| `[Chain End] Request processed successfully!` | 49 | End of chain reached |

### Test Case Analysis

| Test | Request Data | Fails At | Lines Executed |
|------|-------------|----------|----------------|
| Test 1 | admin/admin123/admin/critical | None (Success) | 80,86,120,123,151,160,185,186,49 |
| Test 2 | hacker/wrongpass/admin/low | AuthenticationHandler | 80,89 |
| Test 3 | user1/pass123/guest/medium | RoleAuthorizationHandler | 80,86,120,126 |
| Test 4 | support/support456/premium_user/critical | PriorityHandler | 80,86,120,123,151,157 |
| Test 5 | support/support456/support_agent/high | None (Success) | 80,86,120,123,151,160,185,186,49 |

## Key Characteristics of Chain of Responsibility in Rust

### 1. Memory Safety with Smart Pointers
Rust requires explicit handling of ownership and references. The pattern uses `Rc<RefCell<dyn Handler>>` to:
- `Rc`: Share handler ownership across the chain
- `RefCell`: Allow mutable access through immutable references
- `dyn Handler`: Enable dynamic dispatch for different handler types

### 2. Trait Objects for Polymorphism
The `Handler` trait with `dyn Handler` provides runtime polymorphism, allowing different concrete handlers to be treated uniformly in the chain.

### 3. Composition over Inheritance
Since Rust doesn't have classical inheritance, the `BaseHandler` struct is composed into each concrete handler rather than inherited, demonstrating Rust's preference for composition.

### 4. Early Termination
Each handler can stop the chain by returning `false`, preventing unnecessary processing of invalid requests.

### 5. Decoupled Handlers
Each handler is independent and only knows about:
- The request it processes
- The next handler in the chain (if any)

This makes it easy to add, remove, or reorder handlers without modifying existing code.

## Compilation

This code can be compiled with standard `rustc`:

```bash
rustc main_chain_of_responsibility.rs -o main_chain_of_responsibility.exe
./main_chain_of_responsibility.exe
```

No external dependencies are required. The code uses only the Rust standard library.
