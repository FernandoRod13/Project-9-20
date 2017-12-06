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

    def getSeachAllresources(self, args):
        dao = ResourceDAO()
        description = args.get("description")
        qty = args.get("qty")
        name = args.get("name")
        price = args.get("price")
        avaliability = args.get("avaliability")
        if (len(args) == 1) and description:
            res = dao.getResourcesbyDescription(description)
        elif (len(args) == 1) and name:
            res = dao.getResourcesbyName(name)
        elif (len(args)==2) and name and description:
            res = dao.getResourcesbyName_Description(name,description)
        elif qty or price or avaliability:
            res = dao.getAllResources()
        else:
            res = ("Malformed query string"), 400
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
        elif (len(args)==2) and name and description:
            res = dao.getResourcesRequestedbyName_Description(name,description)
        elif qty or price or avaliability:
            res = dao.getAllResourcesAvaliable()
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
            res = dao.getAllResourcesRequested()
        else:
            res =  "Malformed query string", 400
        return jsonify(Resource = res)    

    def getAvailbaleResourcesByKeyword(self, args):
        return self.getAllresources_avaliable()

    def getRequestedResourcesByKeyword(self, args):
        return self.getAllresources_requested()
    

    