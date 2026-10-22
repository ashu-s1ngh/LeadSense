from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class LeadCreate(BaseModel):
    title: str
    url: HttpUrl
    source: str
    tech_stack: list[str] = []

class LeadResponse(LeadCreate):
    id: int
    comfort_score: int
    created_at: datetime

    class Config:
        from_attribute = True