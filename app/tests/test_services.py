import pytest

from app import models
from app.schemas.questions import QuestionOut
from app.services.questions import fetch_questions, create_questions
from app.tests.api_questions_dump import dump


@pytest.mark.asyncio
async def test_fetch_questions():
    questions = await fetch_questions(3)
    assert len(questions) == 3
    assert all(isinstance(question, QuestionOut) for question in questions)


@pytest.mark.asyncio
async def test_create_questions(db):
    questions = await create_questions(db, 3)
    assert len(questions) == 3
    assert all(isinstance(question, models.Question) for question in questions)


@pytest.mark.asyncio
async def test_create_many_questions(db):
    questions = await create_questions(db, 129)
    assert len(questions) == 129
    assert all(isinstance(question, models.Question) for question in questions)


@pytest.mark.asyncio
async def test_create_zero_questions(db):
    questions = await create_questions(db, 0)
    assert len(questions) == 0
    assert questions == []


@pytest.mark.asyncio
async def test_get_all_question(fake_api, db):
    questions = await create_questions(db, 200)
    assert len(questions) == len(dump)
