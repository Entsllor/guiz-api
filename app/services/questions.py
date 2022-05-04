from httpx import AsyncClient
from sqlalchemy import select

from .. import models
from ..schemas.questions import QuestionOut

client = AsyncClient()


async def get_not_existence_questions_ids(db, ids: set[int]):
    existence_ids = (await db.execute(select(models.Question.id).where(models.Question.id.in_(ids)))).all()
    return ids - set(existence_ids)


async def fetch_questions(count) -> list[QuestionOut]:
    response = await client.get(f"https://jservice.io/api/random?count={count}")
    return [QuestionOut(**question) for question in response.json()]


async def create_questions(db, count):
    new_questions = []
    new_ids = set()
    response_count = 0
    while len(new_ids) != count:
        fetched_questions = await fetch_questions(count)
        response_count += 1
        question_ids = {question.id for question in fetched_questions}
        new_ids |= await get_not_existence_questions_ids(db, question_ids)
        new_questions.extend([question for question in fetched_questions if question.id in new_ids])
        if response_count > 9:
            break

    db_questions = [models.Question(**question.dict()) for question in new_questions[:count]]
    db.add_all(db_questions)
    return db_questions
