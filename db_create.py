from project import db
from project.models import BlogPost, User

def create():
    db.create_all()

    author_a = User('Author A', 'author.a@a.com', 'Teste@123')
    author_b = User('Author B', 'author.a@a.com', 'Teste@123')
    db.session.add(author_a)
    db.session.add(author_b)
    db.session.add(User('admin', 'admin@a.com', 'Teste@123'))

    db.session.commit()

    db.session.add(BlogPost("Good title", "Good description", author_a.id))
    db.session.add(BlogPost("Well title", "Well description", author_b.id))
    db.session.add(BlogPost("Greate title", "Greate description", author_b.id))

    db.session.commit()
