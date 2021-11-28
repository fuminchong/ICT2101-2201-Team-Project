<<<<<<< Updated upstream
from flask import Flask
from datetime import datetime
import re
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/scratch/")
def scratch():
    return render_template("scratch.html")

@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
=======
from flask import Flask
from datetime import datetime
import re
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/validatepin/")
def validatepin():
    return render_template("validatepin.html")

@app.route("/scratcheasy/")
def scratcheasy():
    return render_template("scratcheasy.html")

@app.route("/scratcheasy2/")
def scratcheasy2():
    return render_template("scratcheasy2.html")

@app.route("/scratchmedium/")
def scratchmed():
    return render_template("scratchmedium.html")

# @app.route("/scratchhard/")
# def scratchhard():
#     return render_template("scratchhard.html")


@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
>>>>>>> Stashed changes
    return app.send_static_file("data.json")