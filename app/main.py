from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(api_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db")
def health_check():
    # postgresql://postgres:postgres@localhost:5432/fastapi_db
    return {"DATABASE_URL": settings.DATABASE_URL}
