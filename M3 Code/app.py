from flask import Flask
from datetime import datetime
import re
from flask import render_template, request, redirect, url_for
import json
from car import carController


app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
@app.route("/", methods=["POST", "GET"])
def home():

    with open('static/level.txt', 'w') as f:        # Dis code to reset the level.txt file
        f.write("") 

    error = None
    
    with open('./static/data.json') as json_data:
        pin_data = json.load(json_data)
    
    if request.method == "POST":
        pin = request.form["fpin"]
        if pin in pin_data["pin"]:
            return render_template("lessonplans.html")
        else:
            error = 'Invalid PIN. Please try again.'
    
    return render_template("home.html", error = error)


# New functions
@app.route("/validatepin/")
def validatepin():
    return render_template("validatepin.html")


@app.route("/scratcheasy", methods=['GET', 'POST'])
def scratcheasy():
    with open('static/level.txt', 'w') as f:        # Dis code to reset the level.txt file
        f.write("")                                 # Dis code to reset the level.txt file
    if request.method=="POST":                      # When user submit code
        level = "Easy"           # Get user input on Easy / Medium / Hard
        with open('static/level.txt', 'w') as f:    # Write difficulty level into level.txt
            f.write(level)                          # Write difficulty level into level.txt
        return redirect(url_for("dashboard"))      # Open dashboard page
    return render_template("scratcheasy.html")

@app.route("/scratcheasy2/")
def scratcheasy2():
    return render_template("scratcheasy2.html")


@app.route("/scratchmedium", methods=['GET', 'POST'])
def scratchmedium():
    with open('static/level.txt', 'w') as f:        # Dis code to reset the level.txt file
        f.write("")                                 # Dis code to reset the level.txt file
    if request.method=="POST":                      # When user submit code
        level = "Medium"           # Get user input on Easy / Medium / Hard
        with open('static/level.txt', 'w') as f:    # Write difficulty level into level.txt
            f.write(level)                          # Write difficulty level into level.txt
        return redirect(url_for("dashboard"))      # Open dashboard page

    return render_template("scratchmedium.html")

@app.route("/scratchhard", methods=['GET', 'POST'])
def scratchhard():
    with open('static/level.txt', 'w') as f:        # Dis code to reset the level.txt file
        f.write("")                                 # Dis code to reset the level.txt file
    if request.method=="POST":                      # When user submit code
        level = "Hard"           # Get user input on Easy / Medium / Hard
        with open('static/level.txt', 'w') as f:    # Write difficulty level into level.txt
            f.write(level)                          # Write difficulty level into level.txt
        return redirect(url_for("dashboard"))      # Open dashboard page

    return render_template("scratchhard.html")

@app.route('/lessonplans', methods=['GET', 'POST'])
def setlessonplan():
    with open('static/level.txt', 'w') as f:        # Dis code to reset the level.txt file
        f.write("") 
    with open('./static/data.json') as json_data:
        lesson_data = json.load(json_data)
    if request.method == "POST":
        lessonplan = request.form["lp"]
        if lessonplan in lesson_data["lessonplana"]:
            return redirect(url_for("scratcheasy"))
            #return render_template("scratcheasy.html")
        elif lessonplan in lesson_data["lessonplanb"]:
            return redirect(url_for("scratchmedium"))
            #return render_template("scratchmedium.html")
        elif lessonplan in lesson_data["lessonplanc"]:
            return redirect(url_for("scratchhard"))   
            #return render_template("scratchhard.html")



@app.route("/dashboard/")
def dashboard():
    # level = carController.sendData()
    # return render_template("dashboard.html", level = level)
    level = carController.sendData()
    data2 = carController.receiveData(level)
    data = [level, data2[0], data2[1], data2[2], data2[3]]
    return render_template("dashboard.html", data = data)

@app.route("/dashboard2/")
def dashboard2():
    level = carController.sendData()
    data2 = carController.receiveData()
    data = [level, data2[0], data2[1], data2[2], data2[3]]
    return render_template("dashboard2.html", data = data)

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
