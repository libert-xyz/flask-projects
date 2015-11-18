import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy

from flask_blog import app, db


#add all models for db.create_all

from user.models import *
from home.models import *

class UserTest(unittest.TestCase):
    def setUp(self):
        self.db_uri = 'mysql://%s:%s@mysql:3306' % (app.config['DB_USERNAME'], app.config['DB_PASSWORD'])
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED']
        app.config['BLOG_DATABASE_NAME'] = 'test_blog'
        app.config['SQL_ALCHEMY_DATABASE_URI'] = self.db_uri + app.config['BLOG_DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute('commit')
        conn.execute('CREATE DATABASE ' + app.config['BLOG_DATABASE_NAME'])
        db.create_all()
        conn.close()
        self.app = app.test_client()

        def tearDown(self):
            db.session.remove()
            engine = sqlalchemy.create_engine(self.db_uri)
            conn = engine.connect()
            conn.execute('commit')
            conn.execute('DROP DATABASE ' + app.config['BLOG_DATABASE_NAME'])
            conn.close()

        def create_blog(self):
            return self.app.post('/setup',data=dict(
            name="Test Blog",
            fullname="Libert R Schmidt",
            email="libert@libert.xyz",
            username='libert',
            password='pass',
            confirm='test'
            ), follow_redirect=True)

        def test_create_blog(self):
            rv = self.create_blog()
            print rv.data
            assert 'Blog created' in rv.data


if __name__ == '__main__':
    unittest.main()
