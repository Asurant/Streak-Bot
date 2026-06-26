from slack_bolt import App
from .actions import createStreak, completeStreak, deleteStreak

def register(app: App):
    app.action("createStreak")(createStreak)
    app.action("completeStreak")(completeStreak)
    app.action("deleteStreak")(deleteStreak)
