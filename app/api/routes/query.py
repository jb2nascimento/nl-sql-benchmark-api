import logging
from unittest import result

from fastapi import APIRouter

from app.api.schemas.query import QueryRequest, QueryResponse
from app.application.use_cases.process_query import ProcessQueryUseCase

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/query", response_model=QueryResponse)
async def query_benchmark(payload: QueryRequest) -> QueryResponse:

    logger.info("Benchmark query received: %s", payload.question)

    usecase = ProcessQueryUseCase()
    result = await usecase.execute(payload.question)

    return QueryResponse(
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        parsed_role_title=result.parsed_role_title,
        parsed_seniority_level=result.parsed_seniority_level,
        parsed_location=result.parsed_location,
    )
