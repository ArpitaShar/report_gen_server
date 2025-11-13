from typing import List, Dict, Any, Optional
from pathlib import Path
import pandas as pd
from ...core.config import settings

def retrieve_data(query: str, source_csv: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Simple demo retriever:
      - if source_csv is provided (path relative to DATA_DIR), load it
      - else, try data/input.csv
      - else, return empty list
    """
    csv_path = Path(settings.DATA_DIR) / (source_csv or "input.csv")
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        return df.to_dict(orient="records")
    return []
