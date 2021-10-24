from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
# def hello():
#     return "Hello! This is the main page. <h1>HELLO WORLD<h1>"
# use the templates folder to show up webpage content
def hello():
    return render_template('hello.html')


# @app.route("/user")
# def user():
#     return "Hello! This is the user page. <h1>HELLO USER<h1> <li>Dennis<li><li>George<li>"


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {}</h1>'.format(name)


# if __name__ == "__name__":
#     app.run()
