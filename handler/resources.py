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

    def getresources_avaliable(self,keywords):
        dao = ResourceDAO()
        res = dao.getResourcesAvaliable(keywords)
        return jsonify(Resource = res)

    def getresources_requested(self,keywords):
        dao = ResourceDAO()
        res = dao.getResourcesRequested(keywords)
        return jsonify(Resource = res)

    def WaterCategoryRequested(self):
        dao = ResourceDAO()
        res = dao.getCategoryRequestedWater()
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
    
    
    
   
        
