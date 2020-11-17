from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/") # go to slash route, default route
def index(): # call this func
    return render_template("index.html")

@app.route("/hello")
def bye():
    name = request.args.get("name")
    if not name:
        return render_template("failure.html")
    return render_template("hello.html", name = name)