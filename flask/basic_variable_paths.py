from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi yall'

# decorator function
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Sup {name}, you are {number} years old."

if __name__ == "__main__":
    app.run(debug=True)
