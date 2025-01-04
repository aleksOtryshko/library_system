from application.cli import CLI
from library.domain.library import Library
from library.infrastructure.storage import Storage
from library.services.library_service import LibraryService
from library.services.storage_service import StorageService

def main():
    library = Library()
    storage = Storage("library.json")
    library_service = LibraryService(library)
    storage_service = StorageService(storage, library)
    cli = CLI(library_service, storage_service)
    cli.run()

if __name__ == "__main__":
    main()
