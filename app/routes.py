from flask import render_template, request, redirect, flash
from app import app, db
from app.models import Task
from datetime import datetime  



@app.route("/", methods=["GET", "POST"])
def index():
    tasks = Task.query.all()

    if request.method == "GET":
        return render_template("index.html", tasks=tasks) 
    
    elif request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        due_date_str = request.form["due_date"]  
        priority = request.form["priority"]
        status = request.form["status"]

        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')

        task = Task(title=title, description=description, due_date=due_date, priority=priority, status=status)

        db.session.add(task)
        db.session.commit()

        flash('Task successfully added.', 'success')  # Mensagem de flash para adição de tarefa
        return redirect("/")  # Redireciona para a página inicial

    else:
        flash('Error adding a new task.', 'error')  # Mensagem de flash para erro
        return redirect("/")
    

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    flash('Task successfully deleted.', 'success')  # Mensagem de flash para exclusão de tarefa
    return redirect("/") 



