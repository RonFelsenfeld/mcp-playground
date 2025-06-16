from httpx import AsyncClient, HTTPStatusError

from configs.logger_config import app_logger

from src.news_mcp.models import Article
from src.news_mcp.helpers import get_news_params, normalize_news_data


async def get_latest_news(query: str, language: str = "en") -> list[Article]:
    """
    Get the latest news for a given query and language.

    Args:
        query (str): The query to search for.
        language (str): The language of the news.

    Returns:
        list[Article]: A list of normalized articles.
    """

    url = f"https://newsdata.io/api/1/latest"
    params = get_news_params(query=query, language=language)

    try:
        async with AsyncClient() as client:
            response = await client.get(url=url, params=params)
            response.raise_for_status()
    except HTTPStatusError as e:
        app_logger.error(f"[HTTPError]: Fetching news failed - {str(e)}")
        return []
    except Exception as e:
        app_logger.error(f"[Error]: Fetching news failed - {str(e)}")
        return []
    else:
        result = response.json()
        articles_data = result.get("results", [])
        normalized_articles = normalize_news_data(articles_data)
        return normalized_articles
