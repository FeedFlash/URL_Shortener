from uuid import uuid4
from flask import Flask, request, render_template, redirect,  url_for
import os

db = {}
app = Flask(__name__)

@app.route('/', methods =["GET"])
def index():
    return render_template("index.html")


@app.route("/create_from_shortened", methods=["POST"])
def create_shortened():
    if request.method == "POST":
        url = request.form.get("url")
        shortened_url = shorten(url)
        print(shortened_url)
    return render_template("result.html", shortened_url=shortened_url)

@app.route("/<key>", methods=["GET"])
def get_shortened(key):
    print(db)
    url = db.get(key)
    if url:
        return redirect(url)
    return redirect(url_for('index'))

def shorten(url):
    key = uuid4().hex
    short_key = key[:7]
    db[short_key] = url
    return "/".join((request.host_url.strip("/"), short_key))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)