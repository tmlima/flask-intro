import MySQLdb

conn = MySQLdb.connect(host='localhost',
                       user='admin',
                       passwd='123456',
                       db='flask')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS posts")
c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
c.execute("INSERT INTO posts VALUES('Good Title', 'Good Description')")
c.execute("INSERT INTO posts VALUES('Well Title', 'Well Description')")
conn.commit()
