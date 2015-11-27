from project import db
from project.models import BlogPost

#create the database and db tables
db.create_all()

#insert
db.session.add(BlogPost('Peluchin', 'ten years'))
db.session.add(BlogPost('Paris', 'five years'))
db.session.add(BlogPost('Pierre', '3 years'))


#commit the changes
db.session.commit()
