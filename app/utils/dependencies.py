from ..core.database import async_session


async def get_db():
    session = async_session()
    try:
        yield session
    finally:
        await session.close()
