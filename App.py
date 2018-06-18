# ---- Flask Hello World ---- #
# Import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# Error Handling
app.config["DEBUG"] = True

# Use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/hello")

# Define the view using a function, which returns a string
def hello_world():
    return "Hello, Sandeep!"

# New route
@app.route("/test/<squery>")
def search(squery):
	return squery


@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
    	return "Hello, {}".format(name),  200
    else:
    	return "Not Found dudes", 404


# Start the development server using the run() method
if __name__ == "__main__":
    app.run()