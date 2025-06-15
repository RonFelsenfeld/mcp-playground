from fastapi import FastAPI

from src.api.routes.routes import router

API_PREFIX = "/api"

app = FastAPI()

app.include_router(prefix=API_PREFIX, router=router)
