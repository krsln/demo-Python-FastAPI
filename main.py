from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

# Define settings class for environment variables
class Settings(BaseSettings):
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    environment: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

# Load settings
settings = Settings()

# Initialize FastAPI app
app = FastAPI(
    title="Demo Python FastAPI",
    description="A simple FastAPI application with Swagger UI for API documentation",
    version="1.0.0"
)

# Define a Pydantic model for request/response data
class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

# In-memory storage for items (replace with a database in production)
items: List[Item] = []

# Root endpoint
@app.get("/")
async def root():
    return {"message": f"Welcome to the Demo Python FastAPI application! Running in {settings.environment} mode."}

# Create an item
@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    items.append(item)
    return item

# Read all items
@app.get("/items/", response_model=List[Item])
async def get_items():
    return items

# Read a specific item by ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

# Update an item by ID
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    return {"error": "Item not found"}

# Delete an item by ID
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            return {"message": f"Item {item_id} deleted"}
    return {"error": "Item not found"}