from fastapi import APIRouter

news_router = APIRouter()

from src.api.controllers.news_controller import get_root


@news_router.get(path="/")
async def root():
    return await get_root()
