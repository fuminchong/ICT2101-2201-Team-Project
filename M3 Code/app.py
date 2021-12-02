from flask import Flask
from datetime import datetime
import re
from flask import render_template, request, redirect, url_for
import json

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
@app.route("/", methods=["POST", "GET"])
def home():
    
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
<<<<<<< Updated upstream

<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes

@app.route("/lessonplan", methods=["POST", "GET"])
=======
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
        return render_template("dashboard.html", level = level)     # Open dashboard page
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
        return render_template("dashboard.html", level = level)     # Open dashboard page

    return render_template("scratchmedium.html")

@app.route("/scratchhard", methods=['GET', 'POST'])
def scratchhard():
    with open('static/level.txt', 'w') as f:        # Dis code to reset the level.txt file
        f.write("")                                 # Dis code to reset the level.txt file
    if request.method=="POST":                      # When user submit code
        level = "Hard"           # Get user input on Easy / Medium / Hard
        with open('static/level.txt', 'w') as f:    # Write difficulty level into level.txt
            f.write(level)                          # Write difficulty level into level.txt
        return render_template("dashboard.html", level = level)     # Open dashboard page

    return render_template("scratchhard.html")

@app.route('/lessonplans', methods=['GET', 'POST'])
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
def setlessonplan():
    with open('./static/data.json') as json_data:
        lesson_data = json.load(json_data)
    if request.method == "POST":
        lessonplan = request.form["lp"]
<<<<<<< Updated upstream
<<<<<<< Updated upstream
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
=======
=======
>>>>>>> Stashed changes
        if lessonplan in lesson_data["lessonplana"]:
            return redirect(url_for("scratcheasy"))
            #return render_template("scratcheasy.html")
        elif lessonplan in lesson_data["lessonplanb"]:
            return redirect(url_for("scratchmedium"))
            #return render_template("scratchmedium.html")
        elif lessonplan in lesson_data["lessonplanc"]:
            return redirect(url_for("scratchhard"))   
            #return render_template("scratchhard.html")
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

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