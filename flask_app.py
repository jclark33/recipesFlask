

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import not_
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

menu = []

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
        if request.form["ingn9"]:
            ing = Ingredient(name=request.form["ingn9"], amount=request.form["ing9"], unit= request.form["ingu9"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn10"]:
            ing = Ingredient(name=request.form["ingn10"], amount=request.form["ing10"], unit= request.form["ingu10"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn11"]:
            ing = Ingredient(name=request.form["ingn11"], amount=request.form["ing11"], unit= request.form["ingu11"], recipe_id=r1.id)
            db.session.add(ing)
        if request.form["ingn12"]:
            ing = Ingredient(name=request.form["ingn12"], amount=request.form["ing12"], unit= request.form["ingu12"], recipe_id=r1.id)
            db.session.add(ing)
        db.session.commit()
        return redirect(url_for('addnew'))


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        term = request.form["search"]
        return render_template("results.html", ingredients = Ingredient.query.filter(Ingredient.name.contains(term)).all(), recipes = db.session.query(Recipe).join(Ingredient).filter(Ingredient.name.contains(term)).all())
    return render_template("index.html", recipes = Recipe.query.all())

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method=="POST":
        term = request.form["name"]
        recipe = Recipe.query.filter(Recipe.name.like(term)).first()
        menu.append(recipe.id)
    return redirect(url_for('index'))

@app.route("/menu", methods=["GET","POST"])
def createMenu():
    if request.method=="POST":
        menu.clear()
    return render_template("menu.html", recipes = Recipe.query.filter(Recipe.id.in_(menu)).all(), ingredients = Ingredient.query.all())

@app.route("/build", methods=["GET","POST"])
def buildMenu():
    if request.method=="POST":
        ingredients = Ingredient.query.all()
        note = []
        for ingredient in ingredients:
            for row in menu:
                if ingredient.recipe_id == row:
                    note.append(ingredient.name)
    return render_template("results.html", ingredients = Ingredient.query.filter(Ingredient.name.in_(note), not_(Ingredient.recipe_id.in_(menu))).all(), recipes = db.session.query(Recipe).join(Ingredient).filter(Ingredient.name.in_(note), not_(Ingredient.recipe_id.in_(menu))).all())

@app.route("/grocery", methods=["GET","POST"])
def printList():
    if request.method=="POST":
        return render_template("grocerylist.html", ingredients = db.session.query(Ingredient.name, Ingredient.unit, db.func.sum(Ingredient.amount).label("sum_amt")).group_by(Ingredient.name).filter(Ingredient.recipe_id.in_(menu)).all())

@app.route("/remove", methods=["GET","POST"])
def deleteRecipe():
    if request.method=="POST":
        term = request.form["delname"]
        recipe = Recipe.query.filter(Recipe.name.like(term)).first()
        ingredients = Ingredient.query.filter(Ingredient.recipe_id==recipe.id).all()
        for ingredient in ingredients:
            db.session.delete(ingredient)
        db.session.delete(recipe)
        db.session.commit()
    return redirect(url_for('index'))

@app.route("/alter", methods=["GET","POST"])
def alterRecipe():
    if request.method=="POST":
        term = request.form["rec"]
        recipe = Recipe.query.filter(Recipe.name.like(term)).first()
        ingredients = Ingredient.query.filter(Ingredient.recipe_id==recipe.id).all()
        b = recipe.id
        nums = []
        for ingredient in ingredients:
            nums.append(ingredient.id)
            db.session.delete(ingredient)

        r1 = Recipe(id=b, name= request.form["name"], description = request.form["description"], directions = request.form["steps"])
        db.session.delete(recipe)
        db.session.add(r1)
        for n in nums:
            name = "ing" + str(n)
            amount = "ingn" + str(n)
            unit = "ingu" + str(n)
            if request.form[name]:
                part = Ingredient(id = n, name=request.form[name], amount=request.form[amount], unit= request.form[unit], recipe_id=r1.id)
                db.session.add(part)
        for i in range(1,3):
            name = "ing" + str(i)
            amount = "ingn" + str(i)
            unit = "ingu" + str(i)
            if request.form[name]:
                part = Ingredient(name=request.form[name], amount=request.form[amount], unit= request.form[unit], recipe_id=r1.id)
                db.session.add(part)
        db.session.commit()
    return redirect(url_for('index'))

@app.route("/edit", methods=["GET","POST"])
def editRecipe():
    if request.method=="POST":
        term = request.form["editname"]
        result = Recipe.query.filter(Recipe.name.like(term)).first()
        return render_template("edit.html", recipe = result, ingredients = Ingredient.query.filter(Ingredient.recipe_id == result.id).all(), x = 1)


