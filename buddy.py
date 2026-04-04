import json
import os
import random
from datetime import date

DATA_FILE = os.path.join(os.path.dirname(__file__), "buddy_data.json")

TIPS = [
    "Take a short break every hour to stay focused and refreshed.",
    "Write down your top 3 goals for the day each morning.",
    "Drink a glass of water before your first coffee — your body will thank you.",
    "The best time to start something is now; the second best time is also now.",
    "Review what you accomplished yesterday before planning today.",
    "A rubber duck can solve more bugs than you'd expect. Explain the problem out loud.",
    "Commit early, commit often — small commits are easier to review and revert.",
    "Reading someone else's code is one of the best ways to improve your own.",
    "Name things what they are. Clear names beat clever names every time.",
    "Rest is part of productivity, not the opposite of it.",
    "One focused hour beats three distracted ones.",
    "If it's worth doing, it's worth testing.",
    "Keep a 'wins' list — celebrate small victories to stay motivated.",
    "Simplicity is a feature, not a compromise.",
    "The best documentation is the code you don't have to explain.",
]

GREETINGS = [
    "Hey {name}! Great to see you again — you've visited {count} time(s) so far!",
    "Welcome back, {name}! That's {count} visit(s) and counting!",
    "Oh hey, {name}! Visit number {count} — you're practically a regular!",
    "Hello, {name}! Back again for visit #{count}? Love the dedication!",
]

FIRST_GREETINGS = [
    "Hey there! I'm Buddy, your virtual companion. What should I call you? (For now I'll use 'Friend')",
    "Hello! Nice to meet you — I'm Buddy! I'll be your companion on this journey.",
]


def _load_data() -> dict:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"visits": 0, "last_seen": None, "tip_index": 0}


def _save_data(data: dict) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


class Buddy:
    def __init__(self, name: str = "Friend"):
        self.name = name
        self._data = _load_data()

    def greet(self) -> str:
        self._data["visits"] += 1
        _save_data(self._data)

        if self._data["visits"] == 1:
            return random.choice(FIRST_GREETINGS)

        template = random.choice(GREETINGS)
        return template.format(name=self.name, count=self._data["visits"])

    def daily_tip(self) -> str:
        today = str(date.today())
        if self._data.get("last_seen") == today:
            tip_index = self._data["tip_index"]
        else:
            tip_index = random.randrange(len(TIPS))
            self._data["last_seen"] = today
            self._data["tip_index"] = tip_index
            _save_data(self._data)

        tip = TIPS[tip_index]
        return f"Tip of the day: {tip}"

    def stats(self) -> str:
        visits = self._data["visits"]
        last_seen = self._data.get("last_seen") or "never"
        return f"{self.name} has visited {visits} time(s). Last seen: {last_seen}."
