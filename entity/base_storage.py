from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.exeptions import NotEnoughSpaceError, NotEnoughProductError, UnknownProductError


class BaseStorage(AbstractStorage):
    """
    Base класс Storage
    """
    def __init__(self, items: Dict[str, int], capacity: int):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        """
            Добавление товара
        """
        if self.get_free_space() < amount:
            raise NotEnoughSpaceError

        self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:
        """
            Удаление товара
        """

        if name not in self._items:
            raise UnknownProductError

        if self._items[name] < amount:
            raise NotEnoughProductError

        self._items[name] -= amount
        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self) -> int:
        """
            Получение свободного места
        """
        return self._capacity - sum(self._items.values())

    def get_items(self) -> Dict[str, int]:
        """
            Получение всех товаров и количества.
        """
        return self._items

    def get_unique_items_count(self) -> int:
        """
            Проверка количества уникальных товаров.
        """
        return len(self._items)
