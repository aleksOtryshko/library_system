class Book:
    """
    Represents a book entity with a title and an author.
    """

    def __init__(self, title: str, author: str):
        if not title or not author:
            raise ValueError("Book title and author must not be empty.")
        self.title = title  # Title of the book
        self.author = author  # Author of the book

