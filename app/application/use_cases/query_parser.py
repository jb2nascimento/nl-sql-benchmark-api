import logging

from app.application.dto.parsed_query import ParsedQuery

logger = logging.getLogger(__name__)


class QueryParser:

    def __init__(self):
        pass

    def parse(self, question: str) -> ParsedQuery:
        logger.info("Parsing incoming question")

        normalized_question = question.lower()
        seniority_level = None

        if "junior" in normalized_question:
            seniority_level = "Junior"
        elif "mid" in normalized_question:
            seniority_level = "Mid"
        elif "senior" in normalized_question:
            seniority_level = "Senior"
        elif "staff" in normalized_question:
            seniority_level = "Staff"
        elif "principal" in normalized_question:
            seniority_level = "Principal"

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

        return ParsedQuery(
            role_title=role_title,
            seniority_level=seniority_level,
            location=location,
        )