

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
    ing1 = db.Column(db.Numeric)
    ingu1 = db.Column(db.String(28))
    ingn1 = db.Column(db.String(28))
    ing2 = db.Column(db.Numeric)
    ingu2 = db.Column(db.String(28))
    ingn2 = db.Column(db.String(28))
    ing3 = db.Column(db.Numeric)
    ingu3 = db.Column(db.String(28))
    ingn3 = db.Column(db.String(28))
    ing4 = db.Column(db.Numeric)
    ingu4 = db.Column(db.String(28))
    ingn4 = db.Column(db.String(28))
    ing5 = db.Column(db.Numeric)
    ingu5 = db.Column(db.String(28))
    ingn5 = db.Column(db.String(28))
    ing6 = db.Column(db.Numeric)
    ingu6 = db.Column(db.String(28))
    ingn6 = db. Column(db.String(28))
    ing7 = db.Column(db.Numeric)
    ingu7 = db.Column(db.String(28))
    ingn7 = db.Column(db.String(28))
    ing8 = db.Column(db.Numeric)
    ingu8 = db.Column(db.String(28))
    ingn8 = db.Column(db.String(28))
    ing9 = db.Column(db.Numeric)
    ingu9 = db.Column(db.String(28))
    ingn9 = db.Column(db.String(28))
    ing10 = db.Column(db.Numeric)
    ingu10 = db.Column(db.String(28))
    ingn10 = db.Column(db.String(28))
    ing11 =  db.Column(db.Numeric)
    ingu11 = db.Column(db.String(28))
    ingn11 = db.Column(db.String(28))
    avocado = db.Column(db.Boolean)
    pepper = db.Column(db.Boolean)
    broccoli = db.Column(db.Boolean)
    cauli = db.Column(db.Boolean)
    carrots = db.Column(db.Boolean)
    celery = db.Column(db.Boolean)
    cabbage = db.Column(db.Boolean)
    cucumber = db.Column(db.Boolean)
    grapetom = db.Column(db.Boolean)
    kale = db.Column(db.Boolean)
    lemon = db.Column(db.Boolean)
    lettuce = db.Column(db.Boolean)
    lime = db.Column(db.Boolean)
    mushroom = db.Column(db.Boolean)
    peas = db.Column(db.Boolean)
    poblano = db.Column(db.Boolean)
    potatoes = db.Column(db.Boolean)
    redcab = db.Column(db.Boolean)
    scallion = db.Column(db.Boolean)
    snowpea = db.Column(db.Boolean)
    spinach = db.Column(db.Boolean)
    sweetpotato = db.Column(db.Boolean)
    tomato = db.Column(db.Boolean)
    zucchini = db.Column(db.Boolean)

    def __init__(self, name, description, directions, ing1, ingu1, ingn1, ing2, ingu2, ingn2, ing3, ingu3, ingn3, ing4, ingu4, ingn4, ing5, ingu5, ingn5,
    ing6, ingu6, ingn6, ing7, ingu7, ingn7, ing8, ingu8, ingn8, ing9, ingu9, ingn9, ing10, ingu10, ingn10, ing11, ingu11, ingn11, avocado, pepper, broccoli, cauli, carrots,
    celery, cabbage, cucumber, grapetom, kale, lemon, lettuce, lime, mushroom, peas, poblano, potatoes, redcab, scallion, snowpea, spinach, sweetpotato,
    tomato, zucchini):
        self.name = name
        self.description = description
        self.directions = directions
        self.ing1 = ing1
        self.ingu1 = ingu1
        self.ingn1 = ingn1
        self.ing2 = ing2
        self.ingu2 = ingu2
        self.ingn2 = ingn2
        self.ing3 = ing3
        self.ingu3 = ingu3
        self.ingn3 = ingn3
        self.ing4 = ing4
        self.ingu4 = ingu4
        self.ingn4 = ingn4
        self.ing5 = ing5
        self.ingu5 = ingu5
        self.ingn5 = ingn5
        self.ing6 = ing6
        self.ingu6 = ingu6
        self.ingn6 = ingn6
        self.ing7 = ing7
        self.ingu7 = ingu7
        self.ingn7 = ingn7
        self.ing8 = ing8
        self.ingu8 = ingu8
        self.ingn8 = ingn8
        self.ing9 = ing9
        self.ingu9 = ingu9
        self.ingn9 = ingn9
        self.ing10 = ing10
        self.ingu10 = ingu10
        self.ingn10 = ingn10
        self.ing11 = ing11
        self.ingu11 = ingu11
        self.ingn11 = ingn11
        self.avocado = avocado
        self.pepper = pepper
        self.broccoli = broccoli
        self.cauli = cauli
        self.carrots = carrots
        self.celery = celery
        self.cabbage = cabbage
        self.cucumber = cucumber
        self.grapetom = grapetom
        self.kale = kale
        self.lemon = lemon
        self.lettuce = lettuce
        self.lime = lime
        self.mushroom = mushroom
        self.peas = peas
        self.poblano = poblano
        self.potatoes = potatoes
        self.redcab = redcab
        self.scallion = scallion
        self.snowpea = snowpea
        self.spinach = spinach
        self.sweetpotato = sweetpotato
        self.tomato = tomato
        self.zucchini = zucchini


@app.route("/addnew", methods=["GET","ADD"])
def addnew():
    if request.method == "GET":
        render_template("addnew.html")

    if request.method == "ADD":
        name = request.form["name"]
        description = request.form["description"]
        directions = request.form["steps"]
        ing1 = request.form["ing"]
        ingu1 = request.form["ingu"]
        ingn1 = request.form["ingn"]
        ing2 = request.form["ing1"]
        ingu2 = request.form["ingu1"]
        ingn2 = request.form["ingn1"]
        ing3 = request.form["ing2"]
        ingu3 = request.form["ingu2"]
        ingn3 = request.form["ingn2"]
        ing4 = request.form["ing3"]
        ingu4 = request.form["ingu3"]
        ingn4 = request.form["ingn3"]
        ing5 = request.form["ing4"]
        ingu5 = request.form["ingu4"]
        ingn5 = request.form["ingn4"]
        ing6 = request.form["ing5"]
        ingu6 = request.form["ingu5"]
        ingn6 = request.form["ingn5"]
        ing7 = request.form["ing6"]
        ingu7 = request.form["ingu6"]
        ingn7 = request.form["ingn6"]
        ing8 = request.form["ing7"]
        ingu8 = request.form["ingu7"]
        ingn8 = request.form["ingn7"]
        ing9 = request.form["ing8"]
        ingu9 = request.form["ingu8"]
        ingn9 = request.form["ingn8"]
        ing10 = request.form["ing9"]
        ingu10 = request.form["ingu9"]
        ingn10 = request.form["ingn9"]
        ing11 = request.form["ing0"]
        ingu11 = request.form["ingu0"]
        ingn11 = request.form["ingn0"]
        avocado = request.form.get("avocado")
        pepper = request.form.get("pepper")
        broccoli = request.form.get("broccoli")
        cauli = request.form.get("cauli")
        carrots = request.form.get("carrots")
        celery = request.form.get("celery")
        cabbage = request.form.get("cabbage")
        cucumber = request.form.get("cucumber")
        grapetom = request.form.get("grapetom")
        kale = request.form.get("kale")
        lemon = request.form.get("lemon")
        lettuce = request.form.get("lettuce")
        lime = request.form.get("lime")
        mushroom = request.form.get("mushroom")
        peas = request.form.get("peas")
        poblano = request.form.get("poblano")
        potatoes = request.form.get("potatoes")
        redcab = request.form.get("redcab")
        scallion = request.form.get("scallion")
        snowpea = request.form.get("snowpea")
        spinach = request.form.get("spinach")
        sweetpotato = request.form.get("sweepotato")
        tomato = request.form.get("tomato")
        zucchini = request.form.get("zucchini")
        r1 = Recipe(name, description, directions, ing1, ingu1, ingn1, ing2, ingu2, ingn2, ing3, ingu3, ingn3, ing4, ingu4, ingn4, ing5, ingu5, ingn5,
        ing6, ingu6, ingn6, ing7, ingu7, ingn7, ing8, ingu8, ingn8, ing9, ingu9, ingn9, ing10, ingu10, ingn10, ing11, ingu11, ingn11, avocado, pepper, broccoli, cauli, carrots,
        celery, cabbage, cucumber, grapetom, kale, lemon, lettuce, lime, mushroom, peas, poblano, potatoes, redcab, scallion, snowpea, spinach, sweetpotato,
        tomato, zucchini)
        db.session.add(r1)
        db.session.commit()
        return redirect(url_for('addnew'))

    return render_template("addnew.html")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", names=Recipe.query.all())

