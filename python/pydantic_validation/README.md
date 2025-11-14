# Pydantic Validation Example

This example demonstrates comprehensive validation features in **Pydantic v2**, a powerful data validation library for Python.

## Requirements

- **Python**: 3.8 or higher
- **Pydantic**: 2.0 or higher (automatically installed via inline script metadata)

## Running the Example

```bash
uv run main_pydantic_validation.py
```

The script uses inline script metadata to automatically install required dependencies (`pydantic>=2.0` and `pydantic[email]>=2.0`).

## Features Demonstrated

1. **Basic Type Validation** - Automatic type checking and coercion
2. **Field Constraints** - Min/max length, value ranges, regex patterns
3. **Custom Field Validators** - Custom validation logic with decorators
4. **Model Validators** - Cross-field validation at the model level
5. **Optional Fields and Defaults** - Handling optional data with default values
6. **Nested Models** - Validating complex nested data structures
7. **Comprehensive Error Handling** - Detailed validation error reporting

---

## Source Code and Output

### 1. Basic Type Validation

**Source Code** (Lines 23-26):
```python
23: class BasicUser(BaseModel):
24:     """Simple user model with basic type validation"""
25:     name: str
26:     age: int
27:     email: str
```

**Source Code** (Lines 34-36):
```python
34:     # Valid data
35:     user = BasicUser(name="Alice", age=30, email="alice@example.com")
36:     print(f"✓ Valid user created: {user}")
```

**Output**:
```
✓ Valid user created: name='Alice' age=30 email='alice@example.com'
  Name: Alice, Age: 30, Email: alice@example.com
```

**Annotation**: Lines 23-27 define a basic Pydantic model with type hints. Line 35 creates an instance with valid data, and Pydantic automatically validates the types.

---

**Source Code** (Lines 39-41):
```python
39:     # Type coercion - string to int
40:     user2 = BasicUser(name="Bob", age="25", email="bob@example.com")
41:     print(f"\n✓ Type coercion works - age='25' (str) → {user2.age} (int)")
```

**Output**:
```
✓ Type coercion works - age='25' (str) → 25 (int)
```

**Annotation**: Line 40 demonstrates Pydantic's automatic type coercion - the string `"25"` is automatically converted to integer `25`.

---

**Source Code** (Lines 43-49):
```python
43:     # Validation error - invalid type
44:     try:
45:         user3 = BasicUser(name="Charlie", age="invalid", email="charlie@example.com")
46:     except ValidationError as e:
47:         print(f"\n✗ Validation failed for age='invalid':")
48:         print(f"  Error count: {e.error_count()}")
49:         print(f"  Error: {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Validation failed for age='invalid':
  Error count: 1
  Error: Input should be a valid integer, unable to parse string as an integer
```

**Annotation**: Line 45 attempts to pass `"invalid"` as age. Pydantic raises a `ValidationError` because it cannot convert this string to an integer. Line 48 shows how to access the error count and line 49 retrieves the error message.

---

### 2. Field Constraints

**Source Code** (Lines 55-61):
```python
55: class ConstrainedUser(BaseModel):
56:     """User model with field constraints"""
57:     name: str = Field(min_length=2, max_length=50)
58:     age: int = Field(ge=0, le=150)  # ge: greater than or equal, le: less than or equal
59:     email: EmailStr  # Built-in email validation
60:     score: float = Field(gt=0.0, lt=100.0)  # gt: greater than, lt: less than
61:     username: str = Field(pattern=r"^[a-zA-Z0-9_]+$")  # Regex pattern
```

**Annotation**: Lines 57-61 demonstrate various field constraints:
- Line 57: String length constraints (2-50 characters)
- Line 58: Numeric range constraints (0-150, inclusive)
- Line 59: Built-in email format validation
- Line 60: Strict numeric range (exclusive bounds)
- Line 61: Regex pattern validation for usernames

---

**Source Code** (Lines 68-76):
```python
68:     # Valid data
69:     user = ConstrainedUser(
70:         name="Alice Johnson",
71:         age=30,
72:         email="alice@example.com",
73:         score=85.5,
74:         username="alice_123"
75:     )
76:     print(f"✓ Valid user: {user.name}, score={user.score}")
```

**Output**:
```
✓ Valid user: Alice Johnson, score=85.5
```

**Annotation**: Lines 69-75 create a valid user that satisfies all field constraints.

---

**Source Code** (Lines 78-87):
```python
78:     # Test min_length constraint
79:     try:
80:         user = ConstrainedUser(
81:             name="A",
82:             age=30,
83:             email="alice@example.com",
84:             score=85.5,
85:             username="alice"
86:         )
87:     except ValidationError as e:
88:         print(f"\n✗ Name too short ('A'):")
89:         print(f"  {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Name too short ('A'):
  String should have at least 2 characters
```

**Annotation**: Line 81 violates the `min_length=2` constraint from line 57, triggering a validation error.

---

**Source Code** (Lines 91-100):
```python
91:     # Test age constraint
92:     try:
93:         user = ConstrainedUser(
94:             name="Alice",
95:             age=200,
96:             email="alice@example.com",
97:             score=85.5,
98:             username="alice"
99:         )
100:     except ValidationError as e:
101:         print(f"\n✗ Age too high (200):")
102:         print(f"  {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Age too high (200):
  Input should be less than or equal to 150
```

**Annotation**: Line 95 violates the `le=150` (less than or equal) constraint from line 58.

---

**Source Code** (Lines 104-113):
```python
104:     # Test email validation
105:     try:
106:         user = ConstrainedUser(
107:             name="Alice",
108:             age=30,
109:             email="invalid-email",
110:             score=85.5,
111:             username="alice"
112:         )
113:     except ValidationError as e:
114:         print(f"\n✗ Invalid email format ('invalid-email'):")
115:         print(f"  {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Invalid email format ('invalid-email'):
  value is not a valid email address: An email address must have an @-sign.
```

**Annotation**: Line 109 provides an invalid email format. The `EmailStr` type from line 59 validates email format and requires an @ symbol.

---

**Source Code** (Lines 117-126):
```python
117:     # Test pattern validation
118:     try:
119:         user = ConstrainedUser(
120:             name="Alice",
121:             age=30,
122:             email="alice@example.com",
123:             score=85.5,
124:             username="alice-invalid!"
125:         )
126:     except ValidationError as e:
127:         print(f"\n✗ Username contains invalid characters ('alice-invalid!'):")
128:         print(f"  {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Username contains invalid characters ('alice-invalid!'):
  String should match pattern '^[a-zA-Z0-9_]+$'
```

**Annotation**: Line 124 contains invalid characters (`-` and `!`) that don't match the regex pattern from line 61, which only allows letters, numbers, and underscores.

---

### 3. Custom Field Validators

**Source Code** (Lines 134-152):
```python
134: class Product(BaseModel):
135:     """Product model with custom field validators"""
136:     name: str
137:     price: float
138:     quantity: int
139:     sku: str
140:
141:     @field_validator('name')
142:     @classmethod
143:     def name_must_not_be_empty(cls, v: str) -> str:
144:         """Validate that name is not just whitespace"""
145:         if not v.strip():
146:             raise ValueError('Name cannot be empty or just whitespace')
147:         return v.strip().title()  # Clean and capitalize
148:
149:     @field_validator('price')
150:     @classmethod
151:     def price_must_be_positive(cls, v: float) -> float:
152:         """Validate that price is positive"""
153:         if v <= 0:
154:             raise ValueError('Price must be positive')
155:         return round(v, 2)  # Round to 2 decimal places
156:
157:     @field_validator('sku')
158:     @classmethod
159:     def sku_must_be_uppercase(cls, v: str) -> str:
160:         """Convert SKU to uppercase"""
161:         return v.upper()
```

**Annotation**:
- Lines 141-147: Custom validator for `name` that checks for empty strings and transforms the value by trimming whitespace and capitalizing
- Lines 149-155: Custom validator for `price` that ensures positive values and rounds to 2 decimal places
- Lines 157-161: Custom validator for `sku` that transforms to uppercase

---

**Source Code** (Lines 168-177):
```python
168:     # Valid product with transformations
169:     product = Product(
170:         name="  laptop computer  ",
171:         price=999.999,
172:         quantity=10,
173:         sku="prod-123"
174:     )
175:     print(f"✓ Product created with transformations:")
176:     print(f"  Name: '{product.name}' (trimmed and titled)")
177:     print(f"  Price: ${product.price} (rounded to 2 decimals)")
178:     print(f"  SKU: '{product.sku}' (uppercase)")
```

**Output**:
```
✓ Product created with transformations:
  Name: 'Laptop Computer' (trimmed and titled)
  Price: $1000.0 (rounded to 2 decimals)
  SKU: 'PROD-123' (uppercase)
```

**Annotation**: The validators transform the input data:
- Line 170 → "Laptop Computer" (line 147 strips and titles)
- Line 171 → 1000.0 (line 155 rounds to 2 decimals)
- Line 173 → "PROD-123" (line 161 converts to uppercase)

---

**Source Code** (Lines 180-185):
```python
180:     # Test empty name
181:     try:
182:         product = Product(name="   ", price=100, quantity=5, sku="SKU-001")
183:     except ValidationError as e:
184:         print(f"\n✗ Empty name validation:")
185:         print(f"  {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Empty name validation:
  Value error, Name cannot be empty or just whitespace
```

**Annotation**: Line 182 provides whitespace-only name. The validator at line 145 detects this and raises the custom error from line 146.

---

**Source Code** (Lines 187-192):
```python
187:     # Test negative price
188:     try:
189:         product = Product(name="Mouse", price=-10, quantity=5, sku="SKU-002")
190:     except ValidationError as e:
191:         print(f"\n✗ Negative price validation:")
192:         print(f"  {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Negative price validation:
  Value error, Price must be positive
```

**Annotation**: Line 189 provides a negative price. The validator at line 153 checks for this and raises the custom error from line 154.

---

### 4. Model Validators

**Source Code** (Lines 198-217):
```python
198: class Order(BaseModel):
199:     """Order model with model-level validation"""
200:     order_id: str
201:     items_count: int
202:     total_price: float
203:     discount: float = 0.0
204:     final_price: Optional[float] = None
205:
206:     @model_validator(mode='after')
207:     def calculate_final_price(self) -> 'Order':
208:         """Calculate final price after discount"""
209:         if self.discount > self.total_price:
210:             raise ValueError('Discount cannot exceed total price')
211:
212:         if self.discount < 0:
213:             raise ValueError('Discount cannot be negative')
214:
215:         # Calculate final price
216:         self.final_price = self.total_price - self.discount
217:         return self
218:
219:     @model_validator(mode='after')
220:     def validate_items_and_price(self) -> 'Order':
221:         """Ensure items count matches price logic"""
222:         if self.items_count <= 0:
223:             raise ValueError('Order must have at least one item')
224:
225:         if self.total_price <= 0:
226:             raise ValueError('Total price must be positive')
227:
228:         return self
```

**Annotation**:
- Lines 206-217: Model validator that performs cross-field validation (checking discount vs. total_price) and calculates the final_price automatically
- Lines 219-228: Additional model validator that ensures business logic constraints are met

---

**Source Code** (Lines 235-243):
```python
235:     # Valid order
236:     order = Order(
237:         order_id="ORD-001",
238:         items_count=3,
239:         total_price=150.0,
240:         discount=15.0
241:     )
242:     print(f"✓ Order created:")
243:     print(f"  Order ID: {order.order_id}")
244:     print(f"  Total: ${order.total_price}, Discount: ${order.discount}")
245:     print(f"  Final Price: ${order.final_price} (calculated automatically)")
```

**Output**:
```
✓ Order created:
  Order ID: ORD-001
  Total: $150.0, Discount: $15.0
  Final Price: $135.0 (calculated automatically)
```

**Annotation**: The model validator at line 216 automatically calculates `final_price` as $135.0 ($150.0 - $15.0), even though it wasn't provided in the input (lines 236-241).

---

**Source Code** (Lines 247-255):
```python
247:     # Test discount exceeds total
248:     try:
249:         order = Order(
250:             order_id="ORD-002",
251:             items_count=2,
252:             total_price=100.0,
253:             discount=150.0
254:         )
255:     except ValidationError as e:
256:         print(f"\n✗ Discount exceeds total price:")
257:         print(f"  {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Discount exceeds total price:
  Value error, Discount cannot exceed total price
```

**Annotation**: Line 253 provides a discount ($150) greater than total price ($100). The validator at line 209 catches this and raises the error from line 210.

---

**Source Code** (Lines 259-267):
```python
259:     # Test negative items count
260:     try:
261:         order = Order(
262:             order_id="ORD-003",
263:             items_count=0,
264:             total_price=100.0,
265:             discount=10.0
266:         )
267:     except ValidationError as e:
268:         print(f"\n✗ Invalid items count (0):")
269:         print(f"  {e.errors()[0]['msg']}")
```

**Output**:
```
✗ Invalid items count (0):
  Value error, Order must have at least one item
```

**Annotation**: Line 263 provides 0 items. The validator at line 222 checks for this and raises the error from line 223.

---

### 5. Optional Fields and Defaults

**Source Code** (Lines 275-282):
```python
275: class UserProfile(BaseModel):
276:     """User profile with optional fields and defaults"""
277:     username: str
278:     email: EmailStr
279:     full_name: Optional[str] = None
280:     age: Optional[int] = None
281:     is_active: bool = True
282:     created_at: datetime = Field(default_factory=datetime.now)
283:     tags: list[str] = Field(default_factory=list)
284:     metadata: dict[str, str] = Field(default_factory=dict)
```

**Annotation**:
- Lines 277-278: Required fields (must be provided)
- Lines 279-280: Optional fields with None as default
- Line 281: Boolean with explicit default value
- Line 282: Dynamic default using `default_factory` (calls datetime.now())
- Lines 283-284: Collections with empty defaults using `default_factory`

---

**Source Code** (Lines 291-297):
```python
291:     # Minimal profile
292:     profile1 = UserProfile(username="alice", email="alice@example.com")
293:     print(f"✓ Minimal profile:")
294:     print(f"  Username: {profile1.username}")
295:     print(f"  Full name: {profile1.full_name} (optional, not provided)")
296:     print(f"  Is active: {profile1.is_active} (default=True)")
297:     print(f"  Tags: {profile1.tags} (default empty list)")
```

**Output**:
```
✓ Minimal profile:
  Username: alice
  Full name: None (optional, not provided)
  Is active: True (default=True)
  Tags: [] (default empty list)
```

**Annotation**: Line 292 only provides required fields. Pydantic automatically applies defaults from lines 279-284.

---

**Source Code** (Lines 299-310):
```python
299:     # Full profile
300:     profile2 = UserProfile(
301:         username="bob",
302:         email="bob@example.com",
303:         full_name="Bob Smith",
304:         age=35,
305:         is_active=False,
306:         tags=["admin", "developer"],
307:         metadata={"department": "Engineering"}
308:     )
309:     print(f"\n✓ Full profile:")
310:     print(f"  Username: {profile2.username}")
311:     print(f"  Full name: {profile2.full_name}")
312:     print(f"  Age: {profile2.age}")
313:     print(f"  Is active: {profile2.is_active}")
314:     print(f"  Tags: {profile2.tags}")
315:     print(f"  Metadata: {profile2.metadata}")
```

**Output**:
```
✓ Full profile:
  Username: bob
  Full name: Bob Smith
  Age: 35
  Is active: False
  Tags: ['admin', 'developer']
  Metadata: {'department': 'Engineering'}
```

**Annotation**: Lines 300-308 provide all fields explicitly, overriding the defaults.

---

### 6. Nested Models

**Source Code** (Lines 321-333):
```python
321: class Address(BaseModel):
322:     """Address model"""
323:     street: str
324:     city: str
325:     state: str = Field(pattern=r"^[A-Z]{2}$")
326:     zip_code: str = Field(pattern=r"^\d{5}$")
327:
328:
329: class Company(BaseModel):
330:     """Company with nested address"""
331:     name: str
332:     address: Address
333:     employees: list[str] = Field(min_length=1)
```

**Annotation**:
- Lines 321-326: `Address` model with regex validation for state (2 uppercase letters) and zip_code (5 digits)
- Lines 329-333: `Company` model that includes nested `Address` model at line 332

---

**Source Code** (Lines 340-353):
```python
340:     # Valid nested model
341:     company = Company(
342:         name="Tech Corp",
343:         address=Address(
344:             street="123 Main St",
345:             city="San Francisco",
346:             state="CA",
347:             zip_code="94105"
348:         ),
349:         employees=["Alice", "Bob", "Charlie"]
350:     )
351:     print(f"✓ Company created:")
352:     print(f"  Name: {company.name}")
353:     print(f"  Address: {company.address.street}, {company.address.city}, {company.address.state}")
354:     print(f"  Employees: {company.employees}")
```

**Output**:
```
✓ Company created:
  Name: Tech Corp
  Address: 123 Main St, San Francisco, CA
  Employees: ['Alice', 'Bob', 'Charlie']
```

**Annotation**: Lines 343-348 create a nested `Address` object that is validated according to the Address model definition (lines 321-326).

---

**Source Code** (Lines 356-368):
```python
356:     # Invalid nested address
357:     try:
358:         company = Company(
359:             name="Tech Corp",
360:             address=Address(
361:                 street="123 Main St",
362:                 city="San Francisco",
363:                 state="California",  # Should be 2 letters
364:                 zip_code="94105"
365:             ),
366:             employees=["Alice"]
367:         )
368:     except ValidationError as e:
369:         print(f"\n✗ Invalid state format ('California'):")
370:         print(f"  {e.errors()[0]['msg']}")
371:         print(f"  Location: {' -> '.join(str(x) for x in e.errors()[0]['loc'])}")
```

**Output**:
```
✗ Invalid state format ('California'):
  String should match pattern '^[A-Z]{2}$'
  Location: state
```

**Annotation**: Line 363 provides "California" which doesn't match the 2-letter pattern from line 325. Note how the error location identifies the specific nested field.

---

**Source Code** (Lines 373-385):
```python
373:     # Invalid zip code
374:     try:
375:         company = Company(
376:             name="Tech Corp",
377:             address=Address(
378:                 street="123 Main St",
379:                 city="San Francisco",
380:                 state="CA",
381:                 zip_code="9410"  # Should be 5 digits
382:             ),
383:             employees=["Alice"]
384:         )
385:     except ValidationError as e:
386:         print(f"\n✗ Invalid zip code format ('9410'):")
387:         print(f"  {e.errors()[0]['msg']}")
388:         print(f"  Location: {' -> '.join(str(x) for x in e.errors()[0]['loc'])}")
```

**Output**:
```
✗ Invalid zip code format ('9410'):
  String should match pattern '^\d{5}$'
  Location: zip_code
```

**Annotation**: Line 381 provides "9410" (4 digits) which doesn't match the 5-digit pattern from line 326.

---

### 7. Comprehensive Error Handling

**Source Code** (Lines 394-402):
```python
394: class ComplexModel(BaseModel):
395:     """Model to demonstrate comprehensive error handling"""
396:     model_config = ConfigDict(str_strip_whitespace=True)
397:
398:     id: int = Field(gt=0)
399:     name: str = Field(min_length=3, max_length=50)
400:     email: EmailStr
401:     age: int = Field(ge=18, le=100)
402:     tags: list[str] = Field(min_length=1, max_length=5)
```

**Annotation**: A complex model with multiple constraints designed to trigger multiple validation errors simultaneously.

---

**Source Code** (Lines 409-422):
```python
409:     # Multiple validation errors
410:     try:
411:         model = ComplexModel(
412:             id=-1,
413:             name="AB",
414:             email="invalid-email",
415:             age=15,
416:             tags=[]
417:         )
418:     except ValidationError as e:
419:         print(f"✗ Multiple validation errors detected:")
420:         print(f"  Total errors: {e.error_count()}")
421:         print()
422:         for i, error in enumerate(e.errors(), 1):
423:             field = error['loc'][0]
424:             msg = error['msg']
425:             input_val = error.get('input')
426:             print(f"  Error {i} - Field '{field}':")
427:             print(f"    Input: {input_val}")
428:             print(f"    Message: {msg}")
```

**Output**:
```
✗ Multiple validation errors detected:
  Total errors: 5

  Error 1 - Field 'id':
    Input: -1
    Message: Input should be greater than 0
  Error 2 - Field 'name':
    Input: AB
    Message: String should have at least 3 characters
  Error 3 - Field 'email':
    Input: invalid-email
    Message: value is not a valid email address: An email address must have an @-sign.
  Error 4 - Field 'age':
    Input: 15
    Message: Input should be greater than or equal to 18
  Error 5 - Field 'tags':
    Input: []
    Message: List should have at least 1 item after validation, not 0
```

**Annotation**: Lines 412-416 intentionally violate multiple constraints. Pydantic collects all errors and returns them together:
- Line 412: id=-1 violates `gt=0` from line 398
- Line 413: name="AB" violates `min_length=3` from line 399
- Line 414: invalid email format (line 400)
- Line 415: age=15 violates `ge=18` from line 401
- Line 416: empty list violates `min_length=1` from line 402

---

**Source Code** (Lines 430-433):
```python
430:         # Show JSON representation
431:         print(f"\n  JSON representation:")
432:         import json
433:         print(f"  {json.dumps(e.errors(), indent=4)}")
```

**Output**:
```json
  JSON representation:
  [
    {
        "type": "greater_than",
        "loc": [
            "id"
        ],
        "msg": "Input should be greater than 0",
        "input": -1,
        "ctx": {
            "gt": 0
        },
        "url": "https://errors.pydantic.dev/2.12/v/greater_than"
    },
    {
        "type": "string_too_short",
        "loc": [
            "name"
        ],
        "msg": "String should have at least 3 characters",
        "input": "AB",
        "ctx": {
            "min_length": 3
        },
        "url": "https://errors.pydantic.dev/2.12/v/string_too_short"
    },
    {
        "type": "value_error",
        "loc": [
            "email"
        ],
        "msg": "value is not a valid email address: An email address must have an @-sign.",
        "input": "invalid-email",
        "ctx": {
            "reason": "An email address must have an @-sign."
        }
    },
    {
        "type": "greater_than_equal",
        "loc": [
            "age"
        ],
        "msg": "Input should be greater than or equal to 18",
        "input": 15,
        "ctx": {
            "ge": 18
        },
        "url": "https://errors.pydantic.dev/2.12/v/greater_than_equal"
    },
    {
        "type": "too_short",
        "loc": [
            "tags"
        ],
        "msg": "List should have at least 1 item after validation, not 0",
        "input": [],
        "ctx": {
            "field_type": "List",
            "min_length": 1,
            "actual_length": 0
        },
        "url": "https://errors.pydantic.dev/2.12/v/too_short"
    }
]
```

**Annotation**: Lines 432-433 serialize the validation errors to JSON format. Each error includes:
- `type`: The error type
- `loc`: The field location
- `msg`: Human-readable error message
- `input`: The invalid input value
- `ctx`: Context information about the constraint
- `url`: Link to Pydantic documentation for that error type

---

## Key Takeaways

1. **Type Safety**: Pydantic provides automatic type validation and coercion (see lines 40-41)
2. **Rich Constraints**: Field-level constraints like min/max, patterns, and ranges (lines 57-61)
3. **Custom Logic**: Field validators for custom validation and transformation (lines 141-161)
4. **Cross-Field Validation**: Model validators for business logic across multiple fields (lines 206-228)
5. **Detailed Errors**: Comprehensive error reporting with field locations and context (lines 418-433)
6. **Default Values**: Support for optional fields and dynamic defaults (lines 279-284)
7. **Nested Validation**: Automatic validation of nested models (lines 343-348)

## Learn More

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic V2 Migration Guide](https://docs.pydantic.dev/2.0/migration/)
- [Error Handling](https://docs.pydantic.dev/latest/errors/errors/)
