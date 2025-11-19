# Prototype Design Pattern

The Prototype pattern creates new objects by cloning existing instances rather than creating new instances from scratch. This is useful when object creation is expensive or when objects have many shared configurations.

## How to Run

```bash
uv run python main_prototype.py
```

## Key Source Code

### Abstract Prototype (lines 19-25)

Defines the cloning interface that all prototypes must implement:

```python
19: class Prototype(ABC):
20:     """Abstract base class for prototypes."""
21:
22:     @abstractmethod
23:     def clone(self) -> Prototype:
24:         """Create a copy of the object."""
25:         pass
```

### Document Prototype with Deep/Shallow Clone (lines 40-62)

```python
40: @dataclass
41: class Document(Prototype):
42:     """Concrete prototype representing a document."""
43:
44:     title: str
45:     content: str
46:     author: str
47:     tags: list[str] = field(default_factory=list)
48:     metadata: dict[str, str] = field(default_factory=dict)
49:
50:     def clone(self) -> Document:
51:         """Create a deep copy of the document."""
52:         return copy.deepcopy(self)  # Deep copy: all nested objects copied
53:
54:     def shallow_clone(self) -> Document:
55:         """Create a shallow copy of the document."""
56:         return copy.copy(self)  # Shallow copy: shares mutable objects
```

### Employee with Nested Address (lines 65-90)

Demonstrates deep cloning of complex nested objects:

```python
65: @dataclass
66: class Employee(Prototype):
67:     """Concrete prototype representing an employee."""
68:
69:     name: str
70:     position: str
71:     department: str
72:     salary: float
73:     address: Address  # Nested object
74:     skills: list[str] = field(default_factory=list)
75:
76:     def clone(self) -> Employee:
77:         """Create a deep copy of the employee."""
78:         return copy.deepcopy(self)  # Address is also deep copied
```

### Prototype Registry (lines 93-116)

Manages named prototypes for convenient cloning:

```python
93: class PrototypeRegistry:
94:     """Registry to store and retrieve prototype instances."""
95:
96:     def __init__(self) -> None:
97:         self._prototypes: dict[str, Prototype] = {}
98:
99:     def register(self, name: str, prototype: Prototype) -> None:
100:        """Register a prototype with a given name."""
101:        self._prototypes[name] = prototype
...
107:    def clone(self, name: str) -> Prototype:
108:        """Clone a registered prototype by name."""
109:        prototype = self._prototypes.get(name)
110:        if prototype is None:
111:            raise ValueError(f"Prototype '{name}' not found in registry")
112:        return prototype.clone()
```

### Deep Copy vs Shallow Copy Demo (lines 163-172)

```python
163:    shallow = base_doc.shallow_clone()
164:    deep = base_doc.clone()
165:
166:    # Modify the shallow clone's mutable attributes
167:    shallow.tags.append("shallow-modified")
168:
169:    print(f"Base tags after shallow clone modification: {base_doc.tags}")
170:    print(f"Shallow clone tags: {shallow.tags}")
171:    print(f"Deep clone tags: {deep.tags}")
```

## Program Output

```
============================================================
PROTOTYPE DESIGN PATTERN DEMONSTRATION
============================================================

[1] Document Cloning Example:
----------------------------------------
Original: Document(title='Design Patterns Guide', author='John Doe', tags=['programming', 'design', 'patterns'], metadata={'version': '1.0', 'status': 'draft'})
Original ID: 139283229781328

Cloned:   Document(title='Design Patterns Guide (Copy)', author='John Doe', tags=['programming', 'design', 'patterns', 'cloned'], metadata={'version': '1.0', 'status': 'review'})
Cloned ID: 139283229782672

Original after clone modification: Document(title='Design Patterns Guide', author='John Doe', tags=['programming', 'design', 'patterns'], metadata={'version': '1.0', 'status': 'draft'})
→ Note: Original remains unchanged (deep copy)

[2] Shallow vs Deep Clone Comparison:
----------------------------------------
Base tags after shallow clone modification: ['base', 'shallow-modified']
Shallow clone tags: ['base', 'shallow-modified']
Deep clone tags: ['base']
→ Shallow clone shares mutable objects with original!

[3] Employee Cloning with Nested Objects:
----------------------------------------
Original Employee:
Employee:
    Name: Alice Johnson
    Position: Senior Developer
    Department: Engineering
    Salary: $120,000.00
    Address: 123 Tech Street, San Francisco, USA
    Skills: Python, Java, Kubernetes

Cloned Employee (modified):
Employee:
    Name: Bob Wilson
    Position: Developer
    Department: Engineering
    Salary: $95,000.00
    Address: 456 Code Avenue, San Francisco, USA
    Skills: Python, Java, Kubernetes, Docker

Original Employee (unchanged):
Employee:
    Name: Alice Johnson
    Position: Senior Developer
    Department: Engineering
    Salary: $120,000.00
    Address: 123 Tech Street, San Francisco, USA
    Skills: Python, Java, Kubernetes
→ Nested Address object was also deep copied

[4] Prototype Registry Pattern:
----------------------------------------
Registered prototypes: ['junior-dev', 'senior-dev']

New hire from 'junior-dev' template:
Employee:
    Name: Charlie Brown
    Position: Junior Developer
    Department: Engineering
    Salary: $70,000.00
    Address: Office, Boston, USA
    Skills: Git, Python

New hire from 'senior-dev' template:
Employee:
    Name: Diana Prince
    Position: Senior Developer
    Department: Engineering
    Salary: $130,000.00
    Address: Office, New York, USA
    Skills: Python, Architecture, Leadership, Cloud Architecture

============================================================
Key Benefits of Prototype Pattern:
============================================================
• Avoids expensive object creation from scratch
• Enables runtime object creation without knowing exact class
• Reduces subclassing by cloning configured instances
• Deep copy ensures complete independence of cloned objects
• Registry pattern provides convenient prototype management
============================================================
```

## Output Analysis

### Output Correlation with Source Code

| Output Section | Source Lines | Description |
|----------------|--------------|-------------|
| Document clone IDs | 137-138 | Different object IDs prove new object created |
| Original unchanged | 148-149 | Deep copy (line 52) ensures independence |
| Shallow clone issue | 169-172 | Shallow copy (line 56) shares the tags list |
| Nested Address cloned | 195, 202 | Deep copy handles nested objects (line 78) |
| Registry cloning | 239-251 | Clone from registry (lines 107-112) |

### Key Observations

1. **Object Identity (output lines with IDs)**: The cloned document has a different `id()`, proving `copy.deepcopy()` (line 52) creates a new object

2. **Deep vs Shallow (Section 2 output)**:
   - Line 163: `shallow_clone()` uses `copy.copy()` - tags list is shared
   - Line 164: `clone()` uses `copy.deepcopy()` - tags list is independent
   - Output shows base_doc.tags contains "shallow-modified" after modifying shallow clone

3. **Nested Object Independence (Section 3)**:
   - Line 195: `cloned_emp.address.street = "456 Code Avenue"`
   - Original employee's address remains "123 Tech Street"
   - `copy.deepcopy()` (line 78) recursively copies the Address object

4. **Registry Pattern (Section 4)**:
   - Lines 212-234: Register template prototypes
   - Lines 239-251: Clone and customize without affecting templates
   - This avoids creating complex objects from scratch each time

## Requirements

- Python >= 3.10 (uses modern type hints with `list[str]` and `dict[str, str]` syntax)
