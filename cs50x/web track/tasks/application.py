from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def tasks():
    if "todos" not in session: # session is a dict
        session["todos"] = [] # instead of a global variable, use a session for individuals
    return render_template("tasks.html", todos=session["todos"])

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task") # add.html里的task
        session["todos"].append(todo)
        return redirect("/")