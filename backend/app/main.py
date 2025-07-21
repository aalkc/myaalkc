"""
Main FastAPI application for Amanat Al-Kalima Company ERP
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title="Amanat Al-Kalima Company ERP",
    description="Comprehensive ERP system for metal scrap business operations",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Amanat Al-Kalima Company ERP System",
        "docs": "/docs",
        "api_version": "v1"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "aalkc-erp-backend"}