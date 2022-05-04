from fastapi import APIRouter, Depends
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.schemas.questions import QuestionsCreate, QuestionOut
from app.utils.dependencies import get_db

router = APIRouter()
client = AsyncClient()


async def get_not_existence_questions_ids(db, ids: set[int]):
    existence_ids = (await db.execute(select(models.Question.id).where(models.Question.id.in_(ids)))).all()
    return ids - set(existence_ids)


@router.post('/', response_model=list[QuestionOut])
async def create_question(questions_create: QuestionsCreate, db: AsyncSession = Depends(get_db)):
    new_questions = []
    new_ids = set()
    while len(new_ids) != questions_create.questions_num:
        response = await client.get(f"https://jservice.io/api/random?count={questions_create.questions_num}")
        body = response.json()
        question_ids = {question['id'] for question in body}
        new_ids |= await get_not_existence_questions_ids(db, question_ids)
        new_questions.extend([QuestionOut(**question) for question in body if question['id'] in new_ids])

    db_questions = [models.Question(**question.dict()) for question in new_questions]
    db.add_all(db_questions)
    await db.commit()
    return new_questions
