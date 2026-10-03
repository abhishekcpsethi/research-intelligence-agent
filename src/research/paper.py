from dataclasses import dataclass
from datetime import datetime


@dataclass
class Paper:
    title: str
    authors: list[str]
    summary: str
    published: datetime
    pdf_url: str|None