from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flaskext.markdown import Markdown
app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('settings')

#migrations

migrate = Migrate(app, db)



md = Markdown(app, extensions=['fenced_code', 'tables'])

from home import views
from user import views
