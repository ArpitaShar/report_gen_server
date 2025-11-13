from typing import List, Dict
from duckduckgo_search import DDGS
from ...core.config import settings

def web_search(query: str, max_results: int | None = None) -> List[Dict]:
    limit = max_results or settings.SEARCH_MAX_RESULTS
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=limit):
            results.append({
                "title": r.get("title"),
                "link": r.get("href"),
                "snippet": r.get("body"),
            })
    return results
