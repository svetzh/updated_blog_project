from flask import Flask, render_template
from datetime import datetime
import requests

posts = requests.get('https://api.npoint.io/83d37732f2dee611796e').json()
app = Flask(__name__)
current_year = datetime.now().year

@app.route("/")
def get_all_posts():
    return render_template('index.html', all_posts=posts, current_year=current_year)

# @app.route('/')
# def home():
#     current_year = datetime.now().year
#     return render_template("index.html", current_year=current_year)

@app.route("/about")
def about():
    current_year = datetime.now().year
    return render_template("about.html", current_year=current_year)

@app.route("/contact")
def contact():
    current_year = datetime.now().year
    return render_template("contact.html", current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
