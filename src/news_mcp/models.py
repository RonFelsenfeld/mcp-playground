from pydantic import BaseModel


class Article(BaseModel):
    """
    A news article.

    Args:
        title (str): The title of the article.
        description (str): The description of the article.
        url (str): The URL of the article.
    """

    title: str | None = None
    description: str | None = None
    url: str | None = None
