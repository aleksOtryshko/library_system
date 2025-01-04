class Action:
    """
    Класс для описания действия в системе.
    """
    def __init__(self, name: str, callback):
        self.name = name
        self.callback = callback

    def execute(self):
        return self.callback()
