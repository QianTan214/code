from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # relative path
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods = ["POST","GET"]) # 装饰器
def index():
    if request.method == "POST":
        task_content = request.form['content'] # create a new task from user input
        new_task = Todo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit() # commit to database
            return redirect("/")
        except:
            return "There is an issue adding your task"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # first() the most recent
        return render_template("index.html", tasks= tasks)



@app.route("/delete/<int:id>") # grab the id of the task we want to delete
def delete(id):
    task_to_delete = Todo.query.get_or_404(id) # query the database

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting that task"


@app.route("/update/<int:id>", methods=["POST", "GET"]) # grab the id of the task we want to update
def update(id):

    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["content"]

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue updating your task"

    else:
        return render_template("update.html", task = task)





if __name__ == "__main__":
    app.run(debug = True, port = 3000)