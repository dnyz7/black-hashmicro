from apps import db
from datetime import datetime

# class Test(db.Model):
#     __tablename__ = "tests"
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer,db.ForeignKey('Users.id'))
#     string1 = db.Column(db.String(64) ,nullable=False ,unique=False)
#     string2 = db.Column(db.String(256) ,nullable=False,unique=False)
#     timestamp = db.Column(db.DateTime ,default=datetime.now())