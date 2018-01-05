import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config




class ResourceDAO:
    def __init__(self):
      #self.conn =  psycopg2.connect(user='natalia', password='none',
       #                 host='/cloudsql/project-9-20-187720:us-east1:project-9-20 ')
                         
        self.conn = psycopg2.connect(database='project920', user='natalia', password='none', sslmode='disable',hostaddr='35.196.249.53')
        # sslmode=disable dbname=project920  user=natalia hostaddr=35.196.249.53"

    def loadRequested(self):
        with open('JsonMakers/resources_requested_data.json') as data_file:    
            return json.load(data_file)

    def loadAvaliable(self):
        with open('JsonMakers/resources_avaliable_data.json') as data_file:    
            return json.load(data_file)
       
    def getAllResourcesRequested(self):
        #return self.loadRequested()
        cursor = self.conn.cursor()
        query = "select * from test;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result       

    def getAllResourcesAvaliable(self):
        return self.loadAvaliable()
    
   
    def getAllResources(self):
        a = self.loadAvaliable()
        b = self.loadRequested()      
        return a+b

    def getResourcesbyDescription(self,keywords):
        result = []
        temp = self.getAllResources()
        for resource in temp:           
            if(keywords.lower() in resource['description'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that description, Please Try Again Later"
        return sorted(result, key=lambda k: k['name'])

    def getResourcesbyName(self,keywords):
        result = []
        temp = self.getAllResources()
        for resource in temp:           
            if(keywords.lower() in resource['name'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that name, Please Try Again Later"
        return sorted(result, key=lambda k: k['name'])

    def getResourcesbyName_Description(self,name,description):
        result = []
        temp = self.getAllResources()
        for resource in temp:           
            if(name.lower() in resource['name'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that name, Please Try Again Later"
        else:
            temp=[]
            for resource in result:           
                if(description.lower() in resource['description'].lower()):
                    temp.append(resource)
        return sorted(temp, key=lambda k: k['name'])

           

    def getResourcesRequestedbyDescription(self,keywords):
        result = []
        temp = self.loadRequested()
        for resource in temp:           
            if(keywords.lower() in resource['description'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that description, Please Try Again Later"
        return sorted(result, key=lambda k: k['name'])

    def getResourcesRequestedbyName(self,keywords):
        result = []
        temp = self.loadRequested()
        for resource in temp:           
            if(keywords.lower() in resource['name'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that name, Please Try Again Later"
        return sorted(result, key=lambda k: k['name'])

    def getResourcesRequestedbyName_Description(self,name,description):
        result = []
        temp = self.loadRequested()
        for resource in temp:           
            if(name.lower() in resource['name'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that name, Please Try Again Later"
        else:
            temp=[]
            for resource in result:           
                if(description.lower() in resource['description'].lower()):
                    temp.append(resource)
        return sorted(temp, key=lambda k: k['name'])

        

    def getResourcesAvaliablebyDescription(self,keywords):
        result = []
        temp = self.loadAvaliable()
        for resource in temp:           
            if(keywords.lower() in resource['description'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that description, Please Try Again Later"
        return sorted(result, key=lambda k: k['name'])

    def getResourcesAvaliablebyName(self,keywords):
        result = []
        temp = self.loadAvaliable()
        for resource in temp:           
            if(keywords.lower() in resource['name'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that description, Please Try Again Later"
        return sorted(result, key=lambda k: k['name'])


    def getResourcesAvaliablebyName_Description(self,name,description):
        result = []
        temp = self.loadAvaliable()
        for resource in temp:           
            if(name.lower() in resource['name'].lower()):
                result.append(resource)        
        if(len(result)==0):
            return "No Resource with that name, Please Try Again Later"
        else:
            temp=[]
            for resource in result:           
                if(description.lower() in resource['description'].lower()):
                    temp.append(resource)
        return sorted(temp, key=lambda k: k['name'])

    def getResourcesbyRegion(self, region):
        pass

    def getResourcesbyCity(self, city):
        pass

    def getResourcesbyRegion_Name(self, region,name):
        pass

    def getResourcesbyRegion_Description(self, region,description):
        pass

    

      
