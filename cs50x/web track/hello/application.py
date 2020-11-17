from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/") # go to slash route, default route
def index(): # call this func
    number = random.randint(0,1)
    return render_template("index.html", number = number)

@app.route("/goodbye")
def bye():
    return "goodbye!"