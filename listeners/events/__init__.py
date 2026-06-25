from slack_bolt import App
from .events import streakDashboard


def register(app: App):
    app.event("streakDashboard")(streakDashboard)
