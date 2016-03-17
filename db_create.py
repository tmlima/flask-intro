from app import db
from models import BlogPost, User

#create the database and the db tables
db.create_all()

authorA = User('Author A', 'author.a@a.com', 'Teste@123')
authorB = User('Author B', 'author.a@a.com', 'Teste@123')
db.session.add(authorA)
db.session.add(authorB)

db.session.commit()

db.session.add(BlogPost("Good title", "Good description", authorA.id))
db.session.add(BlogPost("Well title", "Well description", authorB.id))
db.session.add(BlogPost("Greate title", "Greate description", authorB.id))

#commit the changes
db.session.commit()
