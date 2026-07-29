from flask import Flask, render_template, request

app = Flask(__name__)


# Home Page (UI)
@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = num1 + num2
        else:
            result = num1 - num2

    return render_template("index.html", result=result)


# API Route for Addition
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)


# API Route for Subtraction
@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return str(a - b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)