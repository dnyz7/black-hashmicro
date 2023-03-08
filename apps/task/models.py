from apps import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('Users.id'))
    task_title = db.Column(db.String(64) ,nullable=False ,unique=False)
    task_info = db.Column(db.String(256) ,nullable=False,unique=False)
    # 0 = on Doing || 1 = Done! 
    status = db.Column(db.Integer ,default = 0)
    date = db.Column(db.DateTime ,default=datetime.now())