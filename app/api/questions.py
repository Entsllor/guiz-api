from fastapi import APIRouter
from httpx import AsyncClient

from app.schemas.questions import QuestionsCreate, QuestionOut

router = APIRouter()
client = AsyncClient()


@router.post('/', response_model=list[QuestionOut])
async def create_question(questions_create: QuestionsCreate):
    response = await client.get(f"https://jservice.io/api/random?count={questions_create.questions_num}")
    return response.json()
