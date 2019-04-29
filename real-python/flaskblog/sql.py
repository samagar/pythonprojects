# Create Database connection

with SQLite3.connect("blog.db") as conn:
	curs = conn.cursor()


# Create Table to hold blog post data

	curs.execute("DROP TABLE if exists flaskblogpost")
	curs.execute("CREATE TABLE flaskblogpost(title TEXT, Blogdata TEXT")

# Populate some Data
	myposts = [("post1","timepass"),
			   ("post2","tiumepass2"),
			   ("post3","timepass3")]


	curs.executemany("INSERT INTO flaskblogpost(?,?,?)", myposts)


