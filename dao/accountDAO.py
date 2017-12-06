from flask import jsonify
import json

class accountDAO:
    
    def __init__(self):
        pass
    
      # Account verification
    def verifyAccount(self, accountid, accountpass):
        result = []
        result.append("This is to verify if account " + accountid + "is correct")
        return result
    
    def getSuppliers(self):
        with open('JsonMakers/suppliers.json') as data_file:    
            return json.load(data_file)
    