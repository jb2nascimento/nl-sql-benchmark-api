from dataclasses import dataclass

@dataclass
class ParsedQuery:
    role_title: str | None
    seniority_level: str | None
    location: str | None
