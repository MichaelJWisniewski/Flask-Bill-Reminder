from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(180), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Reminders', backref='author', lazy='dynamic') 

    def __repr__(self):
        return f"<User: {self.name}|{self.email}>"

    def generate_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Reminders(db.Model):
    reminder_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    repeat = db.Column(db.Boolean, nullable=False)
    enabled = db.Column(db.Boolean, nullable=False)
    amount = db.Column(db.String(8), nullable=False)
    due_on = db.Column(db.String(8), nullable=False)
    remind_on = db.Column(db.String(8), nullable=False)

    #def __repr__(self):
        #returnf"<Post: {self.user_id}: {self.body[:20]}>"

@login.user_loader
def get_user(id):
    return User.query.get(int(id))




