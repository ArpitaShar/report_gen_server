from typing import List, Dict, Any, Optional
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def make_line_chart(rows: List[Dict[str, Any]], numeric_field: Optional[str] = None) -> bytes | None:
    if not rows:
        return None
    df = pd.DataFrame(rows)
    # pick the first numeric column if not specified
    num_cols = [c for c in df.columns if np.issubdtype(df[c].dtype, np.number)]
    if numeric_field and numeric_field in df.columns:
        col = numeric_field
    elif num_cols:
        col = num_cols[0]
    else:
        return None

    fig, ax = plt.subplots()
    ax.plot(df.index.to_list(), pd.to_numeric(df[col], errors="coerce").fillna(0).to_list())
    ax.set_title(f"{col} over rows")
    ax.set_xlabel("Row #")
    ax.set_ylabel(col)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf.read()
