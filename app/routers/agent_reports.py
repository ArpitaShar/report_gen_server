from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from ..core.config import settings
from ..agents.graph import build_graph

router = APIRouter(prefix="/agent_reports", tags=["agent_reports"])

def api_key_auth(x_api_key: Optional[str] = Header(None)):
    if settings.API_KEY and x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return True

class AgentReportRequest(BaseModel):
    query: str = Field(..., description="User's request/question for the report")
    context: Optional[str] = None
    params: Dict[str, Any] = Field(default_factory=dict)
    # params examples:
    # { "source_csv": "input.csv", "numeric_fields": ["revenue", "orders"], "use_web": true, "viz_numeric_field": "revenue", "title": "Sales Report" }

class AgentReportResponse(BaseModel):
    report_id: str
    report_path: str
    analysis_text: Optional[str] = None
    data_summary: Optional[Dict[str, Any]] = None
    web_results: Optional[list] = None
    messages: Optional[list] = None

@router.post("", response_model=AgentReportResponse)
def create_agent_report(req: AgentReportRequest, _=Depends(api_key_auth)):
    graph = build_graph()
    initial_state = {
        "query": req.query,
        "context": req.context,
        "params": req.params or {},
        "messages": [],
    }
    final_state = graph.invoke(initial_state)

    return AgentReportResponse(
        report_id=final_state.get("report_id"),
        report_path=final_state.get("report_path"),
        analysis_text=final_state.get("analysis_text"),
        data_summary=final_state.get("data_summary"),
        web_results=final_state.get("web_results"),
        messages=final_state.get("messages"),
    )
