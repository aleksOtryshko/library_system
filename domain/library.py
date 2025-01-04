from domain.book import Book


class Library:
    """
    Represents a library entity containing a collection of books.
    """

    def __init__(self):
        self.books = []  # List to store Book objects

    def add(self, book: Book):
        """
        Adds a book to the library.
        :param book: Instance of Book to add to the library.
        """
        self.books.append(book)

    def search(self, query: str):
        """
        Searches for books by title or author.
        :param query: Search query string.
        :return: List of books that match the query.
        """
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

