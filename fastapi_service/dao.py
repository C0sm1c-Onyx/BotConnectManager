from sqlalchemy.future import select

from fastapi_service.database import async_session


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()