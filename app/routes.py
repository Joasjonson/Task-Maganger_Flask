from flask import render_template, redirect, flash
from app import app, db
from app.models import Task 
from app.form import TaskForm
from datetime import datetime



@app.route("/", methods=["GET", "POST"])
def index():
    tasks = Task.query.order_by(Task.due_date).all()
    form = TaskForm()

    
    today = datetime.now().date()
    tasks_due_today = [task for task in tasks if task.due_date.date() == today]

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        due_date = form.due_date.data
        priority = form.priority.data
        status = form.status.data

        task = Task(title=title, description=description, due_date=due_date, priority=priority, status=status)

        db.session.add(task)
        db.session.commit()

        flash('Task successfully added.', 'success') 
        return redirect("/") 

    return render_template("index.html", tasks=tasks, form=form, tasks_due_today=tasks_due_today)


    
    
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    flash('Task successfully deleted.', 'success')  
    return redirect("/") 



@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Task.query.get_or_404(id)
    form = TaskForm(obj=task)

    if form.validate_on_submit():
        form.populate_obj(task)

        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect("/")  

    return render_template("update.html", form=form, task=task)