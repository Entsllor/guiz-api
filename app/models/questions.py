from datetime import datetime

from sqlalchemy import Integer, Column, DateTime, VARCHAR, Text

from ..core.database import Base


class Question(Base):
    __table_name__ = 'question'
    id = Column(Integer, primary_key=True, index=True)
    answer = Column(Text)
    question = Column(VARCHAR(length=1023))
    created_at = Column(DateTime, index=True, default=datetime.now)
