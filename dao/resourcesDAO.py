from flask import jsonify


resources_requested = []

class ResourcesDAO:
    def __init__(self):
        pass
       
    def getAllResourcesRequested(self):
       return 'Resquested'
     #  return  jsonify(resource) for resource in resources_requested

    def getAllResourcesAvaliable(self):
       return 'Avaliable'
    #   return  jsonify(resource) for resource in resources_requested

