from fastapi import APIRouter, Depends
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.schemas.questions import QuestionsCreate, QuestionOut
from app.utils.dependencies import get_db

router = APIRouter()
client = AsyncClient()


@router.post('/', response_model=list[QuestionOut])
async def create_question(questions_create: QuestionsCreate, db: AsyncSession = Depends(get_db)):
    response = await client.get(f"https://jservice.io/api/random?count={questions_create.questions_num}")
    questions = [QuestionOut(**question) for question in response.json()]
    db_questions = [models.Question(**question.dict()) for question in questions]
    db.add_all(db_questions)
    await db.commit()
    return response.json()
