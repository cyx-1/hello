/**
 * Chain of Responsibility Design Pattern in TypeScript
 *
 * The Chain of Responsibility pattern passes a request along a chain of handlers.
 * Each handler decides either to process the request or to pass it to the next
 * handler in the chain. This decouples the sender from receivers and allows
 * multiple objects to handle the request.
 */

// ============================================================
// Example 1: Expense Approval System
// ============================================================

// Request interface
interface ExpenseRequest {
    id: string;
    description: string;
    amount: number;
    requester: string;
}

// Abstract Handler
abstract class ExpenseApprover {
    protected nextApprover: ExpenseApprover | null = null;
    protected approverName: string;
    protected approvalLimit: number;

    constructor(name: string, limit: number) {
        this.approverName = name;
        this.approvalLimit = limit;
    }

    setNext(approver: ExpenseApprover): ExpenseApprover {
        this.nextApprover = approver;
        return approver;
    }

    handle(request: ExpenseRequest): void {
        console.log(`[Line 37] ${this.approverName}: Reviewing expense #${request.id} for $${request.amount}`);

        if (request.amount <= this.approvalLimit) {
            this.approve(request);
        } else if (this.nextApprover) {
            console.log(`[Line 42] ${this.approverName}: Amount exceeds my limit of $${this.approvalLimit}, escalating...`);
            this.nextApprover.handle(request);
        } else {
            this.reject(request);
        }
    }

    protected approve(request: ExpenseRequest): void {
        console.log(`[Line 49] ${this.approverName}: APPROVED expense #${request.id} - "${request.description}" for $${request.amount}`);
    }

    protected reject(request: ExpenseRequest): void {
        console.log(`[Line 53] ${this.approverName}: REJECTED expense #${request.id} - Amount $${request.amount} exceeds all approval limits`);
    }
}

// Concrete Handlers
class TeamLead extends ExpenseApprover {
    constructor() {
        super("Team Lead", 500);
        console.log("[Line 61] TeamLead: Initialized with approval limit of $500");
    }
}

class Manager extends ExpenseApprover {
    constructor() {
        super("Manager", 2500);
        console.log("[Line 68] Manager: Initialized with approval limit of $2,500");
    }
}

class Director extends ExpenseApprover {
    constructor() {
        super("Director", 10000);
        console.log("[Line 75] Director: Initialized with approval limit of $10,000");
    }
}

class VicePresident extends ExpenseApprover {
    constructor() {
        super("Vice President", 50000);
        console.log("[Line 82] VicePresident: Initialized with approval limit of $50,000");
    }
}

class CEO extends ExpenseApprover {
    constructor() {
        super("CEO", 100000);
        console.log("[Line 89] CEO: Initialized with approval limit of $100,000");
    }
}

// ============================================================
// Example 2: Support Ticket Handling
// ============================================================

// Support ticket levels
enum TicketPriority {
    LOW = "LOW",
    MEDIUM = "MEDIUM",
    HIGH = "HIGH",
    CRITICAL = "CRITICAL"
}

interface SupportTicket {
    id: string;
    title: string;
    priority: TicketPriority;
    description: string;
}

// Abstract Handler for Support
abstract class SupportHandler {
    protected nextHandler: SupportHandler | null = null;
    protected handlerName: string;
    protected handledPriorities: TicketPriority[];

    constructor(name: string, priorities: TicketPriority[]) {
        this.handlerName = name;
        this.handledPriorities = priorities;
    }

    setNext(handler: SupportHandler): SupportHandler {
        this.nextHandler = handler;
        return handler;
    }

    handle(ticket: SupportTicket): void {
        console.log(`[Line 126] ${this.handlerName}: Received ticket #${ticket.id} [${ticket.priority}] - "${ticket.title}"`);

        if (this.canHandle(ticket)) {
            this.processTicket(ticket);
        } else if (this.nextHandler) {
            console.log(`[Line 131] ${this.handlerName}: Cannot handle ${ticket.priority} priority, passing to next level...`);
            this.nextHandler.handle(ticket);
        } else {
            console.log(`[Line 134] ${this.handlerName}: No handler available for ticket #${ticket.id}`);
        }
    }

    protected canHandle(ticket: SupportTicket): boolean {
        return this.handledPriorities.includes(ticket.priority);
    }

    protected abstract processTicket(ticket: SupportTicket): void;
}

// Concrete Support Handlers
class HelpDesk extends SupportHandler {
    constructor() {
        super("Help Desk", [TicketPriority.LOW]);
        console.log("[Line 149] HelpDesk: Initialized to handle LOW priority tickets");
    }

    protected processTicket(ticket: SupportTicket): void {
        console.log(`[Line 153] HelpDesk: RESOLVED ticket #${ticket.id} - Basic support provided for "${ticket.title}"`);
    }
}

class TechnicalSupport extends SupportHandler {
    constructor() {
        super("Technical Support", [TicketPriority.MEDIUM]);
        console.log("[Line 160] TechnicalSupport: Initialized to handle MEDIUM priority tickets");
    }

    protected processTicket(ticket: SupportTicket): void {
        console.log(`[Line 164] TechnicalSupport: RESOLVED ticket #${ticket.id} - Technical investigation completed for "${ticket.title}"`);
    }
}

class SeniorEngineer extends SupportHandler {
    constructor() {
        super("Senior Engineer", [TicketPriority.HIGH]);
        console.log("[Line 171] SeniorEngineer: Initialized to handle HIGH priority tickets");
    }

    protected processTicket(ticket: SupportTicket): void {
        console.log(`[Line 175] SeniorEngineer: RESOLVED ticket #${ticket.id} - Expert analysis completed for "${ticket.title}"`);
    }
}

class EmergencyTeam extends SupportHandler {
    constructor() {
        super("Emergency Team", [TicketPriority.CRITICAL]);
        console.log("[Line 182] EmergencyTeam: Initialized to handle CRITICAL priority tickets");
    }

    protected processTicket(ticket: SupportTicket): void {
        console.log(`[Line 186] EmergencyTeam: EMERGENCY RESPONSE for ticket #${ticket.id} - Immediate action taken for "${ticket.title}"`);
    }
}

// ============================================================
// Example 3: Authentication Middleware Chain
// ============================================================

interface AuthRequest {
    userId: string;
    token: string;
    role: string;
    ipAddress: string;
    resource: string;
}

interface AuthResult {
    success: boolean;
    message: string;
}

abstract class AuthMiddleware {
    protected next: AuthMiddleware | null = null;
    protected middlewareName: string;

    constructor(name: string) {
        this.middlewareName = name;
    }

    setNext(middleware: AuthMiddleware): AuthMiddleware {
        this.next = middleware;
        return middleware;
    }

    handle(request: AuthRequest): AuthResult {
        console.log(`[Line 219] ${this.middlewareName}: Processing request from user "${request.userId}"`);

        const result = this.check(request);
        if (!result.success) {
            console.log(`[Line 223] ${this.middlewareName}: BLOCKED - ${result.message}`);
            return result;
        }

        console.log(`[Line 227] ${this.middlewareName}: PASSED - ${result.message}`);

        if (this.next) {
            return this.next.handle(request);
        }

        return { success: true, message: "All authentication checks passed" };
    }

    protected abstract check(request: AuthRequest): AuthResult;
}

// Concrete Authentication Middleware
class IPWhitelistMiddleware extends AuthMiddleware {
    private whitelist: string[] = ["192.168.1.1", "10.0.0.1", "127.0.0.1"];

    constructor() {
        super("IP Whitelist");
        console.log("[Line 244] IPWhitelistMiddleware: Initialized with whitelist");
    }

    protected check(request: AuthRequest): AuthResult {
        if (this.whitelist.includes(request.ipAddress)) {
            return { success: true, message: `IP ${request.ipAddress} is whitelisted` };
        }
        return { success: false, message: `IP ${request.ipAddress} is not in whitelist` };
    }
}

class TokenValidationMiddleware extends AuthMiddleware {
    constructor() {
        super("Token Validation");
        console.log("[Line 258] TokenValidationMiddleware: Initialized");
    }

    protected check(request: AuthRequest): AuthResult {
        // Simulate token validation
        if (request.token && request.token.startsWith("valid-")) {
            return { success: true, message: "Token is valid" };
        }
        return { success: false, message: "Invalid or expired token" };
    }
}

class RoleAuthorizationMiddleware extends AuthMiddleware {
    private resourcePermissions: Map<string, string[]> = new Map([
        ["admin-panel", ["admin"]],
        ["user-data", ["admin", "manager"]],
        ["public-api", ["admin", "manager", "user"]]
    ]);

    constructor() {
        super("Role Authorization");
        console.log("[Line 278] RoleAuthorizationMiddleware: Initialized with role permissions");
    }

    protected check(request: AuthRequest): AuthResult {
        const allowedRoles = this.resourcePermissions.get(request.resource);
        if (!allowedRoles) {
            return { success: true, message: `Resource "${request.resource}" has no restrictions` };
        }
        if (allowedRoles.includes(request.role)) {
            return { success: true, message: `Role "${request.role}" authorized for "${request.resource}"` };
        }
        return { success: false, message: `Role "${request.role}" not authorized for "${request.resource}"` };
    }
}

class RateLimitMiddleware extends AuthMiddleware {
    private requestCounts: Map<string, number> = new Map();
    private limit: number = 100;

    constructor() {
        super("Rate Limiter");
        console.log("[Line 298] RateLimitMiddleware: Initialized with limit of 100 requests");
    }

    protected check(request: AuthRequest): AuthResult {
        const count = this.requestCounts.get(request.userId) || 0;
        if (count >= this.limit) {
            return { success: false, message: `Rate limit exceeded for user "${request.userId}"` };
        }
        this.requestCounts.set(request.userId, count + 1);
        return { success: true, message: `Request count: ${count + 1}/${this.limit}` };
    }
}

// ============================================================
// Demonstration
// ============================================================

function main(): void {
    console.log("=== Chain of Responsibility Pattern Demonstration ===\n");

    // Demo 1: Expense Approval Chain
    console.log("--- Demo 1: Expense Approval System ---\n");
    console.log("Setting up approval chain...\n");

    const teamLead = new TeamLead();
    const manager = new Manager();
    const director = new Director();
    const vp = new VicePresident();
    const ceo = new CEO();

    // Build the chain
    teamLead.setNext(manager).setNext(director).setNext(vp).setNext(ceo);
    console.log("\n[Line 329] Chain established: Team Lead -> Manager -> Director -> VP -> CEO\n");

    // Test expense requests
    const expenses: ExpenseRequest[] = [
        { id: "EXP-001", description: "Office supplies", amount: 250, requester: "Alice" },
        { id: "EXP-002", description: "Team lunch", amount: 800, requester: "Bob" },
        { id: "EXP-003", description: "Conference tickets", amount: 5000, requester: "Charlie" },
        { id: "EXP-004", description: "Server upgrade", amount: 25000, requester: "Diana" },
        { id: "EXP-005", description: "Office renovation", amount: 75000, requester: "Eve" },
        { id: "EXP-006", description: "Company acquisition", amount: 150000, requester: "Frank" }
    ];

    expenses.forEach(expense => {
        console.log(`\nProcessing expense from ${expense.requester}:`);
        teamLead.handle(expense);
    });

    // Demo 2: Support Ticket Chain
    console.log("\n\n--- Demo 2: Support Ticket Handling ---\n");
    console.log("Setting up support chain...\n");

    const helpDesk = new HelpDesk();
    const techSupport = new TechnicalSupport();
    const seniorEngineer = new SeniorEngineer();
    const emergencyTeam = new EmergencyTeam();

    // Build the chain
    helpDesk.setNext(techSupport).setNext(seniorEngineer).setNext(emergencyTeam);
    console.log("\n[Line 356] Chain established: Help Desk -> Tech Support -> Senior Engineer -> Emergency Team\n");

    // Test support tickets
    const tickets: SupportTicket[] = [
        { id: "TKT-001", title: "Password reset", priority: TicketPriority.LOW, description: "User forgot password" },
        { id: "TKT-002", title: "Slow application", priority: TicketPriority.MEDIUM, description: "App takes 30s to load" },
        { id: "TKT-003", title: "Data corruption", priority: TicketPriority.HIGH, description: "Database records corrupted" },
        { id: "TKT-004", title: "System outage", priority: TicketPriority.CRITICAL, description: "Production server down" }
    ];

    tickets.forEach(ticket => {
        console.log(`\nProcessing ticket from queue:`);
        helpDesk.handle(ticket);
    });

    // Demo 3: Authentication Middleware Chain
    console.log("\n\n--- Demo 3: Authentication Middleware Chain ---\n");
    console.log("Setting up authentication middleware...\n");

    const ipCheck = new IPWhitelistMiddleware();
    const tokenCheck = new TokenValidationMiddleware();
    const roleCheck = new RoleAuthorizationMiddleware();
    const rateLimit = new RateLimitMiddleware();

    // Build the chain
    ipCheck.setNext(tokenCheck).setNext(roleCheck).setNext(rateLimit);
    console.log("\n[Line 382] Chain established: IP Whitelist -> Token Validation -> Role Authorization -> Rate Limiter\n");

    // Test authentication requests
    const authRequests: AuthRequest[] = [
        { userId: "user1", token: "valid-token-123", role: "admin", ipAddress: "192.168.1.1", resource: "admin-panel" },
        { userId: "user2", token: "valid-token-456", role: "user", ipAddress: "127.0.0.1", resource: "admin-panel" },
        { userId: "user3", token: "invalid-token", role: "admin", ipAddress: "10.0.0.1", resource: "user-data" },
        { userId: "user4", token: "valid-token-789", role: "manager", ipAddress: "8.8.8.8", resource: "public-api" }
    ];

    authRequests.forEach((request, index) => {
        console.log(`\n[Line 393] Auth Request ${index + 1}: User "${request.userId}" accessing "${request.resource}"`);
        const result = ipCheck.handle(request);
        console.log(`[Line 395] Final Result: ${result.success ? "ACCESS GRANTED" : "ACCESS DENIED"} - ${result.message}`);
    });

    console.log("\n=== End of Demonstration ===");
}

main();
