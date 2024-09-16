import json

class HistoryManager:
    def __init__(self, file_name='gecmis.json'):
        self.file_name = file_name
        self.history = self.load_history()

    def load_history(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_history(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.history, file)

    def add_to_history(self, calculation):
        self.history.append(calculation)
        if len(self.history) > 10:  # Son 10 işlemi sakla
            self.history = self.history[-10:]
        self.save_history()

    def get_history(self):
        return self.history
