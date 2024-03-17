from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
 

    def __repr__(self):
        return "Task %r" % self.id


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        task_content = request.form["content"]
        new_task = Task(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        
        except:
            return " There was an issue adding your task ."
        
    else:
        tasks = Task.query.order_by(Task.id).all()
        return render_template("index.html", tasks=tasks)
    

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    
    except:
        return " There was a problem deleting that task. "
    

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Task.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["content"]

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was any problem update your task."
        
    else:
        return render_template("update.html", task=task)
    
    

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)



