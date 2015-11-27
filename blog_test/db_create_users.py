from app import db
from models import User



db.session.add(User('pierre','pierre@libert.xyz','sesamo'))
db.session.add(User('paris','paris@libert.xyz','sesamo'))


db.session.commit()
