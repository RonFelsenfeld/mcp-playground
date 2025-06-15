import httpx

from src.api.models.news_models import NewsResponse, ResponseStatus

from src.configs.logger_config import app_logger

from src.utils.news_utils import get_news_params, normalize_news_data


async def get_latest_news(query: str, language: str) -> NewsResponse:
    url = f"https://newsdata.io/api/1/latest"
    params = get_news_params(query=query, language=language)

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url, params=params)
            response.raise_for_status()
    except Exception as e:
        error_message = str(e)
        app_logger.error(error_message)
        return NewsResponse(data=[], status=ResponseStatus.ERROR)
    else:
        result = response.json()
        articles_data = result.get("results", [])
        normalized_articles = normalize_news_data(articles_data)
        return NewsResponse(data=normalized_articles, status=ResponseStatus.SUCCESS)
