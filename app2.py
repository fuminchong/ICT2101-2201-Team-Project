from flask import Flask, request, json
from datetime import datetime
import re
from flask import render_template

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")

@app.route("/")
def home():
    with open('static/level.txt', 'w') as f:    # Dis code to reset the level.txt file
        f.write("")                             # Dis code to reset the level.txt file
    return render_template("home.html")



@app.route("/scratch/", methods=['GET', 'POST'])
def scratch():
    with open('static/level.txt', 'w') as f:        # Dis code to reset the level.txt file
        f.write("")                                 # Dis code to reset the level.txt file
    if request.method=="POST":                      # When user submit code
        level = request.form.get('level')           # Get user input on Easy / Medium / Hard
        with open('static/level.txt', 'w') as f:    # Write difficulty level into level.txt
            f.write(level)                          # Write difficulty level into level.txt
        return render_template("dashboard.html", level = level)     # Open dashboard page
    return render_template("scratch.html")



@app.route("/dashboard/")
def dashboard():
    with open('static/level.txt', 'r') as f:        # Open the level.txt file
        level = f.read()                            # Read the level.txt file
    return render_template("dashboard.html", level = level)     # dashboard.html need to add {{level}}


