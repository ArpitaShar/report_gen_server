from fastapi import APIRouter, HTTPException, Depends, Header
from fastapi.responses import FileResponse
from typing import Optional

from ..schemas.report import ReportRequest, ReportInfo
from ..services.report_service import build_report
from ..core.config import settings

router = APIRouter(prefix="/reports", tags=["reports"])


def api_key_auth(x_api_key: Optional[str] = Header(None)):
    if settings.API_KEY and x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return True


@router.post("", response_model=ReportInfo)
def create_report(req: ReportRequest, _=Depends(api_key_auth)):
    result = build_report(req.model_dump())
    return ReportInfo(
        report_id=result["report_id"],
        title=result["title"],
        pdf_path=result["pdf_path"],
    )


@router.get("/{report_id}/pdf")
def get_report_pdf(report_id: str, _=Depends(api_key_auth)):
    from pathlib import Path

    path = Path(settings.REPORTS_DIR) / f"report_{report_id}.pdf"
    if not path.exists():
        raise HTTPException(404, "Report not found")
    return FileResponse(str(path), media_type="application/pdf", filename=path.name)
