from httpx import AsyncClient

from src.configs.logger_config import app_logger

from src.news_mcp.models import Article
from src.news_mcp.helpers import get_news_params, normalize_news_data
from src.news_mcp.constants import API_BASE


async def get_latest_news(query: str, language: str = "en") -> list[Article]:
    """
    Get the latest news for a given query and language.

    Args:
        query (str): The query to search for.
        language (str): The language of the news.

    Returns:
        list[Article]: A list of normalized articles.
    """

    app_logger.info(f"MCP SERVER: Getting latest news for {query} in {language}")

    params = get_news_params(query=query, language=language)

    try:
        async with AsyncClient() as client:
            response = await client.get(url=API_BASE, params=params)
            response.raise_for_status()

            result = response.json()
            articles_data = result.get("results", [])

            normalized_articles = normalize_news_data(articles_data)
            app_logger.info(f"MCP SERVER: Found {len(normalized_articles)} articles")

            return normalized_articles
    except Exception as e:
        app_logger.error(f"Error making request to {API_BASE}: {str(e)}")
        return []
