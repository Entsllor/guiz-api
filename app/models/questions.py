from datetime import datetime

from sqlalchemy import Integer, Column, DateTime, VARCHAR, Text

from ..core.database import Base


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, index=True)
    answer = Column(Text)
    question = Column(VARCHAR(length=1023))
    loaded_at = Column(DateTime(timezone=False), index=True, default=datetime.now)
    created_at = Column(DateTime(timezone=False))
