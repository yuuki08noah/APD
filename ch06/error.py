class Missing(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Duplicated(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)