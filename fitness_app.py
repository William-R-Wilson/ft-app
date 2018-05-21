from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/ft-fitness'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150), unique=True)
    name=db.Column(db.String(150))

    def __init__(self, email_, name_):
        self.email_=email_
        self.height_=height_

class Measurement(db.Model):
    __tablename__ = "measurement"
    id=db.Column(db.Integer, primary_key=True)
    height_ft=db.Column(db.Integer)
    height_inches=db.Column(db.Integer)
    weight=db.Column(db.Integer)

    def __init__(self, height_ft_, height_inches_, weight_):
        self.height_ft_ = height_ft_
        self.height_inches_=height_inches_
        self.weight_=weight_


@app.route('/')

def home():
    return render_template("home.html")

@app.route('/about')

def about():
    return render_template("about.html")

@app.route('/new_user')

def new_user():
    return render_template("new_user.html")

@app.route('/add_user', methods=["POST"])
def add_user():
    if request.method == 'POST':
        print(request)
        return render_template('new_measurement.html')

@app.route('/new_measurement')
def new_measurement():
    return render_template("new_measurement.html")

@app.route('/add_measurement', methods=["POST"])
def add_measurement():
    if request.method =='POST':
        print(request)
        return render_template('measurements.html')


@app.route('/measurements')
def measurements():
    return render_template("measurements.html")

if __name__== "__main__":
    app.run(debug=True)
