from ast import operator
from unittest import result
from db import db
class historymodel(db.Model):
    __tablename__='historiess'
    id = db.Column(db.Integer,primary_key=True)
    number1 = db.Column(db.Float(precision=2))
    number2 = db.Column(db.Float(precision=2))
    operatorr = db.Column(db.String(80))
    def json(self):
        return {'number1':self.number1,'number2':self.number2,'opertor':self.operatorr}
    def __init__(self,number1,number2,operatorr):
        self.number1=number1
        self.number2=number2
        self.operatorr = operatorr
    def save_his(self):
        db.session.add(self)
        db.session.commit()