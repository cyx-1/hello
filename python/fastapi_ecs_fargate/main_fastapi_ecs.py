#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi>=0.115.0",
#     "uvicorn[standard]>=0.32.0",
# ]
# ///

"""
FastAPI service demonstrating deployment to AWS ECS with Fargate.

This application showcases a production-ready FastAPI service that can be
deployed to AWS ECS using Fargate (serverless containers) via CloudFormation.
"""

from datetime import datetime
from typing import Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Line 21: Initialize FastAPI application with metadata
app = FastAPI(
    title="FastAPI ECS Demo",
    description="Demo API for AWS ECS/Fargate deployment",
    version="1.0.0",
)


# Line 29: Define data models using Pydantic
class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    timestamp: str
    service: str


class Item(BaseModel):
    """Sample item model."""

    id: int
    name: str
    description: str | None = None
    price: float


class ItemCreate(BaseModel):
    """Model for creating new items."""

    name: str
    description: str | None = None
    price: float


# Line 54: In-memory storage for demo purposes
items_db: Dict[int, Item] = {
    1: Item(id=1, name="Widget", description="A useful widget", price=19.99),
    2: Item(id=2, name="Gadget", description="An amazing gadget", price=29.99),
}
next_id = 3


# Line 62: Health check endpoint for ECS health checks
@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Health check endpoint used by AWS ECS/ALB target group health checks.

    This endpoint should return 200 OK when the service is healthy.
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow().isoformat(),
        service="fastapi-ecs-demo",
    )


# Line 77: Root endpoint
@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint returning welcome message."""
    return {
        "message": "FastAPI ECS/Fargate Demo API",
        "documentation": "/docs",
        "health": "/health",
    }


# Line 87: List all items
@app.get("/items", response_model=List[Item])
async def list_items() -> List[Item]:
    """Retrieve all items from the database."""
    return list(items_db.values())


# Line 93: Get single item by ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    """Retrieve a specific item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


# Line 102: Create new item
@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: ItemCreate) -> Item:
    """Create a new item."""
    global next_id
    new_item = Item(
        id=next_id,
        name=item.name,
        description=item.description,
        price=item.price,
    )
    items_db[next_id] = new_item
    next_id += 1
    return new_item


# Line 118: Update item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemCreate) -> Item:
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item = Item(
        id=item_id,
        name=item.name,
        description=item.description,
        price=item.price,
    )
    items_db[item_id] = updated_item
    return updated_item


# Line 136: Delete item
@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int) -> None:
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]


# Line 145: Application entry point
if __name__ == "__main__":
    import uvicorn

    # Line 148: Run the application with uvicorn
    # In production (ECS), uvicorn is started via Dockerfile CMD
    uvicorn.run(
        app,
        host="0.0.0.0",  # Listen on all interfaces for container networking
        port=8000,  # Standard port, mapped in ECS task definition
        log_level="info",
    )
