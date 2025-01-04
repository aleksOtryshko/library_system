from domain.library import Library
from infrastructure.storage import Storage
from application.cli import CLI

if __name__ == "__main__":
    storage = Storage("library_data.txt")
    library = Library()
    cli = CLI(library, storage)
    cli.run()

