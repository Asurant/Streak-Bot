from slack_bolt import App
from .commands import streakCommand


def register(app: App):
    app.command("/streakbot-streaks")(streakCommand)
