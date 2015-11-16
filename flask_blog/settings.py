SECRET_KEY = "Pierre"
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'pass'
BLOG_DATABASE_NAME = 'blog'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@mysql:3306/%s' %(DB_USERNAME,DB_PASSWORD,BLOG_DATABASE_NAME)
UPLOADED_IMAGES_DEST = '/opt/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
