from fastapi import APIRouter

router = APIRouter()

from src.api.controllers.controllers import get_root


@router.get(path="/")
async def root():
    return await get_root()
