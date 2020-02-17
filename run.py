from app import app, db, cli
from app.models import User, Reminders

@app.shell_context_processor
def get_context():
    return dict(User = User, Reminders = Reminders, app=app, db=db)
