
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
# the database password is hellodata

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="jclark33",
    password="hellodata",
    hostname="jclark33.mysql.pythonanywhere-services.com",
    databasename="jclark33$mysite",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))

@app.route("/addnew", methods=["GET","ADD"])
def addnew():
    if request.method == "GET":
        # YOU LEFT OFF HERE GENIUS

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", comments=Recipe.query.all())

    comment = Recipe(name = request.form["name"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

