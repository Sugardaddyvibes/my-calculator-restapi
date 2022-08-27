
from flask import Flask
from resources.clculator import calculate
from flask_restful import Resource,Api
from resources.history import calculatehistory
app = Flask(__name__)
api =Api(app)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
@app.before_first_request
def creates_table():
    db.create_all()



api.add_resource(calculate,'/calculat')
api.add_resource(calculatehistory,'/history')
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=500,debug =True)