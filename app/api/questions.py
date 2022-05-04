from fastapi import APIRouter, Depends
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from .. import services
from ..schemas.questions import QuestionsCreate, QuestionOut
from ..utils.dependencies import get_db

router = APIRouter()
client = AsyncClient()


@router.post('/questions/', response_model=list[QuestionOut])
async def create_question(questions_create: QuestionsCreate, db: AsyncSession = Depends(get_db)):
    db_questions = await services.questions.create_questions(db, questions_create.questions_num)
    await db.commit()
    return db_questions
