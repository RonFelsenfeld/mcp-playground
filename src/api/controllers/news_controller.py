from httpx import AsyncClient, HTTPStatusError

from src.api.models.news_models import NewsResponse, ResponseStatus

from src.configs.logger_config import app_logger

from src.utils.news_utils import get_news_params, normalize_news_data


async def get_latest_news(query: str, language: str) -> NewsResponse:
    url = f"https://newsdata.io/api/1/latest"
    params = get_news_params(query=query, language=language)

    try:
        async with AsyncClient() as client:
            response = await client.get(url=url, params=params)
            response.raise_for_status()
    except HTTPStatusError as e:
        app_logger.error(f"[HTTPError]: Fetching news failed - {str(e)}")
        return NewsResponse(data=[], status=ResponseStatus.ERROR)
    except Exception as e:
        app_logger.error(f"[Error]: Fetching news failed - {str(e)}")
        return NewsResponse(data=[], status=ResponseStatus.ERROR)
    else:
        result = response.json()
        articles_data = result.get("results", [])
        normalized_articles = normalize_news_data(articles_data)
        return NewsResponse(data=normalized_articles, status=ResponseStatus.SUCCESS)
