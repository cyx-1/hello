#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "openapi-spec-validator",
#     "pyyaml",
#     "fastapi",
#     "pydantic>=2.0",
# ]
# ///

"""
OpenAPI (formerly Swagger) Demonstration
This script illustrates working with OpenAPI specifications in Python.
"""

import json
import yaml
from openapi_spec_validator import validate
from pathlib import Path
from typing import Any


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def create_openapi_spec() -> dict[str, Any]:
    """Create a sample OpenAPI 3.0 specification."""
    # Line 32: Define a complete OpenAPI 3.0 specification
    spec = {
        "openapi": "3.0.3",
        "info": {
            "title": "Pet Store API",
            "description": "A sample API demonstrating OpenAPI specification",
            "version": "1.0.0",
            "contact": {"name": "API Support", "email": "support@petstore.com"},
        },
        "servers": [
            {"url": "https://api.petstore.com/v1", "description": "Production server"}
        ],
        "paths": {
            "/pets": {
                "get": {
                    "summary": "List all pets",
                    "operationId": "listPets",
                    "tags": ["pets"],
                    "parameters": [
                        {
                            "name": "limit",
                            "in": "query",
                            "description": "How many items to return",
                            "required": False,
                            "schema": {
                                "type": "integer",
                                "format": "int32",
                                "default": 10,
                            },
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "A list of pets",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Pet"},
                                    }
                                }
                            },
                        }
                    },
                },
                "post": {
                    "summary": "Create a pet",
                    "operationId": "createPet",
                    "tags": ["pets"],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/NewPet"}
                            }
                        },
                    },
                    "responses": {
                        "201": {
                            "description": "Pet created successfully",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Pet"}
                                }
                            },
                        }
                    },
                },
            },
            "/pets/{petId}": {
                "get": {
                    "summary": "Get a pet by ID",
                    "operationId": "getPetById",
                    "tags": ["pets"],
                    "parameters": [
                        {
                            "name": "petId",
                            "in": "path",
                            "required": True,
                            "description": "The ID of the pet to retrieve",
                            "schema": {"type": "integer", "format": "int64"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Pet details",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Pet"}
                                }
                            },
                        },
                        "404": {"description": "Pet not found"},
                    },
                }
            },
        },
        "components": {
            "schemas": {
                "Pet": {
                    "type": "object",
                    "required": ["id", "name"],
                    "properties": {
                        "id": {
                            "type": "integer",
                            "format": "int64",
                            "description": "Unique identifier",
                        },
                        "name": {"type": "string", "description": "Pet name"},
                        "tag": {"type": "string", "description": "Optional tag"},
                    },
                },
                "NewPet": {
                    "type": "object",
                    "required": ["name"],
                    "properties": {
                        "name": {"type": "string", "description": "Pet name"},
                        "tag": {"type": "string", "description": "Optional tag"},
                    },
                },
            }
        },
    }
    return spec


def validate_openapi_spec(spec: dict[str, Any]) -> bool:
    """Validate an OpenAPI specification."""
    try:
        # Line 205: Validate the spec using openapi-spec-validator
        validate(spec)
        print("✓ OpenAPI specification is valid!")
        return True
    except Exception as e:
        print(f"✗ Validation failed: {e}")
        return False


def save_spec_formats(spec: dict[str, Any]) -> None:
    """Save the OpenAPI spec in both JSON and YAML formats."""
    output_dir = Path(".")

    # Line 218: Save as JSON
    json_path = output_dir / "petstore_openapi.json"
    with open(json_path, "w") as f:
        json.dump(spec, f, indent=2)
    print(f"✓ Saved JSON spec to: {json_path}")

    # Line 224: Save as YAML
    yaml_path = output_dir / "petstore_openapi.yaml"
    with open(yaml_path, "w") as f:
        yaml.dump(spec, f, default_flow_style=False, sort_keys=False)
    print(f"✓ Saved YAML spec to: {yaml_path}")


def display_spec_summary(spec: dict[str, Any]) -> None:
    """Display a summary of the OpenAPI specification."""
    print(f"API Title: {spec['info']['title']}")
    print(f"Version: {spec['info']['version']}")
    print(f"OpenAPI Version: {spec['openapi']}")
    print("\nEndpoints:")

    # Line 239: Iterate through paths and display operations
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            operation_id = details.get("operationId", "N/A")
            summary = details.get("summary", "N/A")
            print(f"  {method.upper()} {path}")
            print(f"    Operation: {operation_id}")
            print(f"    Summary: {summary}")

    # Line 248: Display schema components
    print("\nData Models:")
    for schema_name in spec["components"]["schemas"].keys():
        print(f"  - {schema_name}")


def demonstrate_fastapi_integration() -> None:
    """Show how FastAPI automatically generates OpenAPI specs."""
    print_section("FastAPI Auto-Generated OpenAPI")

    # Line 257: Import FastAPI (done here to show it's optional)
    from fastapi import FastAPI
    from pydantic import BaseModel

    # Line 261: Define Pydantic models
    class Pet(BaseModel):
        id: int
        name: str
        tag: str | None = None

    class NewPet(BaseModel):
        name: str
        tag: str | None = None

    # Line 270: Create FastAPI app
    app = FastAPI(
        title="Pet Store API (FastAPI)",
        description="Auto-generated OpenAPI from FastAPI",
        version="2.0.0",
    )

    # Line 277: Define endpoints (FastAPI generates OpenAPI automatically)
    @app.get("/pets", response_model=list[Pet])
    async def list_pets(limit: int = 10):
        """List all pets."""
        return []

    @app.post("/pets", response_model=Pet, status_code=201)
    async def create_pet(pet: NewPet):
        """Create a new pet."""
        return Pet(id=1, name=pet.name, tag=pet.tag)

    @app.get("/pets/{pet_id}", response_model=Pet)
    async def get_pet(pet_id: int):
        """Get a pet by ID."""
        return Pet(id=pet_id, name="Fluffy", tag="cat")

    # Line 295: Access the auto-generated OpenAPI spec
    openapi_schema = app.openapi()

    print("FastAPI automatically generates OpenAPI 3.0 specs!")
    print(f"Title: {openapi_schema['info']['title']}")
    print(f"Version: {openapi_schema['info']['version']}")
    print("\nAuto-detected endpoints:")
    for path, methods in openapi_schema["paths"].items():
        for method in methods.keys():
            if method != "parameters":
                print(f"  {method.upper()} {path}")

    print("\n✓ FastAPI integrates OpenAPI natively!")
    print("  - Access spec at: http://localhost:8000/openapi.json")
    print("  - Interactive docs at: http://localhost:8000/docs")
    print("  - Alternative docs at: http://localhost:8000/redoc")


def main() -> None:
    """Main execution function."""
    print_section("OpenAPI (Swagger) Demonstration")

    # Line 319: Create OpenAPI specification
    print("Step 1: Creating OpenAPI 3.0 Specification")
    print("-" * 60)
    spec = create_openapi_spec()
    display_spec_summary(spec)

    # Line 325: Validate the specification
    print("\n" + "-" * 60)
    print("Step 2: Validating OpenAPI Specification")
    print("-" * 60)
    validate_openapi_spec(spec)

    # Line 331: Save in multiple formats
    print("\n" + "-" * 60)
    print("Step 3: Saving Specification (JSON & YAML)")
    print("-" * 60)
    save_spec_formats(spec)

    # Line 337: Demonstrate FastAPI integration
    demonstrate_fastapi_integration()

    # Line 340: Final summary
    print_section("Summary")
    print("OpenAPI (formerly Swagger) provides:")
    print("  ✓ Standardized API documentation format")
    print("  ✓ Language-agnostic API descriptions")
    print("  ✓ Auto-generated interactive documentation")
    print("  ✓ Code generation for clients and servers")
    print("  ✓ API validation and testing tools")
    print("\nModern frameworks like FastAPI generate OpenAPI specs automatically!")


if __name__ == "__main__":
    main()
