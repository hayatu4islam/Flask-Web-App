from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world! My name is Hayat"


@app.route("/user/<name>")
def user(name):
    return f'Hello, {name}'


