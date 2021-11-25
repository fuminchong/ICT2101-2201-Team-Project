from flask import Flask
from datetime import datetime
import re
from flask import render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/lessonplan", methods=["POST", "GET"])
def setlessonplan():
    with open('./static/data.json') as json_data:
        lesson_data = json.load(json_data)
    if request.method == "POST":
        lessonplan = request.form["lp"]
        if lessonplan in lesson_data["lessonplanA"]:
            return redirect(url_for("lessonplanA"))
        elif lessonplan in lesson_data["lessonplanB"]:
             return redirect(url_for("lessonplanB"))
        elif lessonplan in lesson_data["lessonplanC"]:
            return redirect(url_for("lessonplanC"))



def home():
    return render_template("home.html")
# New functions
@app.route("/validatepin/", methods=["POST", "GET"])
def validatepin():
    
    error = None
    
    with open('./static/data.json') as json_data:
        pin_data = json.load(json_data)
    
    if request.method == "POST":
        pin = request.form["fpin"]
        if pin in pin_data["pin"]:
            return redirect(url_for("lessonplan"))
        else:
            error = 'Invalid PIN. Please try again.'
    
    return render_template("validatepin.html", error = error)

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
    return app.send_static_file("data.json")