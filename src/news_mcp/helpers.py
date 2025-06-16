from config import NEWS_API_KEY

from src.news_mcp.models import Article


def get_news_params(query: str, language: str = "en") -> dict:
    """
    Get the parameters for the news API.

    Args:
        query (str): The query to search for.
        language (str): The language of the news.

    Returns:
        dict: A dictionary of parameters for the news API.
    """

    return {
        "apikey": NEWS_API_KEY,
        "q": query,
        "language": language,
    }


def normalize_news_data(articles_data: list[dict]) -> list[Article]:
    """
    Normalize the news data.

    Args:
        articles_data (list[dict]): The data to normalize.

    Returns:
        list[Article]: A list of normalized articles.
    """

    normalized_articles = [
        Article(
            title=item.get("title"),
            description=item.get("description"),
            url=item.get("link"),
        )
        for item in articles_data
    ]

    return normalized_articles
