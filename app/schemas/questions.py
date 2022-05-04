from datetime import datetime

from pydantic import BaseModel


class QuestionsCreate(BaseModel):
    questions_num: int = 1


class QuestionOut(BaseModel):
    id: int
    answer: str
    question: str
    created_at: datetime
