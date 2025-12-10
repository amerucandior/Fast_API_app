# app/core/exceptions.py
class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id
