from flask import Flask
import random

# day 55 - higher lower URLS

app = Flask(__name__)

# get random number
random_number = random.randint(1, 9)
print(random_number)


# home app route
@app.route('/')
def home():
    return '<h1 style="color:blue"> Guess a number between 0 and 9!! </h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def number(number):
    if number < random_number:
        return '<h1 style="color:purple">Too low!</h1>' \
               '<br></br>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTVwM29jZHdkYnJsM283c3l0ank0cHUwcGt4NWo4c2w2NTdhYWJqZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9Wu8LqCQeeaGY/giphy.gif">'

    elif number > random_number:
        return '<h1 style="color:red">Too high!!</h1>' \
               '<br></br>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmtrcDRoZjNnMGtnbjNmeDBqNW0wcDh0eG1vbW8wbXBodjk3NjdoZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gj0IKRLgBFap2TlcoD/giphy.gif">'

    elif number == random_number:
        return '<h1 style="color:green">You got it!!</h1>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjBucnpueTI2anIzOWJwMG9sMnJvd3hjd2F3cWN4dnpybmQ3bnQ0cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GeimqsH0TLDt4tScGw/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True, port=8000)
