from flask import jsonify
import json



class ResourceDAO:
    resources_requested = []

    def loadRequested(self):
        with open('JsonMakers/note_data.json') as data_file:    
            return json.load(data_file)
       
    def getAllResourcesRequested(self):
       #sreturn 'Resquested'
        return self.loadRequested();
         #resources_requested

    def getAllResourcesAvaliable(self):
        return 'Avaliable'
    #   return  jsonify(resource) for resource in resources_requested

    