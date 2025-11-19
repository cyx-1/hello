/**
 * Comprehensive demonstration of the State Pattern in Java
 *
 * The State pattern allows an object to alter its behavior when its internal
 * state changes. The object will appear to change its class.
 */

// State interface
interface VendingMachineState {
    void insertCoin();
    void ejectCoin();
    void selectProduct();
    void dispense();
}

// Context
class VendingMachine {
    private VendingMachineState noCoinState;
    private VendingMachineState hasCoinState;
    private VendingMachineState soldState;
    private VendingMachineState soldOutState;

    private VendingMachineState currentState;
    private int count;

    public VendingMachine(int count) {
        noCoinState = new NoCoinState(this);
        hasCoinState = new HasCoinState(this);
        soldState = new SoldState(this);
        soldOutState = new SoldOutState(this);

        this.count = count;
        if (count > 0) {
            currentState = noCoinState;
        } else {
            currentState = soldOutState;
        }
    }

    public void insertCoin() { currentState.insertCoin(); }
    public void ejectCoin() { currentState.ejectCoin(); }
    public void selectProduct() {
        currentState.selectProduct();
        currentState.dispense();
    }

    public void setState(VendingMachineState state) { currentState = state; }
    public VendingMachineState getNoCoinState() { return noCoinState; }
    public VendingMachineState getHasCoinState() { return hasCoinState; }
    public VendingMachineState getSoldState() { return soldState; }
    public VendingMachineState getSoldOutState() { return soldOutState; }

    public void releaseProduct() {
        if (count > 0) {
            count--;
            System.out.println("  [Machine] Product dispensed. Remaining: " + count);
        }
    }

    public int getCount() { return count; }
}

// Concrete States
class NoCoinState implements VendingMachineState {
    private VendingMachine machine;

    public NoCoinState(VendingMachine machine) {
        this.machine = machine;
    }

    @Override
    public void insertCoin() {
        System.out.println("  [NoCoin] Coin inserted");
        machine.setState(machine.getHasCoinState());
    }

    @Override
    public void ejectCoin() {
        System.out.println("  [NoCoin] No coin to eject");
    }

    @Override
    public void selectProduct() {
        System.out.println("  [NoCoin] Please insert a coin first");
    }

    @Override
    public void dispense() {
        System.out.println("  [NoCoin] Please insert a coin first");
    }
}

class HasCoinState implements VendingMachineState {
    private VendingMachine machine;

    public HasCoinState(VendingMachine machine) {
        this.machine = machine;
    }

    @Override
    public void insertCoin() {
        System.out.println("  [HasCoin] Coin already inserted");
    }

    @Override
    public void ejectCoin() {
        System.out.println("  [HasCoin] Coin ejected");
        machine.setState(machine.getNoCoinState());
    }

    @Override
    public void selectProduct() {
        System.out.println("  [HasCoin] Product selected");
        machine.setState(machine.getSoldState());
    }

    @Override
    public void dispense() {
        System.out.println("  [HasCoin] Please select a product");
    }
}

class SoldState implements VendingMachineState {
    private VendingMachine machine;

    public SoldState(VendingMachine machine) {
        this.machine = machine;
    }

    @Override
    public void insertCoin() {
        System.out.println("  [Sold] Please wait, dispensing product");
    }

    @Override
    public void ejectCoin() {
        System.out.println("  [Sold] Cannot eject, product is being dispensed");
    }

    @Override
    public void selectProduct() {
        System.out.println("  [Sold] Already dispensing");
    }

    @Override
    public void dispense() {
        machine.releaseProduct();
        if (machine.getCount() > 0) {
            machine.setState(machine.getNoCoinState());
        } else {
            System.out.println("  [Sold] Out of products");
            machine.setState(machine.getSoldOutState());
        }
    }
}

class SoldOutState implements VendingMachineState {
    private VendingMachine machine;

    public SoldOutState(VendingMachine machine) {
        this.machine = machine;
    }

    @Override
    public void insertCoin() {
        System.out.println("  [SoldOut] Machine is sold out, returning coin");
    }

    @Override
    public void ejectCoin() {
        System.out.println("  [SoldOut] No coin to eject");
    }

    @Override
    public void selectProduct() {
        System.out.println("  [SoldOut] Machine is sold out");
    }

    @Override
    public void dispense() {
        System.out.println("  [SoldOut] No product to dispense");
    }
}

// Document workflow example

interface DocumentState {
    void edit(DocumentContext doc);
    void review(DocumentContext doc);
    void approve(DocumentContext doc);
    void reject(DocumentContext doc);
    void publish(DocumentContext doc);
}

class DocumentContext {
    private DocumentState draftState = new DraftState();
    private DocumentState reviewState = new ReviewState();
    private DocumentState approvedState = new ApprovedState();
    private DocumentState publishedState = new PublishedState();

    private DocumentState currentState;
    private String name;

    public DocumentContext(String name) {
        this.name = name;
        this.currentState = draftState;
    }

    public void edit() { currentState.edit(this); }
    public void review() { currentState.review(this); }
    public void approve() { currentState.approve(this); }
    public void reject() { currentState.reject(this); }
    public void publish() { currentState.publish(this); }

    public void setState(String state) {
        switch (state) {
            case "draft": currentState = draftState; break;
            case "review": currentState = reviewState; break;
            case "approved": currentState = approvedState; break;
            case "published": currentState = publishedState; break;
        }
    }

    public String getName() { return name; }
}

class DraftState implements DocumentState {
    @Override
    public void edit(DocumentContext doc) {
        System.out.println("  [Draft] Editing document: " + doc.getName());
    }

    @Override
    public void review(DocumentContext doc) {
        System.out.println("  [Draft] Submitting for review: " + doc.getName());
        doc.setState("review");
    }

    @Override
    public void approve(DocumentContext doc) {
        System.out.println("  [Draft] Cannot approve from draft state");
    }

    @Override
    public void reject(DocumentContext doc) {
        System.out.println("  [Draft] Cannot reject from draft state");
    }

    @Override
    public void publish(DocumentContext doc) {
        System.out.println("  [Draft] Cannot publish from draft state");
    }
}

class ReviewState implements DocumentState {
    @Override
    public void edit(DocumentContext doc) {
        System.out.println("  [Review] Cannot edit during review");
    }

    @Override
    public void review(DocumentContext doc) {
        System.out.println("  [Review] Already in review");
    }

    @Override
    public void approve(DocumentContext doc) {
        System.out.println("  [Review] Document approved: " + doc.getName());
        doc.setState("approved");
    }

    @Override
    public void reject(DocumentContext doc) {
        System.out.println("  [Review] Document rejected, returning to draft");
        doc.setState("draft");
    }

    @Override
    public void publish(DocumentContext doc) {
        System.out.println("  [Review] Cannot publish without approval");
    }
}

class ApprovedState implements DocumentState {
    @Override
    public void edit(DocumentContext doc) {
        System.out.println("  [Approved] Editing, returning to draft");
        doc.setState("draft");
    }

    @Override
    public void review(DocumentContext doc) {
        System.out.println("  [Approved] Already approved");
    }

    @Override
    public void approve(DocumentContext doc) {
        System.out.println("  [Approved] Already approved");
    }

    @Override
    public void reject(DocumentContext doc) {
        System.out.println("  [Approved] Rejecting, returning to draft");
        doc.setState("draft");
    }

    @Override
    public void publish(DocumentContext doc) {
        System.out.println("  [Approved] Publishing document: " + doc.getName());
        doc.setState("published");
    }
}

class PublishedState implements DocumentState {
    @Override
    public void edit(DocumentContext doc) {
        System.out.println("  [Published] Cannot edit published document");
    }

    @Override
    public void review(DocumentContext doc) {
        System.out.println("  [Published] Cannot review published document");
    }

    @Override
    public void approve(DocumentContext doc) {
        System.out.println("  [Published] Already published");
    }

    @Override
    public void reject(DocumentContext doc) {
        System.out.println("  [Published] Cannot reject published document");
    }

    @Override
    public void publish(DocumentContext doc) {
        System.out.println("  [Published] Already published");
    }
}

public class MainState {
    public static void main(String[] args) {
        System.out.println("=== State Pattern Demonstration ===\n");

        // Vending machine example
        System.out.println("--- 1. Vending Machine ---");

        VendingMachine machine = new VendingMachine(2);

        System.out.println("\nAttempt without coin:");
        machine.selectProduct();

        System.out.println("\nNormal purchase:");
        machine.insertCoin();
        machine.selectProduct();

        System.out.println("\nEject coin:");
        machine.insertCoin();
        machine.ejectCoin();

        System.out.println("\nLast product:");
        machine.insertCoin();
        machine.selectProduct();

        System.out.println("\nSold out:");
        machine.insertCoin();
        System.out.println();

        // Document workflow
        System.out.println("--- 2. Document Workflow ---");

        DocumentContext doc = new DocumentContext("Annual Report");

        System.out.println("\nDraft phase:");
        doc.edit();
        doc.publish();  // Cannot publish from draft

        System.out.println("\nSubmit for review:");
        doc.review();
        doc.edit();     // Cannot edit during review

        System.out.println("\nReject and revise:");
        doc.reject();
        doc.edit();
        doc.review();

        System.out.println("\nApprove and publish:");
        doc.approve();
        doc.publish();

        System.out.println("\nTry to modify published:");
        doc.edit();

        System.out.println("\n=== Summary ===");
        System.out.println("State pattern benefits:");
        System.out.println("  - Localizes state-specific behavior");
        System.out.println("  - Makes state transitions explicit");
        System.out.println("  - State objects can be shared");
        System.out.println("\nVs Strategy pattern:");
        System.out.println("  - State: behavior changes based on internal state");
        System.out.println("  - Strategy: client chooses algorithm");
    }
}
