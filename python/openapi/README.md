# OpenAPI (formerly Swagger) Python Example

This example demonstrates working with OpenAPI specifications in Python, including creating, validating, and generating specs both manually and automatically with FastAPI.

## Overview

OpenAPI (formerly known as Swagger) is a specification for describing RESTful APIs. This example shows:
- Creating OpenAPI 3.0 specifications programmatically
- Validating OpenAPI specs
- Saving specs in JSON and YAML formats
- Auto-generating OpenAPI specs with FastAPI

## Running the Example

```bash
cd python/openapi
uv run main_openapi.py
```

## Source Code

The main script demonstrates OpenAPI concepts in several steps:

### Step 1: Creating an OpenAPI Specification (Lines 32-197)

```python
32: def create_openapi_spec() -> dict[str, Any]:
33:     """Create a sample OpenAPI 3.0 specification."""
34:     # Line 32: Define a complete OpenAPI 3.0 specification
35:     spec = {
36:         "openapi": "3.0.3",
37:         "info": {
38:             "title": "Pet Store API",
39:             "description": "A sample API demonstrating OpenAPI specification",
40:             "version": "1.0.0",
...
48:         "servers": [
49:             {
50:                 "url": "https://api.petstore.com/v1",
51:                 "description": "Production server"
52:             }
53:         ],
54:         "paths": {
55:             "/pets": {
56:                 "get": {
57:                     "summary": "List all pets",
58:                     "operationId": "listPets",
...
```

**Annotation**: Lines 32-197 define a complete OpenAPI 3.0 specification including API metadata (info), server URLs, endpoints (paths), and reusable components (schemas).

### Step 2: Validating the Specification (Lines 199-200)

```python
199: def validate_openapi_spec(spec: dict[str, Any]) -> bool:
200:     """Validate an OpenAPI specification."""
201:     try:
202:         # Line 205: Validate the spec using openapi-spec-validator
203:         validate(spec)
204:         print("✓ OpenAPI specification is valid!")
205:         return True
206:     except Exception as e:
207:         print(f"✗ Validation failed: {e}")
208:         return False
```

**Annotation**: The `openapi-spec-validator` library ensures the spec conforms to OpenAPI 3.0 standards.

### Step 3: Saving in Multiple Formats (Lines 203-217)

```python
203: def save_spec_formats(spec: dict[str, Any]) -> None:
204:     """Save the OpenAPI spec in both JSON and YAML formats."""
205:     output_dir = Path(".")
206:
207:     # Line 218: Save as JSON
208:     json_path = output_dir / "petstore_openapi.json"
209:     with open(json_path, "w") as f:
210:         json.dump(spec, f, indent=2)
211:     print(f"✓ Saved JSON spec to: {json_path}")
212:
213:     # Line 224: Save as YAML
214:     yaml_path = output_dir / "petstore_openapi.yaml"
215:     with open(yaml_path, "w") as f:
216:         yaml.dump(spec, f, default_flow_style=False, sort_keys=False)
217:     print(f"✓ Saved YAML spec to: {yaml_path}")
```

**Annotation**: OpenAPI specs can be expressed in both JSON and YAML formats. This function saves the same specification in both formats.

### Step 4: FastAPI Auto-Generation (Lines 248-306)

```python
248: def demonstrate_fastapi_integration() -> None:
249:     """Show how FastAPI automatically generates OpenAPI specs."""
250:     print_section("FastAPI Auto-Generated OpenAPI")
251:
252:     # Line 257: Import FastAPI (done here to show it's optional)
253:     from fastapi import FastAPI
254:     from pydantic import BaseModel
255:
256:     # Line 261: Define Pydantic models
257:     class Pet(BaseModel):
258:         id: int
259:         name: str
260:         tag: str | None = None
...
265:     # Line 270: Create FastAPI app
266:     app = FastAPI(
267:         title="Pet Store API (FastAPI)",
268:         description="Auto-generated OpenAPI from FastAPI",
269:         version="2.0.0"
270:     )
271:
272:     # Line 277: Define endpoints (FastAPI generates OpenAPI automatically)
273:     @app.get("/pets", response_model=list[Pet])
274:     async def list_pets(limit: int = 10):
275:         """List all pets."""
276:         return []
...
288:     # Line 295: Access the auto-generated OpenAPI spec
289:     openapi_schema = app.openapi()
```

**Annotation**: FastAPI automatically generates OpenAPI 3.0 specifications from Python type hints and Pydantic models. No manual spec writing required!

## Program Output

```
============================================================
  OpenAPI (Swagger) Demonstration
============================================================

Step 1: Creating OpenAPI 3.0 Specification
------------------------------------------------------------
API Title: Pet Store API
Version: 1.0.0
OpenAPI Version: 3.0.3

Endpoints:
  GET /pets
    Operation: listPets
    Summary: List all pets
  POST /pets
    Operation: createPet
    Summary: Create a pet
  GET /pets/{petId}
    Operation: getPetById
    Summary: Get a pet by ID

Data Models:
  - Pet
  - NewPet

------------------------------------------------------------
Step 2: Validating OpenAPI Specification
------------------------------------------------------------
✓ OpenAPI specification is valid!

------------------------------------------------------------
Step 3: Saving Specification (JSON & YAML)
------------------------------------------------------------
✓ Saved JSON spec to: petstore_openapi.json
✓ Saved YAML spec to: petstore_openapi.yaml

============================================================
  FastAPI Auto-Generated OpenAPI
============================================================

FastAPI automatically generates OpenAPI 3.0 specs!
Title: Pet Store API (FastAPI)
Version: 2.0.0

Auto-detected endpoints:
  GET /pets
  POST /pets
  GET /pets/{pet_id}

✓ FastAPI integrates OpenAPI natively!
  - Access spec at: http://localhost:8000/openapi.json
  - Interactive docs at: http://localhost:8000/docs
  - Alternative docs at: http://localhost:8000/redoc

============================================================
  Summary
============================================================

OpenAPI (formerly Swagger) provides:
  ✓ Standardized API documentation format
  ✓ Language-agnostic API descriptions
  ✓ Auto-generated interactive documentation
  ✓ Code generation for clients and servers
  ✓ API validation and testing tools

Modern frameworks like FastAPI generate OpenAPI specs automatically!
```

## Output Annotations

### Lines 1-26 (Step 1 Output)
The program successfully creates a Pet Store API specification with:
- 3 endpoints (GET /pets, POST /pets, GET /pets/{petId})
- 2 data models (Pet, NewPet)
- This correlates with the specification defined at **source lines 32-197**

### Lines 30-31 (Step 2 Output)
The `openapi-spec-validator` successfully validates the specification, confirming it meets OpenAPI 3.0 standards. This uses the validation function at **source lines 199-208**.

### Lines 35-37 (Step 3 Output)
The specification is saved in both JSON and YAML formats as `petstore_openapi.json` and `petstore_openapi.yaml`. This is handled by the function at **source lines 203-217**.

### Lines 41-56 (Step 4 Output)
FastAPI automatically generates an OpenAPI spec from Python code with type hints:
- The Pydantic models at **source lines 257-264** define the data structures
- The endpoint decorators at **source lines 273-287** define the API operations
- FastAPI creates the spec automatically via `app.openapi()` at **source line 289**
- The generated spec is accessible at `/openapi.json` and includes interactive documentation at `/docs` (Swagger UI) and `/redoc` (ReDoc)

## Key Concepts

1. **Manual Specification**: Creating OpenAPI specs as Python dictionaries (old Swagger approach)
2. **Validation**: Using `openapi-spec-validator` to ensure spec correctness
3. **Format Flexibility**: Specs can be JSON or YAML (both are valid)
4. **Modern Approach**: FastAPI auto-generates specs from Python code, eliminating manual spec writing

## Version Requirements

- **Python**: 3.10+ (required for modern type hints like `str | None`)
- **Dependencies**:
  - `openapi-spec-validator`: For validating OpenAPI specs
  - `pyyaml`: For YAML format support
  - `fastapi`: For auto-generated OpenAPI specs
  - `pydantic>=2.0`: For data validation with FastAPI

## Historical Context

**Swagger** was the original name of the specification. In 2016, the specification was renamed to **OpenAPI** when it was donated to the OpenAPI Initiative under the Linux Foundation. The term "Swagger" now refers to the tooling ecosystem (Swagger UI, Swagger Editor, etc.) rather than the specification itself.
