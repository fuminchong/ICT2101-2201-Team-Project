from flask import Flask, render_template
from werkzeug.datastructures import RequestCacheControl

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('lessonplans.html')

@app.route('/lessonplan', methods=['GET', 'POST'])
def setlessonplan():
    with open('./static/data.json') as json_data:
        lesson_data = json.load(json_data)
    if request.method == 'POST':
        lessonplan = request.form["lp"]
        if lessonplan in lesson_data["lessonplanA"]:
            return redirect(url_for("lessonplanA"))
        elif lessonplan in lesson_data["lessonplanB"]:
            return redirect(url_for("lessonplanB"))
        elif lessonplan in lesson_data["lessonplanC"]:
            return redirect(url_for("lessonplanC"))        

if __name__ == '__main__':
    app.run(debug=True)