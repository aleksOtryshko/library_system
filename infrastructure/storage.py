from domain.library import Library
from domain.book import Book


class Storage:
    """
    Handles data persistence for the library.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path  # Path to the storage file

    def save(self, library: Library):
        """
        Saves the library data to a file.
        :param library: Library instance to save.
        """
        try:
            with open(self.file_path, 'w') as file:
                data = [{'title': book.title, 'author': book.author} for book in library.books]
                file.write(str(data))
        except Exception as e:
            print(f"Error saving data: {e}")

    def load(self, library: Library):
        """
        Loads the library data from a file.
        :param library: Library instance to populate.
        """
        try:
            with open(self.file_path, 'r') as file:
                data = eval(file.read())
                for book_data in data:
                    library.add(Book(book_data['title'], book_data['author']))
        except FileNotFoundError:
            print("No data file found. Starting with an empty library.")
        except Exception as e:
            print(f"Error loading data: {e}")

