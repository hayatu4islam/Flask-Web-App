from flask import Flask, redirect, abort, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world! My name is Hayat"


@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)


@app.route("/red")
def red_index():
    return redirect('http://google.com')


# @app.route('/user/<name>')
# def get_user(name):
#     # user = get_user(name)
#     if len(name) < 4:
#         abort(404) # throws an exception
#     return 'Hello, {}'.format(user.name)

