import logging

from fastapi import APIRouter

from app.api.schemas.query import QueryRequest, QueryResponse
from app.application.use_cases.process_query import ProcessQueryUseCase

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/query", response_model=QueryResponse)
def query_benchmark(payload: QueryRequest) -> QueryResponse:
    logger.info("Benchmark query received: %s", payload.question)

    use_case = ProcessQueryUseCase()
    result = use_case.execute(payload.question)

    return QueryResponse(
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        parsed_role_title=result.parsed_role_title,
        parsed_seniority_level=result.parsed_seniority_level,
        parsed_location=result.parsed_location,
        parsed_metric_requested=result.parsed_metric_requested,
        currency=result.currency,
        p25_base_salary=result.p25_base_salary,
        p50_base_salary=result.p50_base_salary,
        p75_base_salary=result.p75_base_salary,
        p90_base_salary=result.p90_base_salary,
        data_points=result.data_points,
    )