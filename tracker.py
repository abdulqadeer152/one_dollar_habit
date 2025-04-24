# tracker.py
import json
from datetime import datetime, timedelta

class Habit:
    def __init__(self, name):
        self.name = name
        self.streak = 0
        self.last_completed = None

    def mark_done(self):
        today = datetime.today().date()
        if self.last_completed == today:
            return False  # Already done today

        if self.last_completed == today - timedelta(days=1):
            self.streak += 1
        else:
            self.streak = 1  # Reset streak

        self.last_completed = today
        return True

    def to_dict(self):
        return {
            'name': self.name,
            'streak': self.streak,
            'last_completed': self.last_completed.isoformat() if self.last_completed else None
        }

    @staticmethod
    def from_dict(data):
        habit = Habit(data['name'])
        habit.streak = data['streak']
        habit.last_completed = datetime.fromisoformat(data['last_completed']).date() if data['last_completed'] else None
        return habit

class Tracker:
    def __init__(self):
        self.habits = []
        self.earnings = 0
        self.load_data()

    def add_habit(self, name):
        self.habits.append(Habit(name))
        self.save_data()

    def complete_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                if habit.mark_done():
                    self.earnings += 1
                    self.save_data()
                    return True
                else:
                    return False
        return None

    def get_habits(self):
        return self.habits

    def get_earnings(self):
        return self.earnings

    def save_data(self):
        with open('data.json', 'w') as f:
            json.dump({
                'habits': [h.to_dict() for h in self.habits],
                'earnings': self.earnings
            }, f)

    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.earnings = data.get('earnings', 0)
                self.habits = [Habit.from_dict(h) for h in data.get('habits', [])]
        except FileNotFoundError:
            self.habits = []
            self.earnings = 0
