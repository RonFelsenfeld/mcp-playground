from src.api.models.news_models import Article


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
