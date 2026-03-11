import logging

from fastapi import APIRouter

from app.api.schemas.health import HealthResponse
from app.core.settings import settings

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    logger.info("Healthcheck requested")
    return  HealthResponse(
            status="ok",
            environment=settings.app_env,
            debug=settings.app_debug
    )