import logging

from app.application.dto.parsed_query import ParsedQuery
from app.domain.enums.metric_requested import MetricRequested
from app.domain.enums.seniority_level import SeniorityLevel

logger = logging.getLogger(__name__)


class QueryParser:

    def __init__(self):
        pass

    def parse(self, question: str) -> ParsedQuery:
        logger.info("Parsing incoming question")

        normalized_question = question.lower()
        seniority_level = None

        seniority_level = None
        if "junior" in normalized_question:
            seniority_level = SeniorityLevel.JUNIOR
        elif "mid" in normalized_question:
            seniority_level = SeniorityLevel.MID
        elif "senior" in normalized_question:
            seniority_level = SeniorityLevel.SENIOR
        elif "staff" in normalized_question:
            seniority_level = SeniorityLevel.STAFF
        elif "principal" in normalized_question:
            seniority_level = SeniorityLevel.PRINCIPAL

        role_title = None
        if "backend engineer" in normalized_question:
            role_title = "Backend Engineer"
        elif "data engineer" in normalized_question:
            role_title = "Data Engineer"
        elif "data scientist" in normalized_question:
            role_title = "Data Scientist"

        location = None
        if "london" in normalized_question:
            location = "London"
        elif "berlin" in normalized_question:
            location = "Berlin"
        elif "new york" in normalized_question:
            location = "New York"

        metric_requested = None
        if "range" in normalized_question:
            metric_requested = MetricRequested.RANGE
        elif "p25" in normalized_question:
            metric_requested = MetricRequested.P25
        elif "p50" in normalized_question:
            metric_requested = MetricRequested.P50
        elif "p75" in normalized_question:
            metric_requested = MetricRequested.P75
        elif "p90" in normalized_question:
            metric_requested = MetricRequested.P90

        return ParsedQuery(
            role_title=role_title,
            seniority_level=seniority_level,
            location=location,
            metric_requested=metric_requested
        )