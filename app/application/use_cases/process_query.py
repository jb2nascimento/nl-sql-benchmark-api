import logging

from app.application.dto.query_result import QueryResult
from app.application.use_cases.query_parser import QueryParser
from app.infrastructure.external.in_memory_benchmark_repository import (
    InMemoryBenchmarkRepository,
)

logger = logging.getLogger(__name__)


class ProcessQueryUseCase:
    def __init__(self) -> None:
        self.query_parser = QueryParser()
        self.benchmark_repository = InMemoryBenchmarkRepository()

    def execute(self, question: str) -> QueryResult:
        logger.info("Processing benchmark query")

        parsed_query = self.query_parser.parse(question)

        has_required_data = parsed_query.role_title is not None and parsed_query.location is not None

        if not has_required_data:
            logger.warning("Insufficient parsed data for benchmark query")

            return QueryResult(
                summary="Insufficient data to process benchmark query",
                insufficient_data=True,
                parsed_role_title=parsed_query.role_title,
                parsed_seniority_level=(parsed_query.seniority_level.value if parsed_query.seniority_level is not None else None),
                parsed_location=parsed_query.location,
                parsed_metric_requested=(parsed_query.metric_requested.value if parsed_query.metric_requested is not None else None),
                currency=None,
                p25_base_salary=None,
                p50_base_salary=None,
                p75_base_salary=None,
                p90_base_salary=None,
                data_points=None,
                notes=["Missing required query dimensions: role title and/or location"],
            )

        benchmark = self.benchmark_repository.find_benchmark(
            role_title=parsed_query.role_title,
            location=parsed_query.location,
            seniority_level=parsed_query.seniority_level,
        )

        if benchmark is None:
            logger.warning("No benchmark record found for parsed query")

            return QueryResult(
                summary="No benchmark data found for the requested query",
                insufficient_data=True,
                parsed_role_title=parsed_query.role_title,
                parsed_seniority_level=(parsed_query.seniority_level.value if parsed_query.seniority_level is not None else None),
                parsed_location=parsed_query.location,
                parsed_metric_requested=(parsed_query.metric_requested.value if parsed_query.metric_requested is not None else None),
                currency=None,
                p25_base_salary=None,
                p50_base_salary=None,
                p75_base_salary=None,
                p90_base_salary=None,
                data_points=None,
                notes=["No benchmark record matched the parsed query"],
            )

        logger.info("Benchmark record found successfully")

        metric = parsed_query.metric_requested
        if metric is None or metric.value == "range":
            summary = f"Compensation range benchmark for " f"{benchmark.seniority_level.value} {benchmark.role_title} " f"in {benchmark.location}"
        else:
            summary = f"{metric.value.upper()} compensation benchmark for " f"{benchmark.seniority_level.value} {benchmark.role_title} " f"in {benchmark.location}"

        return QueryResult(
            summary=summary,
            insufficient_data=False,
            parsed_role_title=parsed_query.role_title,
            parsed_seniority_level=(parsed_query.seniority_level.value if parsed_query.seniority_level is not None else None),
            parsed_location=parsed_query.location,
            parsed_metric_requested=(parsed_query.metric_requested.value if parsed_query.metric_requested is not None else None),
            currency=benchmark.currency,
            p25_base_salary=benchmark.p25_base_salary,
            p50_base_salary=benchmark.p50_base_salary,
            p75_base_salary=benchmark.p75_base_salary,
            p90_base_salary=benchmark.p90_base_salary,
            data_points=benchmark.data_points,
            notes=[f"Based on {benchmark.data_points} data points"],
        )
