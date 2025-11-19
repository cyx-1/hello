/**
 * Comprehensive demonstration of the Chain of Responsibility Pattern in Java
 *
 * The Chain of Responsibility pattern avoids coupling the sender of a request
 * to its receiver by giving more than one object a chance to handle the request.
 */

// Handler interface
abstract class SupportHandler {
    protected SupportHandler nextHandler;
    protected String handlerName;

    public SupportHandler(String name) {
        this.handlerName = name;
    }

    public SupportHandler setNext(SupportHandler handler) {
        this.nextHandler = handler;
        return handler;
    }

    public void handle(SupportTicket ticket) {
        if (canHandle(ticket)) {
            processTicket(ticket);
        } else if (nextHandler != null) {
            System.out.println("  [" + handlerName + "] Passing to next handler...");
            nextHandler.handle(ticket);
        } else {
            System.out.println("  [" + handlerName + "] No handler available for: " + ticket.getDescription());
        }
    }

    protected abstract boolean canHandle(SupportTicket ticket);
    protected abstract void processTicket(SupportTicket ticket);
}

// Request class
class SupportTicket {
    public enum Priority { LOW, MEDIUM, HIGH, CRITICAL }
    public enum Type { GENERAL, TECHNICAL, BILLING, SECURITY }

    private String description;
    private Priority priority;
    private Type type;

    public SupportTicket(String description, Priority priority, Type type) {
        this.description = description;
        this.priority = priority;
        this.type = type;
    }

    public String getDescription() { return description; }
    public Priority getPriority() { return priority; }
    public Type getType() { return type; }
}

// Concrete Handlers
class FrontDeskHandler extends SupportHandler {
    public FrontDeskHandler() {
        super("Front Desk");
    }

    @Override
    protected boolean canHandle(SupportTicket ticket) {
        return ticket.getType() == SupportTicket.Type.GENERAL &&
               ticket.getPriority() == SupportTicket.Priority.LOW;
    }

    @Override
    protected void processTicket(SupportTicket ticket) {
        System.out.println("  [Front Desk] Handling general inquiry: " + ticket.getDescription());
    }
}

class TechnicalSupportHandler extends SupportHandler {
    public TechnicalSupportHandler() {
        super("Technical Support");
    }

    @Override
    protected boolean canHandle(SupportTicket ticket) {
        return ticket.getType() == SupportTicket.Type.TECHNICAL &&
               (ticket.getPriority() == SupportTicket.Priority.LOW ||
                ticket.getPriority() == SupportTicket.Priority.MEDIUM);
    }

    @Override
    protected void processTicket(SupportTicket ticket) {
        System.out.println("  [Technical Support] Resolving technical issue: " + ticket.getDescription());
    }
}

class BillingHandler extends SupportHandler {
    public BillingHandler() {
        super("Billing Department");
    }

    @Override
    protected boolean canHandle(SupportTicket ticket) {
        return ticket.getType() == SupportTicket.Type.BILLING;
    }

    @Override
    protected void processTicket(SupportTicket ticket) {
        System.out.println("  [Billing] Processing billing request: " + ticket.getDescription());
    }
}

class ManagerHandler extends SupportHandler {
    public ManagerHandler() {
        super("Manager");
    }

    @Override
    protected boolean canHandle(SupportTicket ticket) {
        return ticket.getPriority() == SupportTicket.Priority.HIGH ||
               ticket.getPriority() == SupportTicket.Priority.CRITICAL;
    }

    @Override
    protected void processTicket(SupportTicket ticket) {
        System.out.println("  [Manager] Escalated issue handled: " + ticket.getDescription());
    }
}

class SecurityHandler extends SupportHandler {
    public SecurityHandler() {
        super("Security Team");
    }

    @Override
    protected boolean canHandle(SupportTicket ticket) {
        return ticket.getType() == SupportTicket.Type.SECURITY;
    }

    @Override
    protected void processTicket(SupportTicket ticket) {
        System.out.println("  [Security] ALERT! Security issue: " + ticket.getDescription());
    }
}

// Another example: Request approval chain

abstract class Approver {
    protected Approver nextApprover;
    protected String title;
    protected double approvalLimit;

    public Approver(String title, double approvalLimit) {
        this.title = title;
        this.approvalLimit = approvalLimit;
    }

    public Approver setNext(Approver approver) {
        this.nextApprover = approver;
        return approver;
    }

    public void processRequest(PurchaseRequest request) {
        if (request.getAmount() <= approvalLimit) {
            approve(request);
        } else if (nextApprover != null) {
            System.out.println("  [" + title + "] Amount $" + request.getAmount() +
                              " exceeds my limit of $" + approvalLimit + ". Escalating...");
            nextApprover.processRequest(request);
        } else {
            System.out.println("  [" + title + "] Request for $" + request.getAmount() +
                              " requires board approval.");
        }
    }

    protected void approve(PurchaseRequest request) {
        System.out.println("  [" + title + "] Approved: " + request.getDescription() +
                          " for $" + request.getAmount());
    }
}

class PurchaseRequest {
    private String description;
    private double amount;

    public PurchaseRequest(String description, double amount) {
        this.description = description;
        this.amount = amount;
    }

    public String getDescription() { return description; }
    public double getAmount() { return amount; }
}

class TeamLead extends Approver {
    public TeamLead() { super("Team Lead", 1000); }
}

class DepartmentManager extends Approver {
    public DepartmentManager() { super("Department Manager", 5000); }
}

class Director extends Approver {
    public Director() { super("Director", 20000); }
}

class VP extends Approver {
    public VP() { super("VP", 50000); }
}

class CEO extends Approver {
    public CEO() { super("CEO", 100000); }
}

// Third example: Middleware chain

abstract class Middleware {
    private Middleware next;

    public Middleware linkWith(Middleware next) {
        this.next = next;
        return next;
    }

    public abstract boolean check(String email, String password);

    protected boolean checkNext(String email, String password) {
        if (next == null) {
            return true;
        }
        return next.check(email, password);
    }
}

class ThrottlingMiddleware extends Middleware {
    private int requestPerMinute;
    private int currentRequests = 0;

    public ThrottlingMiddleware(int requestPerMinute) {
        this.requestPerMinute = requestPerMinute;
    }

    @Override
    public boolean check(String email, String password) {
        if (currentRequests >= requestPerMinute) {
            System.out.println("  [Throttling] Request limit exceeded!");
            return false;
        }
        currentRequests++;
        System.out.println("  [Throttling] Request allowed (" + currentRequests + "/" + requestPerMinute + ")");
        return checkNext(email, password);
    }
}

class AuthenticationMiddleware extends Middleware {
    @Override
    public boolean check(String email, String password) {
        if (!email.contains("@")) {
            System.out.println("  [Auth] Invalid email format!");
            return false;
        }
        if (password.length() < 6) {
            System.out.println("  [Auth] Password too short!");
            return false;
        }
        System.out.println("  [Auth] Credentials validated");
        return checkNext(email, password);
    }
}

class AuthorizationMiddleware extends Middleware {
    @Override
    public boolean check(String email, String password) {
        if (email.equals("admin@example.com")) {
            System.out.println("  [Authorization] Admin access granted");
            return checkNext(email, password);
        }
        System.out.println("  [Authorization] Standard user access");
        return checkNext(email, password);
    }
}

public class MainChainOfResponsibility {
    public static void main(String[] args) {
        System.out.println("=== Chain of Responsibility Pattern Demonstration ===\n");

        // Support ticket example
        System.out.println("--- 1. Customer Support Chain ---");

        SupportHandler frontDesk = new FrontDeskHandler();
        SupportHandler techSupport = new TechnicalSupportHandler();
        SupportHandler billing = new BillingHandler();
        SupportHandler manager = new ManagerHandler();
        SupportHandler security = new SecurityHandler();

        frontDesk.setNext(techSupport).setNext(billing).setNext(manager).setNext(security);

        System.out.println("\nTicket 1: General inquiry (LOW)");
        frontDesk.handle(new SupportTicket("How do I reset password?",
            SupportTicket.Priority.LOW, SupportTicket.Type.GENERAL));

        System.out.println("\nTicket 2: Technical issue (MEDIUM)");
        frontDesk.handle(new SupportTicket("Application crashes on startup",
            SupportTicket.Priority.MEDIUM, SupportTicket.Type.TECHNICAL));

        System.out.println("\nTicket 3: Billing inquiry");
        frontDesk.handle(new SupportTicket("Incorrect charge on invoice",
            SupportTicket.Priority.MEDIUM, SupportTicket.Type.BILLING));

        System.out.println("\nTicket 4: Critical issue (CRITICAL)");
        frontDesk.handle(new SupportTicket("System completely down",
            SupportTicket.Priority.CRITICAL, SupportTicket.Type.TECHNICAL));

        System.out.println("\nTicket 5: Security breach");
        frontDesk.handle(new SupportTicket("Unauthorized access detected",
            SupportTicket.Priority.CRITICAL, SupportTicket.Type.SECURITY));
        System.out.println();

        // Purchase approval example
        System.out.println("--- 2. Purchase Approval Chain ---");

        Approver teamLead = new TeamLead();
        Approver manager2 = new DepartmentManager();
        Approver director = new Director();
        Approver vp = new VP();
        Approver ceo = new CEO();

        teamLead.setNext(manager2).setNext(director).setNext(vp).setNext(ceo);

        System.out.println("\nRequest 1: Office supplies");
        teamLead.processRequest(new PurchaseRequest("Office supplies", 500));

        System.out.println("\nRequest 2: New laptop");
        teamLead.processRequest(new PurchaseRequest("Developer laptop", 2500));

        System.out.println("\nRequest 3: Server equipment");
        teamLead.processRequest(new PurchaseRequest("Server equipment", 15000));

        System.out.println("\nRequest 4: Department renovation");
        teamLead.processRequest(new PurchaseRequest("Office renovation", 75000));

        System.out.println("\nRequest 5: Building expansion");
        teamLead.processRequest(new PurchaseRequest("New building wing", 500000));
        System.out.println();

        // Middleware example
        System.out.println("--- 3. Authentication Middleware Chain ---");

        Middleware middleware = new ThrottlingMiddleware(5);
        middleware.linkWith(new AuthenticationMiddleware())
                  .linkWith(new AuthorizationMiddleware());

        System.out.println("\nLogin attempt 1:");
        middleware.check("admin@example.com", "admin123");

        System.out.println("\nLogin attempt 2 (invalid email):");
        middleware.check("invalid-email", "password123");

        System.out.println("\nLogin attempt 3 (short password):");
        middleware.check("user@example.com", "123");

        System.out.println("\n=== Summary ===");
        System.out.println("Chain of Responsibility pattern benefits:");
        System.out.println("  - Decouples sender and receiver");
        System.out.println("  - Adds flexibility in assigning responsibilities");
        System.out.println("  - Each handler focuses on its specific responsibility");
        System.out.println("  - Easy to add or remove handlers");
    }
}
