from datetime import datetime

from pydantic import BaseModel, validator
from pydantic.datetime_parse import parse_datetime


class QuestionsCreate(BaseModel):
    questions_num: int = 1


class QuestionOut(BaseModel):
    id: int
    answer: str
    question: str
    created_at: datetime

    @validator('created_at', pre=True)
    def created_at_validator(cls, date_time: datetime):
        date_time = parse_datetime(date_time)
        date_time = date_time.replace(tzinfo=None)
        return date_time
