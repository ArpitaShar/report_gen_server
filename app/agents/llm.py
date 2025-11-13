from typing import Any
from langchain_ollama import ChatOllama
from ..core.config import settings

def get_llm() -> Any:
    # Local-first LLM via Ollama
    return ChatOllama(
        base_url=settings.OLLAMA_BASE_URL,
        model=settings.LLM_MODEL,
        temperature=settings.TEMPERATURE,
        num_ctx=4096, # will change this later to high
    )
