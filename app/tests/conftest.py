import asyncio
import random
from asyncio import AbstractEventLoop

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, AsyncConnection, AsyncEngine

from app import services
from app.core.database import create_db_engine, Base
from app.core.settings import settings
from app.main import app
from app.schemas.questions import QuestionOut
from app.tests.api_questions_dump import dump
from app.utils.dependencies import get_db


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def db_engine() -> AsyncEngine:
    engine = create_db_engine(settings.TEST_DB_URL)
    yield engine
    engine.dispose()


@pytest.fixture(scope="function")
async def db_tables(db_engine) -> AsyncConnection:
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def db(db_tables, db_engine, event_loop: AbstractEventLoop) -> AsyncSession:
    session = AsyncSession(bind=db_engine)
    try:
        yield session
    finally:
        await session.rollback()
        await session.close()


@pytest.fixture(scope="function")
async def client(db, event_loop) -> AsyncClient:
    app.dependency_overrides[get_db] = lambda: db
    async with AsyncClient(app=app, base_url="http://test/") as test_client:
        yield test_client


async def get_questions_from_fake_api(count):
    return [QuestionOut(**question) for question in random.choices(dump, k=min(count, 100))]


@pytest.fixture
def fake_api(monkeypatch):
    monkeypatch.setattr(services.questions, 'fetch_questions', get_questions_from_fake_api)
