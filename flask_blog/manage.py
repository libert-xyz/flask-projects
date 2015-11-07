import os, sys

sys.path.open.append(os.path.abspatch(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from flask_blog import app

manager = Manager(app)

manager.add_command("runserver", Server(
    use_debuger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = '5000')
))


if __name__ = "__main__":
    manager.run()
    
