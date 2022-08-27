
from flask_restful import  reqparse,request

from models.calculator import calculatemodel
from flask_restful import reqparse,request,Resource
from models.calculator import  calculatemodel
from models.history import historymodel
class calculate(Resource):
       parser = reqparse.RequestParser()
       parser.add_argument('number1',type=float,
       required=True,
       help="you need a number to add" )
       parser.add_argument('number2',type=float,
       required=True,
       help="you need a number to add" )
       parser.add_argument('operatorr',type=str,
       required=True,
       help="you need a number to add" )
       def post (self):
              data = calculate.parser.parse_args()
              operatorr=data['operatorr']
              number1 = data['number1']
              number2 = data['number2']
              hist =historymodel(data['number1'],data['number2'],data['operatorr'])
              hist.save_his()
              if operatorr == '+':
                     result = calculatemodel.add(number1,number2)
                     return result
              elif operatorr == '*':
                     result = calculatemodel.multiply(number1,number2)
                     return result
              elif operatorr == '-':
                     result = calculatemodel.subtract(number1,number2)
                     return result
              elif operatorr == '/':
                     result = calculatemodel.divide(number1,number2)
                     return result
              else :
                      return {'message':'you have to hav an operatror'}
              

       



