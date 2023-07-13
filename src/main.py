from fastapi import FastAPI
from src.models.task import Task
import random
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from pydantic import Field
from fastapi import Body

app = FastAPI(
    title='TasksAPI',
    description='An API to perform database operations related to tasks'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


CLASSIFICATION = [
    'lowest',
    'low',
    'medium',
    'high',
    'highest'
]

fake_db: dict[str, Task] = dict()

@app.get('/tasks')
def get_all_tasks() -> list[Task]:
    return list(fake_db.values())


@app.post('/tasks')
def create_task(task: Task):
    task.priority = random.choice(CLASSIFICATION)
    fake_db[task.description] = task


@app.delete('/tasks')
def delete_task(description: Annotated[str, Body(embed=True)]):
    try:
        fake_db.pop(description)
    except:
        raise HTTPException(status_code=404, detail="Item not found")
