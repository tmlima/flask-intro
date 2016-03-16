from app import db
from models import BlogPost

#create the database and the db tables
db.create_all()

db.session.add(BlogPost("Good title", "Good description"))
db.session.add(BlogPost("Well title", "Well description"))

#commit the changes
db.session.commit()
