from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

class ReportRequest(BaseModel):
    title: str = Field(default="API Data Report")
    description: Optional[str] = None
    # List of row dicts from your API/DB
    data: List[Dict[str, Any]] = Field(default_factory=list)
    # Optional hint for which columns are numeric
    numeric_fields: Optional[List[str]] = None

class ReportInfo(BaseModel):
    report_id: str
    title: str
    pdf_path: str
