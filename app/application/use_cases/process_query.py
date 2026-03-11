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

        return QueryResult(
            summary="Parsed benchmark query successfully",
            insufficient_data=False,
            parsed_role_title=parsed_query.role_title,
            parsed_seniority_level=parsed_query.seniority_level,
            parsed_location=parsed_query.location,
        )