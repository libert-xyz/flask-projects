from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('settings')

#migrations

migrate = Migrate(app, db)


from home import views
from user import views
