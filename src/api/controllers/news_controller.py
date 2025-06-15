import httpx
import json

from src.api.models.news_models import NewsResponse, ResponseStatus

from config import NEWS_API_KEY
from src.configs.logger_config import app_logger

from src.utils.news_utils import normalize_news_data


async def get_root() -> NewsResponse:
    query = "Israel-Iran-War"
    url = f"https://newsdata.io/api/1/latest"
    params = {"apikey": NEWS_API_KEY, "q": query, "language": "en"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url, params=params)
    except Exception as e:
        error_message = str(e)
        app_logger.error(error_message)
        return NewsResponse(data=[], status=ResponseStatus.ERROR)
    else:
        result = response.json()
        articles_data = result.get("results", [])
        normalized_articles = normalize_news_data(articles_data)
        return NewsResponse(data=normalized_articles, status=ResponseStatus.SUCCESS)
