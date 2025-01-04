from library.domain.book import Book

class Library:
    """
    Класс, управляющий коллекцией книг.
    """
    def __init__(self):
        self.books = []

    def add(self, book: Book):
        self.books.append(book)

    def search(self, query: str):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

    def get_all(self):
        return self.books
