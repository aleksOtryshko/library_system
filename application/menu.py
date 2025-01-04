class Menu:
    """
    Класс для работы с меню CLI.
    """
    def __init__(self):
        self.options = {}

    def add_option(self, key: str, action_name: str, action_callback):
        self.options[key] = {"name": action_name, "callback": action_callback}

    def show(self):
        for key, option in self.options.items():
            print(f"{key}. {option['name']}")
        print("4. Exit")  # Добавлен пункт для выхода

    def execute(self, key: str):
        if key in self.options:
            self.options[key]["callback"]()
        else:
            print("Invalid option.")
