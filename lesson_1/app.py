import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello World"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query


# dynamic route that takes ints
@app.route("/integer/<int:value>")
def float_type(value: int):
    return str(value + 1)

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value: str):
    return value.replace("/", " ")

# example of also returning status codes
@app.route("/name/<name>")
def index(name: str):
    if name.lower() == "micheal":
        print("found it")
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()
