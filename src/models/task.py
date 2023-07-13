from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    description: str
    priority: Optional[str] = Field(None)
    impact: str
    relevance: str
    complexity: str