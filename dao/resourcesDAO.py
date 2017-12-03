from flask import jsonify
import json



class ResourceDAO:
    def __init__(self):
        pass
        
    def loadRequested(self):
        with open('JsonMakers/resources_requested_data.json') as data_file:    
            return json.load(data_file)

    def loadAvaliable(self):
        with open('JsonMakers/resources_avaliable_data.json') as data_file:    
            return json.load(data_file)
       
    def getAllResourcesRequested(self):
        # cursor = self.conn.cursor()
        # query = "select * from parts;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result      
        return self.loadRequested()
        

    def getAllResourcesAvaliable(self):
        return self.loadAvaliable()
    
   
    def getAllResources(self):
        a = self.loadAvaliable()
        b = self.loadRequested()      
        return a+b
           

    def getResourcesRequested(self,keywords):
        result = []
        temp = self.loadRequested()
        for resource in temp:           
            if(keywords.lower() in resource['description'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that Keywords, Please Try Again Later"
        return sorted(result, key=lambda k: k['name'])
        

    def getResourcesAvaliable(self,keywords):
        result = []
        temp = self.loadAvaliable()
        for resource in temp:           
            if(keywords.lower() in resource['description'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that Keywords, Please Try Again Later"
        return sorted(result, key=lambda k: k['name'])

    def getCategoryRequestedWater(self):
        return ' Water Category'