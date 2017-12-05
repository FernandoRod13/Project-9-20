from dao.resourcesDAO import ResourceDAO
from flask import jsonify


class ResourcesHandler:
    def __init__(self):
        pass
               
    def build_resource(self,name,description):
        new_resource = {
            'name': name,
            'description' : description 
        }
        return new_resource

    def getAllresources(self):
        dao = ResourceDAO()
        res = dao.getAllResources()
        return jsonify(Resource = res)

    def getAllresources_requested(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesRequested()
        return jsonify(Resource = res)

    def getAllresources_avaliable(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesAvaliable()
        return jsonify(Resource = res)
        

    def getresources_requested(self,args):
        dao = ResourceDAO()
        description = args.get("description")
        qty = args.get("qty")
        name = args.get("name")
        price = args.get("price")
        avaliability = args.get("avaliability")
        if (len(args) == 1) and description:
            res = dao.getResourcesRequestedbyDescription(description)
        elif (len(args) == 1) and name:
            res = dao.getResourcesRequestedbyName(name)
        elif qty or price or avaliability:
            res = "Result of search with that keyword"
        else:
            res = ("Malformed query string"), 400
        return jsonify(Resource = res)

    def getresources_avaliable(self,args):
        dao = ResourceDAO()
        description = args.get("description")
        qty = args.get("qty")
        name = args.get("name")
        price = args.get("price")
        avaliability = args.get("avaliability")
        if (len(args) == 1) and description:
            res = dao.getResourcesAvaliablebyDescription(description)
        elif (len(args) == 1) and name:
            res = dao.getResourcesAvaliablebyName(name)
        elif (len(args)==2) and name and description:
            res = dao.getResourcesAvaliablebyName_Description(name,description)
        elif qty or price or avaliability:
            res = "Result of search with that keyword"
        else:
            res = ("Malformed query string"), 400
        return jsonify(Resource = res)    

    

    


    

    
    #
    # ****************** DASHBOARD METHODS *********************
    #

    # DAILY STATISTICS
    def getAllDailyRes_InNeed(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesAvaliable()
        return jsonify(Resource = res)
    
    def getAllDailyRes_Available(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesAvaliable()
        return jsonify(Resource = res)
    
    def getAllDailyRes_Between(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesAvaliable()
        return jsonify(Resource = res)
    
    # TRENDING STATISTICS (7 DAY PERIOD)
    def getAllTrendingRes_InNeed(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesAvaliable()
        return jsonify(Resource = res)
    
    def getAllTrendingRes_Available(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesAvaliable()
        return jsonify(Resource = res)
    
    def getAllTrendingRes_Between(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesAvaliable()
        return jsonify(Resource = res)
    
    # TRENDING STATICTICS (8 SENATES)
    def getAllDailyRes_InNeedBySenate(self, keywords):
        dao = ResourceDAO()
        res = dao.getResourcesRequested(keywords)
        return jsonify(Resource = res)
    
    def getAllDailyRes_AvailableBySenate(self, keywords):
        dao = ResourceDAO()
        res = dao.getResourcesRequested(keywords)
        return jsonify(Resource = res)
    
    def getAllDailyRes_BetweenBySenate(self, keywords):
        dao = ResourceDAO()
        res = dao.getResourcesRequested(keywords)
        return jsonify(Resource = res)
    
    
    
   
        
