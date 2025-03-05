from requests import post
from config import AUTH_API


async def register_user(**kwargs):
    response = post(AUTH_API, data=kwargs)
    return response.status_code

