# ---- Flask Hello World ---- #
# Import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# Debugging
app.config["DEBUG"]

# Use the decorator pattern to link the view function to a url
@app.route("/")
def hello_world1():
    return "Hello, world!"

@app.route("/search/<search_query>")
def search(search_query):
    return search_query


@app.route("/int/<int:value>")
def integer1(value):
    return "correct"

@app.route("/hello")

# Define the view using a function, which returns a string
def hello_world():
    return "Hello, Sandeep!"


@app.route("/name/<value>")
def namematch(value):
	if value.lower() == "sandeep" :
		return "hello, {}".format(value), 200
	else:
	    return "not found", 404

# Start the development server using the run() method

if __name__ == "__main__":
    app.run()