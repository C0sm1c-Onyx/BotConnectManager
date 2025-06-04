from fastapi_service.dao import BaseDAO
from fastapi_service.auth.models import user


class UsersDAO(BaseDAO):
    model = user