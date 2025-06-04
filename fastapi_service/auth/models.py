from sqlalchemy import Table, Column, String, Integer, Boolean

from fastapi_service.database import metadata


user = Table(
    "user",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, default=True, nullable=True),
    Column('is_superuser', Boolean, default=False, nullable=True),
    Column('is_verified', Boolean, default=False, nullable=True)
)
