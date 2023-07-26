from flask import Flask, redirect, url_for, render_template, request
from flask_pyngrok import ngrok
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return "HOME PAGE"


@app.route('/square/<int:usr>')
def user(usr):
    sq = usr ** 2
    return render_template("index.html", num=usr, sq_num=sq)


@app.route("/uploadimagepath")
def image():
    return render_template("uploadimage.html")


@app.route("/table/<int:no>")
def table(no):
    table = [var * no for var in range(1, 10)]
    return render_template('tabledisplay.html', n=table)


@app.route('/convertHash', methods=['GET', 'POST'])
def convertHash():
    if request.method == 'POST':
        image = request.form['Path']
        # Convert the Image into md5Hash
        with open(image, "rb") as f:
            im_bytes = f.read()
        im_hash = str(hashlib.md5(im_bytes).hexdigest())
        return "<b>md5Hash of the Image :  </b>" + im_hash


if __name__ == '__main__':
    app.run()
