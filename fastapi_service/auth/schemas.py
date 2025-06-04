from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    is_active: bool = True
    is_verified: bool = False
    is_superuser: bool = False