from typing import TypedDict, List, Dict, Any, Optional
from dataclasses import dataclass

class AgentState(TypedDict, total=False):
    query: str                          # user request
    context: Optional[str]              # extra instructions
    params: Dict[str, Any]              # flags like {use_web: True}
    data_rows: List[Dict[str, Any]]     # retrieved tabular rows
    data_summary: Dict[str, Any]        # numeric stats, columns, etc.
    analysis_text: str                  # LLM analysis narrative
    web_results: List[Dict[str, Any]]   # {title, link, snippet}
    viz_images: List[bytes]             # PNG bytes
    report_id: str
    report_path: str
    messages: List[str]                 # trace log for debugging
