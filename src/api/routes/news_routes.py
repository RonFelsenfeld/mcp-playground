from fastapi import APIRouter, Query

news_router = APIRouter()

from src.api.controllers.news_controller import get_latest_news


@news_router.get(path="/")
async def get_news(query: str, language: str = "en"):
    return await get_latest_news(query=query, language=language)
