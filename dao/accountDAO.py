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
        with open('JsonMakers/requester.json') as data_file:    
            return json.load(data_file)

    def getSuppliersbyCity(self,city):
        with open('JsonMakers/requester.json') as data_file: 
            data = json.load(data_file)
            res = []
            for supplier in data:
                if( city.lower() in supplier['city'].lower()):
                    res.append(supplier)
            if(len(res)==0):
                return "There are no supplier in that City"
            return res

    def getRequester(self):
        with open('JsonMakers/suppliers.json') as data_file:    
            return json.load(data_file)

    def getRequesterByCity(self,city):
        with open('JsonMakers/suppliers.json') as data_file: 
            data = json.load(data_file)
            res = []
            for supplier in data:
                if( city.lower() in supplier['city'].lower()):
                    res.append(supplier)
            if len(res)==0:
                return "There are no supplier in that City"
            return res