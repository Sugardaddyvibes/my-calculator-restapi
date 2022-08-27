import json
from unittest import result
from flask_restful import  reqparse,request

class calculatemodel():
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def add(number1,number2):
        return number1 + number2
    def subtract(number1,number2,):
        return number1 -  number2
    def multiply(number1,number2):
        return number1 * number2
    def divide(number1,number2):
        return  number1 / number2


