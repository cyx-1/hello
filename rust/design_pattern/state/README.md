# State Design Pattern in Rust

## Description

The **State pattern** is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

This implementation demonstrates a document workflow system with four states:
- **Draft**: Document is being created/edited
- **Moderation**: Document is under review
- **Approved**: Document has been approved and is ready to publish
- **Published**: Document is live

Each state defines which operations are valid and how they affect the document's state.

## Source Code

```rust
  1  // State Design Pattern - Document Workflow Example
  2  // Demonstrates how an object's behavior changes based on its internal state
  3
  4  use std::fmt;
  5
  6  // =============================================================================
  7  // State Trait - Defines interface for all concrete states
  8  // =============================================================================
  9
 10  trait DocumentState: fmt::Display {
 11      fn edit(&self, content: &str) -> (Box<dyn DocumentState>, Option<String>);
 12      fn submit(&self) -> Box<dyn DocumentState>;
 13      fn approve(&self) -> Box<dyn DocumentState>;
 14      fn reject(&self) -> Box<dyn DocumentState>;
 15      fn publish(&self) -> Box<dyn DocumentState>;
 16      fn get_state_name(&self) -> &str;
 17  }
 18
 19  // =============================================================================
 20  // Concrete States
 21  // =============================================================================
 22
 23  // Draft State - Document is being edited
 24  struct DraftState;
 25
 26  impl fmt::Display for DraftState {
 27      fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
 28          write!(f, "Draft")
 29      }
 30  }
 31
 32  impl DocumentState for DraftState {
 33      fn edit(&self, content: &str) -> (Box<dyn DocumentState>, Option<String>) {
 34          println!("  [Draft] Editing document content...");
 35          println!("  [Draft] Content updated successfully");
 36          (Box::new(DraftState), Some(content.to_string()))
 37      }
 38
 39      fn submit(&self) -> Box<dyn DocumentState> {
 40          println!("  [Draft] Submitting document for moderation...");
 41          println!("  [Draft -> Moderation] Document submitted for review");
 42          Box::new(ModerationState)
 43      }
 44
 45      fn approve(&self) -> Box<dyn DocumentState> {
 46          println!("  [Draft] Cannot approve - document must be submitted first");
 47          Box::new(DraftState)
 48      }
 49
 50      fn reject(&self) -> Box<dyn DocumentState> {
 51          println!("  [Draft] Cannot reject - document is not under review");
 52          Box::new(DraftState)
 53      }
 54
 55      fn publish(&self) -> Box<dyn DocumentState> {
 56          println!("  [Draft] Cannot publish - document must go through moderation");
 57          Box::new(DraftState)
 58      }
 59
 60      fn get_state_name(&self) -> &str {
 61          "Draft"
 62      }
 63  }
 64
 65  // Moderation State - Document is under review
 66  struct ModerationState;
 67
 68  impl fmt::Display for ModerationState {
 69      fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
 70          write!(f, "Moderation")
 71      }
 72  }
 73
 74  impl DocumentState for ModerationState {
 75      fn edit(&self, _content: &str) -> (Box<dyn DocumentState>, Option<String>) {
 76          println!("  [Moderation] Cannot edit - document is under review");
 77          (Box::new(ModerationState), None)
 78      }
 79
 80      fn submit(&self) -> Box<dyn DocumentState> {
 81          println!("  [Moderation] Document already submitted for review");
 82          Box::new(ModerationState)
 83      }
 84
 85      fn approve(&self) -> Box<dyn DocumentState> {
 86          println!("  [Moderation] Moderator approving document...");
 87          println!("  [Moderation -> Approved] Document approved and ready for publishing");
 88          Box::new(ApprovedState)
 89      }
 90
 91      fn reject(&self) -> Box<dyn DocumentState> {
 92          println!("  [Moderation] Moderator rejecting document...");
 93          println!("  [Moderation -> Draft] Document rejected - returned to draft");
 94          Box::new(DraftState)
 95      }
 96
 97      fn publish(&self) -> Box<dyn DocumentState> {
 98          println!("  [Moderation] Cannot publish - document must be approved first");
 99          Box::new(ModerationState)
100      }
101
102      fn get_state_name(&self) -> &str {
103          "Moderation"
104      }
105  }
106
107  // Approved State - Document is approved and ready to publish
108  struct ApprovedState;
109
110  impl fmt::Display for ApprovedState {
111      fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
112          write!(f, "Approved")
113      }
114  }
115
116  impl DocumentState for ApprovedState {
117      fn edit(&self, _content: &str) -> (Box<dyn DocumentState>, Option<String>) {
118          println!("  [Approved] Cannot edit - document is already approved");
119          (Box::new(ApprovedState), None)
120      }
121
122      fn submit(&self) -> Box<dyn DocumentState> {
123          println!("  [Approved] Document already approved - no need to submit");
124          Box::new(ApprovedState)
125      }
126
127      fn approve(&self) -> Box<dyn DocumentState> {
128          println!("  [Approved] Document already approved");
129          Box::new(ApprovedState)
130      }
131
132      fn reject(&self) -> Box<dyn DocumentState> {
133          println!("  [Approved] Revoking approval...");
134          println!("  [Approved -> Draft] Approval revoked - returned to draft");
135          Box::new(DraftState)
136      }
137
138      fn publish(&self) -> Box<dyn DocumentState> {
139          println!("  [Approved] Publishing document...");
140          println!("  [Approved -> Published] Document is now live!");
141          Box::new(PublishedState)
142      }
143
144      fn get_state_name(&self) -> &str {
145          "Approved"
146      }
147  }
148
149  // Published State - Document is live
150  struct PublishedState;
151
152  impl fmt::Display for PublishedState {
153      fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
154          write!(f, "Published")
155      }
156  }
157
158  impl DocumentState for PublishedState {
159      fn edit(&self, _content: &str) -> (Box<dyn DocumentState>, Option<String>) {
160          println!("  [Published] Cannot edit - document is already published");
161          (Box::new(PublishedState), None)
162      }
163
164      fn submit(&self) -> Box<dyn DocumentState> {
165          println!("  [Published] Document already published");
166          Box::new(PublishedState)
167      }
168
169      fn approve(&self) -> Box<dyn DocumentState> {
170          println!("  [Published] Document already published");
171          Box::new(PublishedState)
172      }
173
174      fn reject(&self) -> Box<dyn DocumentState> {
175          println!("  [Published] Unpublishing document...");
176          println!("  [Published -> Draft] Document unpublished - returned to draft");
177          Box::new(DraftState)
178      }
179
180      fn publish(&self) -> Box<dyn DocumentState> {
181          println!("  [Published] Document is already published");
182          Box::new(PublishedState)
183      }
184
185      fn get_state_name(&self) -> &str {
186          "Published"
187      }
188  }
189
190  // =============================================================================
191  // Context - Document that holds state and delegates operations
192  // =============================================================================
193
194  struct Document {
195      title: String,
196      content: String,
197      state: Box<dyn DocumentState>,
198  }
199
200  impl Document {
201      fn new(title: &str) -> Self {
202          println!("Creating new document: '{}'", title);
203          println!("  Initial state: Draft");
204          Document {
205              title: title.to_string(),
206              content: String::new(),
207              state: Box::new(DraftState),
208          }
209      }
210
211      fn edit(&mut self, content: &str) {
212          println!("\nAction: Edit document");
213          let (new_state, new_content) = self.state.edit(content);
214          self.state = new_state;
215          if let Some(c) = new_content {
216              self.content = c;
217          }
218      }
219
220      fn submit(&mut self) {
221          println!("\nAction: Submit document");
222          self.state = self.state.submit();
223      }
224
225      fn approve(&mut self) {
226          println!("\nAction: Approve document");
227          self.state = self.state.approve();
228      }
229
230      fn reject(&mut self) {
231          println!("\nAction: Reject document");
232          self.state = self.state.reject();
233      }
234
235      fn publish(&mut self) {
236          println!("\nAction: Publish document");
237          self.state = self.state.publish();
238      }
239
240      fn status(&self) {
241          println!("\n--- Document Status ---");
242          println!("Title: {}", self.title);
243          println!("State: {}", self.state.get_state_name());
244          println!("Content: {}", if self.content.is_empty() { "(empty)" } else { &self.content });
245          println!("-----------------------");
246      }
247  }
248
249  // =============================================================================
250  // Main - Demonstrate state transitions
251  // =============================================================================
252
253  fn main() {
254      println!("=== State Design Pattern Demo ===");
255      println!("Document Workflow: Draft -> Moderation -> Approved -> Published\n");
256
257      // Create a new document (starts in Draft state)
258      let mut doc = Document::new("Rust State Pattern Guide");
259      doc.status();
260
261      // Scenario 1: Try invalid operations in Draft state
262      println!("\n>>> Scenario 1: Invalid operations in Draft state");
263      doc.approve();  // Cannot approve in Draft
264      doc.publish();  // Cannot publish in Draft
265
266      // Scenario 2: Valid workflow - edit and submit
267      println!("\n>>> Scenario 2: Edit and submit document");
268      doc.edit("This is the initial content about the State pattern.");
269      doc.submit();
270      doc.status();
271
272      // Scenario 3: Try to edit while in Moderation
273      println!("\n>>> Scenario 3: Try to edit during moderation");
274      doc.edit("Trying to change content...");
275
276      // Scenario 4: Reject and return to Draft
277      println!("\n>>> Scenario 4: Reject document");
278      doc.reject();
279      doc.status();
280
281      // Scenario 5: Edit, resubmit, and approve
282      println!("\n>>> Scenario 5: Revise, resubmit, and approve");
283      doc.edit("Revised content with improvements.");
284      doc.submit();
285      doc.approve();
286      doc.status();
287
288      // Scenario 6: Publish the approved document
289      println!("\n>>> Scenario 6: Publish document");
290      doc.publish();
291      doc.status();
292
293      // Scenario 7: Try operations on published document
294      println!("\n>>> Scenario 7: Operations on published document");
295      doc.edit("Cannot change published content");
296      doc.approve();
297
298      // Scenario 8: Unpublish document
299      println!("\n>>> Scenario 8: Unpublish document");
300      doc.reject();
301      doc.status();
302
303      println!("\n=== Demo Complete ===");
304  }
```

## Program Output

```
=== State Design Pattern Demo ===
Document Workflow: Draft -> Moderation -> Approved -> Published

Creating new document: 'Rust State Pattern Guide'
  Initial state: Draft

--- Document Status ---
Title: Rust State Pattern Guide
State: Draft
Content: (empty)
-----------------------

>>> Scenario 1: Invalid operations in Draft state

Action: Approve document
  [Draft] Cannot approve - document must be submitted first

Action: Publish document
  [Draft] Cannot publish - document must go through moderation

>>> Scenario 2: Edit and submit document

Action: Edit document
  [Draft] Editing document content...
  [Draft] Content updated successfully

Action: Submit document
  [Draft] Submitting document for moderation...
  [Draft -> Moderation] Document submitted for review

--- Document Status ---
Title: Rust State Pattern Guide
State: Moderation
Content: This is the initial content about the State pattern.
-----------------------

>>> Scenario 3: Try to edit during moderation

Action: Edit document
  [Moderation] Cannot edit - document is under review

>>> Scenario 4: Reject document

Action: Reject document
  [Moderation] Moderator rejecting document...
  [Moderation -> Draft] Document rejected - returned to draft

--- Document Status ---
Title: Rust State Pattern Guide
State: Draft
Content: This is the initial content about the State pattern.
-----------------------

>>> Scenario 5: Revise, resubmit, and approve

Action: Edit document
  [Draft] Editing document content...
  [Draft] Content updated successfully

Action: Submit document
  [Draft] Submitting document for moderation...
  [Draft -> Moderation] Document submitted for review

Action: Approve document
  [Moderation] Moderator approving document...
  [Moderation -> Approved] Document approved and ready for publishing

--- Document Status ---
Title: Rust State Pattern Guide
State: Approved
Content: Revised content with improvements.
-----------------------

>>> Scenario 6: Publish document

Action: Publish document
  [Approved] Publishing document...
  [Approved -> Published] Document is now live!

--- Document Status ---
Title: Rust State Pattern Guide
State: Published
Content: Revised content with improvements.
-----------------------

>>> Scenario 7: Operations on published document

Action: Edit document
  [Published] Cannot edit - document is already published

Action: Approve document
  [Published] Document already published

>>> Scenario 8: Unpublish document

Action: Reject document
  [Published] Unpublishing document...
  [Published -> Draft] Document unpublished - returned to draft

--- Document Status ---
Title: Rust State Pattern Guide
State: Draft
Content: Revised content with improvements.
-----------------------

=== Demo Complete ===
```

## Code Annotations

### Key Sections Explained

#### State Trait (Lines 10-17)
The `DocumentState` trait defines the interface that all concrete states must implement. Each method:
- Takes `&self` (immutable borrow of state)
- Returns a new `Box<dyn DocumentState>` for state transitions
- The `edit` method returns a tuple with new state and optional content update

This design allows states to be replaced without mutating the current state object (Rust's ownership model in action).

#### DraftState (Lines 24-63)
The initial state where documents can be edited:
- **Lines 33-37**: `edit()` allows content changes, returns new content in `Some()`
- **Lines 39-43**: `submit()` transitions to `ModerationState`
- **Lines 45-58**: `approve()`, `reject()`, `publish()` are invalid operations

#### ModerationState (Lines 66-105)
Document is under review and locked for editing:
- **Lines 75-78**: `edit()` is blocked, returns `None` for content
- **Lines 85-89**: `approve()` transitions to `ApprovedState`
- **Lines 91-95**: `reject()` returns document to `DraftState`

#### ApprovedState (Lines 108-147)
Document is approved and ready for publishing:
- **Lines 132-136**: `reject()` revokes approval, returns to `DraftState`
- **Lines 138-142**: `publish()` transitions to `PublishedState`

#### PublishedState (Lines 150-188)
Document is live and mostly immutable:
- **Lines 174-178**: `reject()` unpublishes and returns to `DraftState`
- All other operations are blocked

#### Context - Document (Lines 194-247)
The `Document` struct holds the state and delegates operations:
- **Line 197**: State is stored as `Box<dyn DocumentState>` (trait object)
- **Lines 211-218**: `edit()` method delegates to current state and updates content if returned
- **Lines 220-238**: Other methods simply delegate to state and update

### Output Correlation Table

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| `Creating new document...` | 202-203 | Document constructor prints initial state |
| `State: Draft` | 207, 243 | Initial state is `DraftState` |
| `[Draft] Cannot approve...` | 46 | Invalid operation in Draft state |
| `[Draft] Cannot publish...` | 56 | Must go through moderation first |
| `[Draft] Editing document...` | 34-35 | Valid edit in Draft state |
| `[Draft -> Moderation]` | 40-42 | State transition via `submit()` |
| `[Moderation] Cannot edit...` | 76 | Editing blocked during review |
| `[Moderation -> Draft]` | 92-94 | Rejection returns to Draft |
| `[Moderation -> Approved]` | 86-88 | Approval advances workflow |
| `[Approved -> Published]` | 139-141 | Final publish transition |
| `[Published] Cannot edit...` | 160 | Published documents are immutable |
| `[Published -> Draft]` | 175-177 | Unpublishing returns to Draft |

### Key Characteristics of State Pattern in Rust

1. **Trait Objects with Box**: States are stored as `Box<dyn DocumentState>` enabling dynamic dispatch and runtime polymorphism

2. **Ownership-Based Transitions**: Each state method returns a new state object rather than mutating in place, aligning with Rust's ownership model

3. **Type Safety**: The compiler ensures all state transitions are valid - no null states or undefined behavior

4. **Encapsulated Behavior**: Each state encapsulates its own valid/invalid operations, eliminating conditional logic in the context

5. **Extensibility**: New states can be added by implementing the `DocumentState` trait without modifying existing code

6. **Memory Safety**: Using `Box<dyn Trait>` ensures proper memory management with automatic cleanup

7. **No Global State**: Each document manages its own state independently

## Requirements

- **Rust Version**: Any stable Rust version (1.0+)
- **No external dependencies**: Uses only the standard library

## Compilation and Execution

```bash
rustc main_state.rs -o main_state && ./main_state
```
