import json
from library.domain.book import Book

class Storage:
    """
    Класс для сохранения и загрузки данных из файла.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, books: list):
        data = [{"title": book.title, "author": book.author} for book in books]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [Book(**item) for item in data]
        except FileNotFoundError:
            return []
