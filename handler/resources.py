from flask import jsonify
from dao.resourcesDAO import ResourceDAO

class ResourcesHandler:
    resources_requested = []
    
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
   
        
