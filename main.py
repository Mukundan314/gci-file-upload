import os
from flask import Flask, redirect, request, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', files=os.listdir('uploads'))


@app.route('/upload', methods=["POST"])
def upload():
    filename = secure_filename(request.form.get('filename'))

    if os.path.exists(os.path.join('uploads', filename)):
        return render_template('title_taken.html', title=filename)

    request.files['file'].save(os.path.join('uploads', filename))
    return redirect("/")


@app.route('/uploads/<path:path>')
def get_upload(path):
    return send_from_directory('uploads', path)


if __name__ == "__main__":
    app.run(debug=True)
