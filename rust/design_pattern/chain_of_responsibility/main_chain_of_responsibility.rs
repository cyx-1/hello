// Chain of Responsibility Design Pattern in Rust
// Example: Support Ticket Authentication and Authorization System

use std::cell::RefCell;
use std::rc::Rc;

// Request structure representing a support ticket with authentication info
#[derive(Clone, Debug)]
struct SupportRequest {
    user_id: String,
    password: String,
    role: String,
    ticket_priority: String,
    description: String,
}

impl SupportRequest {
    fn new(user_id: &str, password: &str, role: &str, priority: &str, desc: &str) -> Self {
        SupportRequest {
            user_id: user_id.to_string(),
            password: password.to_string(),
            role: role.to_string(),
            ticket_priority: priority.to_string(),
            description: desc.to_string(),
        }
    }
}

// Handler trait defining the chain interface
trait Handler {
    fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>);
    fn handle(&self, request: &SupportRequest) -> bool;
}

// Base handler with common chain functionality
struct BaseHandler {
    next: Option<Rc<RefCell<dyn Handler>>>,
}

impl BaseHandler {
    fn new() -> Self {
        BaseHandler { next: None }
    }

    fn handle_next(&self, request: &SupportRequest) -> bool {
        if let Some(ref next_handler) = self.next {
            return next_handler.borrow().handle(request);
        }
        println!("  [Chain End] Request processed successfully!");
        true
    }
}

// Concrete Handler 1: Authentication Handler
struct AuthenticationHandler {
    base: BaseHandler,
    valid_credentials: Vec<(String, String)>,
}

impl AuthenticationHandler {
    fn new() -> Self {
        let mut handler = AuthenticationHandler {
            base: BaseHandler::new(),
            valid_credentials: Vec::new(),
        };
        // Add some valid credentials
        handler.valid_credentials.push(("admin".to_string(), "admin123".to_string()));
        handler.valid_credentials.push(("user1".to_string(), "pass123".to_string()));
        handler.valid_credentials.push(("support".to_string(), "support456".to_string()));
        handler
    }
}

impl Handler for AuthenticationHandler {
    fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>) {
        self.base.next = Some(handler);
    }

    fn handle(&self, request: &SupportRequest) -> bool {
        println!("  [AuthenticationHandler] Checking credentials for user: {}", request.user_id);

        let is_valid = self.valid_credentials.iter()
            .any(|(user, pass)| user == &request.user_id && pass == &request.password);

        if is_valid {
            println!("  [AuthenticationHandler] Authentication successful!");
            self.base.handle_next(request)
        } else {
            println!("  [AuthenticationHandler] Authentication FAILED - Invalid credentials");
            false
        }
    }
}

// Concrete Handler 2: Role Authorization Handler
struct RoleAuthorizationHandler {
    base: BaseHandler,
    allowed_roles: Vec<String>,
}

impl RoleAuthorizationHandler {
    fn new() -> Self {
        let mut handler = RoleAuthorizationHandler {
            base: BaseHandler::new(),
            allowed_roles: Vec::new(),
        };
        handler.allowed_roles.push("admin".to_string());
        handler.allowed_roles.push("support_agent".to_string());
        handler.allowed_roles.push("premium_user".to_string());
        handler
    }
}

impl Handler for RoleAuthorizationHandler {
    fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>) {
        self.base.next = Some(handler);
    }

    fn handle(&self, request: &SupportRequest) -> bool {
        println!("  [RoleAuthorizationHandler] Checking role: {}", request.role);

        if self.allowed_roles.contains(&request.role) {
            println!("  [RoleAuthorizationHandler] Role '{}' is authorized!", request.role);
            self.base.handle_next(request)
        } else {
            println!("  [RoleAuthorizationHandler] Role '{}' is NOT authorized", request.role);
            false
        }
    }
}

// Concrete Handler 3: Priority Handler (checks if user can submit priority tickets)
struct PriorityHandler {
    base: BaseHandler,
}

impl PriorityHandler {
    fn new() -> Self {
        PriorityHandler {
            base: BaseHandler::new(),
        }
    }
}

impl Handler for PriorityHandler {
    fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>) {
        self.base.next = Some(handler);
    }

    fn handle(&self, request: &SupportRequest) -> bool {
        println!("  [PriorityHandler] Checking ticket priority: {}", request.ticket_priority);

        // Only admin and support_agent can submit critical tickets
        let can_submit_critical = request.role == "admin" || request.role == "support_agent";

        if request.ticket_priority == "critical" && !can_submit_critical {
            println!("  [PriorityHandler] Only admin/support can submit critical tickets");
            false
        } else {
            println!("  [PriorityHandler] Priority level '{}' approved!", request.ticket_priority);
            self.base.handle_next(request)
        }
    }
}

// Concrete Handler 4: Ticket Processing Handler (final handler)
struct TicketProcessingHandler {
    base: BaseHandler,
}

impl TicketProcessingHandler {
    fn new() -> Self {
        TicketProcessingHandler {
            base: BaseHandler::new(),
        }
    }
}

impl Handler for TicketProcessingHandler {
    fn set_next(&mut self, handler: Rc<RefCell<dyn Handler>>) {
        self.base.next = Some(handler);
    }

    fn handle(&self, request: &SupportRequest) -> bool {
        println!("  [TicketProcessingHandler] Processing ticket: '{}'", request.description);
        println!("  [TicketProcessingHandler] Ticket created successfully for user '{}'", request.user_id);
        self.base.handle_next(request)
    }
}

// Helper function to build the handler chain
fn build_handler_chain() -> Rc<RefCell<dyn Handler>> {
    let auth_handler = Rc::new(RefCell::new(AuthenticationHandler::new()));
    let role_handler = Rc::new(RefCell::new(RoleAuthorizationHandler::new()));
    let priority_handler = Rc::new(RefCell::new(PriorityHandler::new()));
    let ticket_handler = Rc::new(RefCell::new(TicketProcessingHandler::new()));

    // Build the chain: Auth -> Role -> Priority -> Ticket
    priority_handler.borrow_mut().set_next(ticket_handler);
    role_handler.borrow_mut().set_next(priority_handler);
    auth_handler.borrow_mut().set_next(role_handler);

    auth_handler
}

fn main() {
    println!("=== Chain of Responsibility Pattern Demo ===");
    println!("Support Ticket Authentication & Authorization System\n");

    // Build the handler chain
    let handler_chain = build_handler_chain();

    // Test Case 1: Successful request from admin
    println!("--- Test 1: Admin submitting critical ticket ---");
    let request1 = SupportRequest::new(
        "admin",
        "admin123",
        "admin",
        "critical",
        "Server outage in production"
    );
    let result1 = handler_chain.borrow().handle(&request1);
    println!("Result: {}\n", if result1 { "SUCCESS" } else { "FAILED" });

    // Test Case 2: Authentication failure
    println!("--- Test 2: Invalid credentials ---");
    let request2 = SupportRequest::new(
        "hacker",
        "wrongpass",
        "admin",
        "low",
        "Suspicious request"
    );
    let result2 = handler_chain.borrow().handle(&request2);
    println!("Result: {}\n", if result2 { "SUCCESS" } else { "FAILED" });

    // Test Case 3: Role authorization failure
    println!("--- Test 3: Unauthorized role ---");
    let request3 = SupportRequest::new(
        "user1",
        "pass123",
        "guest",
        "medium",
        "Need help with login"
    );
    let result3 = handler_chain.borrow().handle(&request3);
    println!("Result: {}\n", if result3 { "SUCCESS" } else { "FAILED" });

    // Test Case 4: Priority check failure
    println!("--- Test 4: Premium user trying critical priority ---");
    let request4 = SupportRequest::new(
        "support",
        "support456",
        "premium_user",
        "critical",
        "Urgent billing issue"
    );
    let result4 = handler_chain.borrow().handle(&request4);
    println!("Result: {}\n", if result4 { "SUCCESS" } else { "FAILED" });

    // Test Case 5: Successful request from support agent
    println!("--- Test 5: Support agent with normal priority ---");
    let request5 = SupportRequest::new(
        "support",
        "support456",
        "support_agent",
        "high",
        "Customer escalation"
    );
    let result5 = handler_chain.borrow().handle(&request5);
    println!("Result: {}\n", if result5 { "SUCCESS" } else { "FAILED" });

    println!("=== Demo Complete ===");
}
