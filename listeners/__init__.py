
from .commands.commands import streakCommand
from .actions.actions import createStreak
from .actions.actions import completeStreak
from .actions.actions import deleteStreak
from .views.views import addStreak
from .events.events import streakDashboard

def register_listeners(app):
    app.command("/streakbot-streaks")(streakCommand)
    app.action("createStreak")(createStreak)
    app.action("completeStreak")(completeStreak)
    app.action("deleteStreak")(deleteStreak)
    app.view("createStreak")(addStreak)
    app.event("app_home_opened")(streakDashboard)

