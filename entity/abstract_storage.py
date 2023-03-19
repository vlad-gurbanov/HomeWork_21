from abc import ABC, abstractmethod
from typing import Dict


class AbstractStorage():
    """
    Абстрактный класс Storage
    """
    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> Dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
