import json

from flask import jsonify


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
        return self.loadRequested()
        

    def getAllResourcesAvaliable(self):
        return self.loadAvaliable()
    
   
    def getAllResources(self):
        a = self.loadAvaliable()
        b = self.loadRequested()      
        return a+b
           

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

    

    def getCategoryRequestedWater(self):
        return ' Water Category'
    #
    # ****************** DASHBOARD METHODS *********************
    #

    # DAILY STATISTICS
    def getAllDailyResInNeed(self):
        result = []
        result.append("Daily resources in need")
        return result
    
    def getAllDailyResAvailable(self):
        result = []
        result.append("Daily resources available")
        return result
    
    def getAllDailyResBetween(self):
        result = []
        result.append("Daily resources between")
        return result
    
    # TRENDING STATISTICS (7 DAY PERIOD)
    def getAllTrendingResInNeed(self):
        result = []
        result.append("Trending resources in need")
        return result
    
    def getAllTrendingResAvailable(self):
        result = []
        result.append("Trending resources available")
        return result
    
    def getAllTrendingResBetween(self):
        result = []
        result.append("Trending resources between")
        return result 
    
    # TRENDING STATICTICS (8 SENATES)
    def getAllTrendingResInNeedBySenate(self, keywords):
        result = []
        result.append("Trending resources by" + keywords + " in need")
        return result
    
    def getAllTrendingResAvailableBySenate(self, keywords):
        result = []
        result.append("Trending resources by" + keywords + " available")
        return result
    
    def getAllTrendingResBetweenBySenate(self, keywords):
        result = []
        result.append("Trending resources by" + keywords + " in between")
        return result
    
    # Account verification
    def verifyAccount(self, accountid, accountpass):
        result = []
        result.append("This is to verify if account " + accountid + "is correct")
        return result
    
