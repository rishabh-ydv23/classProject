from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator App is Running!"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return str(a - b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)