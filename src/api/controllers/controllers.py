from src.api.models.models import BasicResponse, ResponseStatus


async def get_root():
    return BasicResponse(message="Hello World", status=ResponseStatus.SUCCESS)
