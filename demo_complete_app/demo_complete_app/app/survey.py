import json

from flask import render_template, request, redirect, url_for, Flask

from questions import questions
from proccess_data import proccess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/survey")
def survey():
    return render_template("survey.html", questions=enumerate(questions))


@app.route("/result", methods=["POST"])
def result():
    answers_json = request.form.get("answers")
    answers = json.loads(answers_json)
    answers = [int(answers[key]) for key in answers]

    # If all questions have been answered, calculate the sum and display the results
    if len(answers) == len(questions):
        result = proccess(answers)
        answers = []  # Clear the answers list
        return render_template("result.html", result=result)

    # If there are more questions to answer, redirect to the next question
    return redirect(url_for("survey"))

@app.route("/result", methods=["GET"])
def result_without_data():
    return render_template("result_no_data.html")


if __name__ == "__main__":
    app.run(debug=True)
