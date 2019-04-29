
# imports
import sqlite3

from flask import Flask, render_template, request, session, \
     flash, redirect, url_for, g


# Config
DATABASE = "blog.db"

app = Flask(__name__)


# Pulls in app config by looking in uppercase variables
app.config.from_object(__name__)

# Function to connect to Db

def connect_db():
	return SQLite3.connect(app.config("DATABASE"))


@app.route("/main")
def main():
	return render_template("main.html")


@app.route("/")
def login():
	return render_template("login.html")


if __name__ == '__main__':
	app.run(debug=True)

