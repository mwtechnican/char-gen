from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Worldsfeef!</p>"

@app.route("/generate")
def function():
    return "<p>Hello, generate!</p>"
