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

    def getAllresources_requested(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesRequested()
        return jsonify(Resource = res)
        

    def getAllresources_avaliable(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesRequested()
        return jsonify(Resource = res)
   
        
