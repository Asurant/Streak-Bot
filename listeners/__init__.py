
from .commands import streakCommand
from .actions import createStreak
from .actions import completeStreak
from .actions import deleteStreak
from .views import addStreak
from .events import streakDashboard

def register_listeners(app):
    app.command("/streak")(streakCommand)
    app.action("createStreak")(createStreak)
    app.action(completeStreak)(completeStreak)
    app.action(deleteStreak)(deleteStreak)
    app.view(addStreak)(addStreak)
    app.event(streakDashboard)(streakDashboard)

