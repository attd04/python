import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    token = request.form['token']
    project_id = request.form['project_id']
    model = request.form['model']
    image_file = request.files['file']

    if image_file:
        file_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(file_path)  # Save image to the server

        headers = {"X-Auth-token": token, "Content-Type": "application/octet-stream"}
        image_data = open(file_path, 'rb').read()
        response = requests.post(f'https://platform.sentisight.ai/api/predict/{project_id}/{model}/',
                                 headers=headers, data=image_data)

        if response.status_code == 200:
            return render_template('results.html', results=response.json(), image_url=file_path)
        else:
            return f'Error occurred with REST API. Status code: {response.status_code}\nError message: {response.text}'

if __name__ == '__main__':
    app.run(debug=True)
