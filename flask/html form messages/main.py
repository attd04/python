from flask import Flask, render_template, request
import smtplib

EMAIL = "tumtiede123@gmail.com"
PASSWORD = "dlzfbgyplkxuidup"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        name = request.form['name']
        passw = request.form["password"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="au_tiede@yahoo.com",
                                msg="Subject: New message!\n\n"
                                    f"{message}\n"
                                    f"from: {name} <3")

    return f"<h1> {name} {passw}, your message was received. </h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5003)
