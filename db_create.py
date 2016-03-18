from project import db
from project.models import BlogPost, User


def create():
    db.create_all()

    author_a = User('Author A', 'author.a@a.com', 'Test@123')
    author_b = User('Author B', 'author.a@a.com', 'Test@123')
    db.session.add(author_a)
    db.session.add(author_b)
    db.session.add(User('admin', 'admin@a.com', 'Test@123'))

    db.session.commit()

    db.session.add(BlogPost("Good title", "Good description", author_a.id))
    db.session.add(BlogPost("Well title", "Well description", author_b.id))
    db.session.add(BlogPost("Great title", "Great description", author_b.id))

    db.session.commit()

if __name__ == '__main__':
    create()
