from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'Add your name with a forward slash to have your gender and age guessed'


@app.route('/guess/<name>')
def hello(name):
    gender_url = f"https://api.genderize.io?name={name}"
    g_response = requests.get(gender_url).json()
    gender_guess = g_response['gender']

    age_url = f"https://api.agify.io?name={name}"
    a_response = requests.get(age_url).json()
    age_guess = a_response['age']

    return render_template("index.html", name=name.capitalize(),
                           gender=gender_guess,
                           age=age_guess)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
