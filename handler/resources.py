from flask import jsonify
from dao.resourcesDAO import rDAO

resources_requested = []


class ResourcesHandler:
    def __init__(self):
        pass
    
    def build_resource(self,name,description):
        new_resource = {
            'name': name,
            'description' : description 
        }
        return new_resource

    def getAllresources_requested():
        return rDAO.getAllResourcesRequested()

    def getAllresources_requested():
        return rDAO.getAllResourcesAvaliable()
   
        
