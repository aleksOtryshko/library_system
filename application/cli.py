from domain.library import Library
from domain.book import Book
from infrastructure.storage import Storage


class CLI:
    """
    Command-line interface for interacting with the library.
    """

    def __init__(self, library: Library, storage: Storage):
        self.library = library
        self.storage = storage

    def run(self):
        """
        Runs the CLI application.
        """
        try:
            self.storage.load(self.library)  # Load existing library data
            print("Library data loaded successfully.")
        except Exception as e:
            print(f"Error loading library data: {e}")

        menu_options = {
            '1': self.add_book,
            '2': self.search_books,
            '3': self.list_books,
            '4': self.exit_program,
        }

        while True:
            try:
                self.show_menu()
                choice = input("Enter your choice: ").strip()
                if choice not in menu_options:
                    print("Invalid choice. Please try again.")
                    continue

                # Call the selected action
                menu_options[choice]()
            except Exception as e:
                print(f"An error occurred: {e}")

    @staticmethod
    def show_menu():
        """
        Displays the main menu.
        """
        print("\nLibrary System")
        print("1. Add a book")
        print("2. Search for a book")
        print("3. List all books")
        print("4. Exit")

    def add_book(self):
        """
        Handles adding a new book to the library.
        """
        try:
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()

            if not title or not author:
                raise ValueError("Title and author cannot be empty.")

            self.library.add(Book(title, author))
            print(f"Book '{title}' by {author} added successfully.")
        except ValueError as e:
            print(f"Validation error: {e}")
        except Exception as e:
            print(f"Error adding book: {e}")

    def search_books(self):
        """
        Handles searching for books in the library.
        """
        try:
            query = input("Enter a search term (title or author): ").strip()

            if not query:
                raise ValueError("Search term cannot be empty.")

            results = self.library.search(query)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"- {book.title} by {book.author}")
            else:
                print("No books found.")
        except ValueError as e:
            print(f"Validation error: {e}")
        except Exception as e:
            print(f"Error searching books: {e}")

    def list_books(self):
        """
        Displays all books in the library.
        """
        try:
            if self.library.books:
                print("\nBooks in the Library:")
                for book in self.library.books:
                    print(f"- {book.title} by {book.author}")
            else:
                print("The library is empty.")
        except Exception as e:
            print(f"Error listing books: {e}")

    def exit_program(self):
        """
        Saves the library data and exits the program.
        """
        try:
            self.storage.save(self.library)
            print("Library data saved. Goodbye!")
            exit(0)
        except Exception as e:
            print(f"Error saving library data: {e}")

