from flask import jsonify
import json



class ResourceDAO:
    resources_requested = []

    def loadRequested(self):
        with open('JsonMakers/note_data.json') as data_file:    
            return json.load(data_file)
       
    def getAllResourcesRequested(self):
        # cursor = self.conn.cursor()
        # query = "select * from parts;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
      
        return self.loadRequested();
        

    def getAllResourcesAvaliable(self):
        return 'Avaliable'
    #   return  jsonify(resource) for resource in resources_requested

    