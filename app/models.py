from app import db
from sqlalchemy import Enum
from sqlalchemy import event
from datetime import datetime

class Task(db.Model):
    __tablename__ = "tasks" 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    priority = db.Column(Enum('high', 'medium', 'low', name='priority_enum'), nullable=False)
    status = db.Column(Enum('pending','in_progress', 'completed', name='status_enum'), nullable=False)  # Corrigido removendo espaço antes de 'in progress'

    def __init__(self, title, description, due_date, priority, status ):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
