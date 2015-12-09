import os
import unittest
import coverage
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(branch=True, include='project/*')
    cov.start()
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print 'Coverage Summary:'
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()


if __name__ == '__main__':
    manager.run()
