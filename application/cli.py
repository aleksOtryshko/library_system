from application.menu import Menu
from library.services.library_service import LibraryService
from library.services.storage_service import StorageService
from library.domain.book import Book
import re

class CLI:
    """
    Интерфейс командной строки для управления библиотекой.
    """
    def __init__(self, library_service: LibraryService, storage_service: StorageService):
        self.library_service = library_service
        self.storage_service = storage_service
        self.menu = Menu()

    def run(self):
        self.storage_service.load_library()
        self.setup_menu()
        while True:
            print("\nLibrary System:")
            self.menu.show()
            choice = input("\nSelect an option: ")
            if choice == "4":  # Обработка выбора выхода
                self.storage_service.save_library()
                print("Goodbye!")
                break  # Прерывание цикла и завершение программы
            self.menu.execute(choice)

    def setup_menu(self):
        self.menu.add_option("1", "Add Book", self.add_book)
        self.menu.add_option("2", "Search Books", self.search_books)
        self.menu.add_option("3", "List Books", self.list_books)

    def add_book(self):
        title = self.get_valid_input("Enter book title: ")
        author = self.get_valid_input("Enter book author: ")
        self.library_service.add_book(Book(title, author))
        print(f"Added '{title}' by {author}")

    def search_books(self):
        query = input("Search term: ")
        results = self.library_service.search_books(query)
        for book in results:
            print(f"- {book.title} by {book.author}")

    def list_books(self):
        books = self.library_service.get_books()
        if not books:
            print("Library is empty.")
        for book in books:
            print(f"- {book.title} by {book.author}")

    def get_valid_input(self, prompt: str):
        while True:
            user_input = input(prompt)
            if re.match("^[A-Za-z0-9 ]+$", user_input):  # Проверка на спецсимволы
                return user_input
            else:
                print("Invalid input. Only letters, numbers, and spaces are allowed.")
