from fastapi import APIRouter

router = APIRouter()

from src.api.controllers.controllers import get_root


@router.get("/")
async def root():
    return get_root()
