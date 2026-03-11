import logging

from app.application.dto.query_result import QueryResult
from app.application.use_cases.query_parser import QueryParser

logger = logging.getLogger(__name__)    

class ProcessQueryUseCase:
    
    def __init__(self) -> None:
        self.query_parser = QueryParser()

    async def execute(self, question: str) -> QueryResult:
        logger.info("Processing query: %s", question)

        parsed_query = self.query_parser.parse(question)

        has_required_data = (
            parsed_query.role_title is not None and
            parsed_query.location is not None
        )

        if not has_required_data:
            logger.warning("Insufficient parsed data for benchmark query")
            return QueryResult(
                summary="Insufficient data to process benchmark query",
                insufficient_data=True,
                parsed_role_title=parsed_query.role_title,
                parsed_seniority_level=parsed_query.seniority_level,
                parsed_location=parsed_query.location,
                 parsed_metric_requested=parsed_query.metric_requested
            )
        
        logger.info("Parsed query contains required benchmark fields: %s", parsed_query)

        return QueryResult(
            summary="Parsed benchmark query successfully",
            insufficient_data=False,
            parsed_role_title=parsed_query.role_title,
            parsed_seniority_level=parsed_query.seniority_level,
            parsed_location=parsed_query.location,
              parsed_metric_requested=parsed_query.metric_requested
        )