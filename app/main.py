# from fastapi import FastAPI

# app = FastAPI(title="Report Generator API")

# @app.get("/api/health")
# def health():
#     return {"status": "healthy"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from app.core.config import settings
from .core.logging import setup_logging
from .routers import health
from .routers import reports
from .routers import health, agent_reports, reports

setup_logging()
app = FastAPI(title=settings.APP_NAME)

# CORS
origins = [o.strip() for o in settings.ALLOW_ORIGINS.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix=settings.API_PREFIX)

app.include_router(reports.router, prefix=settings.API_PREFIX)

app.include_router(agent_reports.router, prefix=settings.API_PREFIX)  # new graph pipeline

# Root
@app.get("/")
def root():
    return {"status": "ok", "name": settings.APP_NAME}
