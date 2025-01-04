from library.domain.library import Library
from library.domain.book import Book

class LibraryService:
    """
    Сервис для работы с библиотекой.
    """
    def __init__(self, library: Library):
        self.library = library

    def add_book(self, book: Book):
        self.library.add(book)

    def search_books(self, query: str):
        return self.library.search(query)

    def get_books(self):
        return self.library.get_all()
