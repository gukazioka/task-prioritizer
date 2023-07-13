from fastapi import FastAPI
from src.models.task import Task
from contextlib import asynccontextmanager
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from pydantic import Field
from fastapi import Body
from src.services.task_service import TaskService, get_task_service

task_service: TaskService | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global task_service 
    task_service = get_task_service()
    yield
    del task_service


app = FastAPI(
    title='TasksPrioritizer',
    description='An API to prioritize tasks',
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/tasks')
def get_all_tasks() -> list[Task]:
    return task_service.get_all_tasks()


@app.post('/tasks')
def create_task(task: Task):
    task_service.create_task(task)


@app.delete('/tasks')
def delete_task(description: Annotated[str, Body(embed=True)]):
    if not task_service.delete_task(description):
        raise HTTPException(status_code=404, detail="Item not found")
