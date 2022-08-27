from flask_restful import Resource
from models.history import historymodel
from resources.clculator import calculate
class calculatehistory(Resource):
    def get(self):
        return {'history':[hist.json() for hist in historymodel.query.all()]}