from base_storage import BaseStorage
from exceptions import TooManyDifferentProducts

class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_uniq_items_count() > 5:
            raise TooManyDifferentProducts
        super().add(name, amount)

