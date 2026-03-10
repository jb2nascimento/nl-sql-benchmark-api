from fastapi import APIRouter
from app.core.settings import settings

router = APIRouter()

@router.get("/health")
def health() -> dict[str, str]:
    return {
            "status": "ok",
            "enviroment": settings.app_env,
            "debug": str(settings.app_debug)
           }