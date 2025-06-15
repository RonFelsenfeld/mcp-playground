from fastapi import FastAPI
from src.api.routes.news_routes import news_router

API_PREFIX = "/api"

app = FastAPI()

app.include_router(prefix=API_PREFIX, router=news_router)
