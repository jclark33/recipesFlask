

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
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
migrate = Migrate(app, db)

class Recipe(db.Model):

    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(151))
    description = db.Column(db.String(251))
    directions = db.Column(db.String(4096))

class Ingredient(db.Model):

     __tablename__ = "pantry"

     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(28))
     amount = db.Column(db.Numeric)
     unit = db.Column(db.String(15))
     recipe_id = db.Column(db.Integer, db.ForeignKey('book.id'),nullable=True)
     recipe = db.relationship('Recipe', foreign_keys=recipe_id)


@app.route("/addnew", methods=["GET","POST"])
def addnew():
    if request.method == 'GET':
        return render_template("addnew.html")
    elif request.method == 'POST':
        r1 = Recipe(name= request.form["name"], description = request.form["description"], directions = request.form["steps"])
        db.session.add(r1)
        db.session.commit()

        if request.form["ingn"]:
            ing = Ingredient(name=request.form["ingn"], amount=request.form["ing"], unit= request.form["ingu"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn1"]:
            ing = Ingredient(name=request.form["ingn1"], amount=request.form["ing1"], unit= request.form["ingu1"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn2"]:
            ing = Ingredient(name=request.form["ingn2"], amount=request.form["ing2"], unit= request.form["ingu2"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn3"]:
            ing = Ingredient(name=request.form["ingn3"], amount=request.form["ing3"], unit= request.form["ingu3"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn4"]:
            ing = Ingredient(name=request.form["ingn4"], amount=request.form["ing4"], unit= request.form["ingu4"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn5"]:
            ing = Ingredient(name=request.form["ingn5"], amount=request.form["ing5"], unit= request.form["ingu5"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn6"]:
            ing = Ingredient(name=request.form["ingn6"], amount=request.form["ing6"], unit= request.form["ingu6"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn7"]:
            ing = Ingredient(name=request.form["ingn7"], amount=request.form["ing7"], unit= request.form["ingu7"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn8"]:
            ing = Ingredient(name=request.form["ingn8"], amount=request.form["ing8"], unit= request.form["ingu8"], recipe_id=r1.id)
            db.session.add(ing)

        db.session.commit()
        return redirect(url_for('addnew'))


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        term = request.form["search"]
        return render_template("results.html", ingredients = Ingredient.query.filter_by(name = term).all())
    recipes = Recipe.query.all()
    return render_template("index.html",recipes = recipes)






