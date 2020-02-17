from flask import Flask

app = Flask(__name__)

from config import Config
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

from app.blueprints.main import main
app.register_blueprint(main, url_prefix='/')

from flask_login import LoginManager
login = LoginManager(app)
login.login_view = 'account.login'
login.login_message_category = 'danger'

from app.blueprints.account import account
app.register_blueprint(account, url_prefix='/account')

from app import models, cli