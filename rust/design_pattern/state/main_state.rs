// State Design Pattern - Document Workflow Example
// Demonstrates how an object's behavior changes based on its internal state

use std::fmt;

// =============================================================================
// State Trait - Defines interface for all concrete states
// =============================================================================

trait DocumentState: fmt::Display {
    fn edit(&self, content: &str) -> (Box<dyn DocumentState>, Option<String>);
    fn submit(&self) -> Box<dyn DocumentState>;
    fn approve(&self) -> Box<dyn DocumentState>;
    fn reject(&self) -> Box<dyn DocumentState>;
    fn publish(&self) -> Box<dyn DocumentState>;
    fn get_state_name(&self) -> &str;
}

// =============================================================================
// Concrete States
// =============================================================================

// Draft State - Document is being edited
struct DraftState;

impl fmt::Display for DraftState {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Draft")
    }
}

impl DocumentState for DraftState {
    fn edit(&self, content: &str) -> (Box<dyn DocumentState>, Option<String>) {
        println!("  [Draft] Editing document content...");
        println!("  [Draft] Content updated successfully");
        (Box::new(DraftState), Some(content.to_string()))
    }

    fn submit(&self) -> Box<dyn DocumentState> {
        println!("  [Draft] Submitting document for moderation...");
        println!("  [Draft -> Moderation] Document submitted for review");
        Box::new(ModerationState)
    }

    fn approve(&self) -> Box<dyn DocumentState> {
        println!("  [Draft] Cannot approve - document must be submitted first");
        Box::new(DraftState)
    }

    fn reject(&self) -> Box<dyn DocumentState> {
        println!("  [Draft] Cannot reject - document is not under review");
        Box::new(DraftState)
    }

    fn publish(&self) -> Box<dyn DocumentState> {
        println!("  [Draft] Cannot publish - document must go through moderation");
        Box::new(DraftState)
    }

    fn get_state_name(&self) -> &str {
        "Draft"
    }
}

// Moderation State - Document is under review
struct ModerationState;

impl fmt::Display for ModerationState {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Moderation")
    }
}

impl DocumentState for ModerationState {
    fn edit(&self, _content: &str) -> (Box<dyn DocumentState>, Option<String>) {
        println!("  [Moderation] Cannot edit - document is under review");
        (Box::new(ModerationState), None)
    }

    fn submit(&self) -> Box<dyn DocumentState> {
        println!("  [Moderation] Document already submitted for review");
        Box::new(ModerationState)
    }

    fn approve(&self) -> Box<dyn DocumentState> {
        println!("  [Moderation] Moderator approving document...");
        println!("  [Moderation -> Approved] Document approved and ready for publishing");
        Box::new(ApprovedState)
    }

    fn reject(&self) -> Box<dyn DocumentState> {
        println!("  [Moderation] Moderator rejecting document...");
        println!("  [Moderation -> Draft] Document rejected - returned to draft");
        Box::new(DraftState)
    }

    fn publish(&self) -> Box<dyn DocumentState> {
        println!("  [Moderation] Cannot publish - document must be approved first");
        Box::new(ModerationState)
    }

    fn get_state_name(&self) -> &str {
        "Moderation"
    }
}

// Approved State - Document is approved and ready to publish
struct ApprovedState;

impl fmt::Display for ApprovedState {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Approved")
    }
}

impl DocumentState for ApprovedState {
    fn edit(&self, _content: &str) -> (Box<dyn DocumentState>, Option<String>) {
        println!("  [Approved] Cannot edit - document is already approved");
        (Box::new(ApprovedState), None)
    }

    fn submit(&self) -> Box<dyn DocumentState> {
        println!("  [Approved] Document already approved - no need to submit");
        Box::new(ApprovedState)
    }

    fn approve(&self) -> Box<dyn DocumentState> {
        println!("  [Approved] Document already approved");
        Box::new(ApprovedState)
    }

    fn reject(&self) -> Box<dyn DocumentState> {
        println!("  [Approved] Revoking approval...");
        println!("  [Approved -> Draft] Approval revoked - returned to draft");
        Box::new(DraftState)
    }

    fn publish(&self) -> Box<dyn DocumentState> {
        println!("  [Approved] Publishing document...");
        println!("  [Approved -> Published] Document is now live!");
        Box::new(PublishedState)
    }

    fn get_state_name(&self) -> &str {
        "Approved"
    }
}

// Published State - Document is live
struct PublishedState;

impl fmt::Display for PublishedState {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Published")
    }
}

impl DocumentState for PublishedState {
    fn edit(&self, _content: &str) -> (Box<dyn DocumentState>, Option<String>) {
        println!("  [Published] Cannot edit - document is already published");
        (Box::new(PublishedState), None)
    }

    fn submit(&self) -> Box<dyn DocumentState> {
        println!("  [Published] Document already published");
        Box::new(PublishedState)
    }

    fn approve(&self) -> Box<dyn DocumentState> {
        println!("  [Published] Document already published");
        Box::new(PublishedState)
    }

    fn reject(&self) -> Box<dyn DocumentState> {
        println!("  [Published] Unpublishing document...");
        println!("  [Published -> Draft] Document unpublished - returned to draft");
        Box::new(DraftState)
    }

    fn publish(&self) -> Box<dyn DocumentState> {
        println!("  [Published] Document is already published");
        Box::new(PublishedState)
    }

    fn get_state_name(&self) -> &str {
        "Published"
    }
}

// =============================================================================
// Context - Document that holds state and delegates operations
// =============================================================================

struct Document {
    title: String,
    content: String,
    state: Box<dyn DocumentState>,
}

impl Document {
    fn new(title: &str) -> Self {
        println!("Creating new document: '{}'", title);
        println!("  Initial state: Draft");
        Document {
            title: title.to_string(),
            content: String::new(),
            state: Box::new(DraftState),
        }
    }

    fn edit(&mut self, content: &str) {
        println!("\nAction: Edit document");
        let (new_state, new_content) = self.state.edit(content);
        self.state = new_state;
        if let Some(c) = new_content {
            self.content = c;
        }
    }

    fn submit(&mut self) {
        println!("\nAction: Submit document");
        self.state = self.state.submit();
    }

    fn approve(&mut self) {
        println!("\nAction: Approve document");
        self.state = self.state.approve();
    }

    fn reject(&mut self) {
        println!("\nAction: Reject document");
        self.state = self.state.reject();
    }

    fn publish(&mut self) {
        println!("\nAction: Publish document");
        self.state = self.state.publish();
    }

    fn status(&self) {
        println!("\n--- Document Status ---");
        println!("Title: {}", self.title);
        println!("State: {}", self.state.get_state_name());
        println!("Content: {}", if self.content.is_empty() { "(empty)" } else { &self.content });
        println!("-----------------------");
    }
}

// =============================================================================
// Main - Demonstrate state transitions
// =============================================================================

fn main() {
    println!("=== State Design Pattern Demo ===");
    println!("Document Workflow: Draft -> Moderation -> Approved -> Published\n");

    // Create a new document (starts in Draft state)
    let mut doc = Document::new("Rust State Pattern Guide");
    doc.status();

    // Scenario 1: Try invalid operations in Draft state
    println!("\n>>> Scenario 1: Invalid operations in Draft state");
    doc.approve();  // Cannot approve in Draft
    doc.publish();  // Cannot publish in Draft

    // Scenario 2: Valid workflow - edit and submit
    println!("\n>>> Scenario 2: Edit and submit document");
    doc.edit("This is the initial content about the State pattern.");
    doc.submit();
    doc.status();

    // Scenario 3: Try to edit while in Moderation
    println!("\n>>> Scenario 3: Try to edit during moderation");
    doc.edit("Trying to change content...");

    // Scenario 4: Reject and return to Draft
    println!("\n>>> Scenario 4: Reject document");
    doc.reject();
    doc.status();

    // Scenario 5: Edit, resubmit, and approve
    println!("\n>>> Scenario 5: Revise, resubmit, and approve");
    doc.edit("Revised content with improvements.");
    doc.submit();
    doc.approve();
    doc.status();

    // Scenario 6: Publish the approved document
    println!("\n>>> Scenario 6: Publish document");
    doc.publish();
    doc.status();

    // Scenario 7: Try operations on published document
    println!("\n>>> Scenario 7: Operations on published document");
    doc.edit("Cannot change published content");
    doc.approve();

    // Scenario 8: Unpublish document
    println!("\n>>> Scenario 8: Unpublish document");
    doc.reject();
    doc.status();

    println!("\n=== Demo Complete ===");
}
