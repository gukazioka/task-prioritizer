from src.repositories.abstract_repository import AbstractRepository
from src.models.task import Task

class MemoryRepository(AbstractRepository):
    
    def __init__(self):
        self._db: list[Task] = list()
    
    def add(self, task: Task):
        self._db.append(task)

    def get_all(self) -> list[Task]:
        return self._db
    
    def remove(self, description: str) -> bool:
        for task in self._db:
            if task.description == description:
                self._db.remove(task)
                return True