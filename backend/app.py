from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return {'message': 'File uploaded successfully'}, 200

if __name__ == "__main__":
    app.run(debug=True)

