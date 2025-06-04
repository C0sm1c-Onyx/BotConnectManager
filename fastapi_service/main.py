from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.managers import get_user_manager
from auth.schemas import UserRead, UserCreate
from auth.auth import auth_backend

from fastapi_service.database import AuthUser

from fastapi_service.bot_handling.routers import router


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FastAPI application!"}


fastapi_users = FastAPIUsers[AuthUser, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    router,
    prefix='/bot',
)