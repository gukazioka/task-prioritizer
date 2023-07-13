from abc import ABC, abstractmethod
from typing import T

class AbstractRepository(ABC):
    @abstractmethod
    def add(self, object: T): ...

    @abstractmethod
    def get_all(self) -> list[T]: ...

    @abstractmethod
    def remove(self, object: T) -> bool: ...
