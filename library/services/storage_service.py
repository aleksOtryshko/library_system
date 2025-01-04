from library.infrastructure.storage import Storage
from library.domain.library import Library

class StorageService:
    """
    Сервис для взаимодействия со хранилищем данных.
    """
    def __init__(self, storage: Storage, library: Library):
        self.storage = storage
        self.library = library

    def save_library(self):
        self.storage.save(self.library.get_all())

    def load_library(self):
        books = self.storage.load()
        for book in books:
            self.library.add(book)
