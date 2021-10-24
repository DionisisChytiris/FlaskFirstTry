from flask import Flask, render_template

app = Flask(__name__)

# jinja


# @app.route('/user/<name>')
# def user(name):
#     return render_template('test.html', name=name)


@app.route('/user/<name>')
def user(name):
    first_name = 'Dionysis'
    stuff = 'This is <strong>Bold Text</strong>.'
    staff = 'This is <strong>bold text</strong>.'
    stoff = 'This is bold text.'

    favorite_pizza = ['Pepperoni', 'Cheese', 'Mushroom', 'Margarita', 41]
    return render_template('test.html', first_name=first_name, stuff=stuff, staff=staff, stoff=stoff, favorite_pizza=favorite_pizza)


# CREATE CUSTOM ERROR PAGES

# INVALID URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
