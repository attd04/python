from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hi yall </h1>' \
            '<p> this is a paragraph </p>' \
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWQ4NjgwbXgydm5hZHgzNHNvY3A5eDFrY2E5a25ucDR4eG0ydzM5aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GeimqsH0TLDt4tScGw/giphy.gif" width=400>'


# decorator functions
@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Sup {name}, you are {number} years old."


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'bye bye'


if __name__ == "__main__":
    app.run(debug=True)
