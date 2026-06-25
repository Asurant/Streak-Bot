from slack_bolt import App
from .views import addStreak


def register(app: App):
    app.view("addStreak")(addStreak)
