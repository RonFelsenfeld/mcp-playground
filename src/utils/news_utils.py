from config import NEWS_API_KEY

from src.api.models.news_models import Article


def get_news_params(query: str, language: str = "en") -> dict:
    return {
        "apikey": NEWS_API_KEY,
        "q": query,
        "language": language,
    }


def normalize_news_data(articles_data: list[dict]) -> list[Article]:
    normalized_articles = [
        Article(
            title=item.get("title"),
            description=item.get("description"),
            url=item.get("link"),
        )
        for item in articles_data
    ]

    return normalized_articles
