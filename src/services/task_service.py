from src.repositories.abstract_repository import AbstractRepository
from src.repositories.memory_repository import MemoryRepository
from src.fuzzy.task_prioritizer import TaskPrioritizer
from src.models.task import Task

class TaskService:

    def __init__(self, repository: AbstractRepository, prioritizer: TaskPrioritizer):
        self._repository = repository
        self._prioritizer = prioritizer

    def get_all_tasks(self) -> list[Task]:
        return self._repository.get_all()

    def create_task(self, task: Task):
        task.priority = self._prioritizer.set_priority(task.relevance, task.impact, task.complexity)
        self._repository.add(task)

    def delete_task(self, description: str):
        return self._repository.remove(description)


def get_task_service():
    return TaskService(MemoryRepository(), TaskPrioritizer())
