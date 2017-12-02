from flask import jsonify


class ResourceDAO:
    resources_requested = []
       
    def getAllResourcesRequested(self):
       return 'Resquested'
     #  return  jsonify(resource) for resource in resources_requested

    def getAllResourcesAvaliable(self):
       return 'Avaliable'
    #   return  jsonify(resource) for resource in resources_requested

