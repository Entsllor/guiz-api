import uvicorn
from fastapi import FastAPI

from app.api import questions

app = FastAPI()

app.include_router(questions.router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run('main:app')
