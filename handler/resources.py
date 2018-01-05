from dao.resourcesDAO import ResourceDAO
from flask import jsonify


class ResourcesHandler:
    def __init__(self):
        pass
               
    def build_resource(self,row):
        result = {}
        result['name'] = row[0]
        result['category'] = row[1]
        result['accountID'] = row[2]
        result['description'] = row[3]
        result['class'] = row[4]
        return result

    def build_resource_requested(self,row):
        result = {}
        result['name'] = row[0]
        result['category'] = row[1]
        result['accountID'] = row[2]
        result['description'] = row[3]        
        result['qty'] = row[5]
        result['Requested_time'] = row[6]
        return result

    def build_resource_avaliable(self,row):
        result = {}
        result['name'] = row[0]
        result['category'] = row[1]
        result['accountID'] = row[2]
        result['price'] = row[3]
        result['description'] = row[4]
        result['avalaible'] = row[5]
        result['qty'] = row[6]
        result['date_added'] = row[7]
        result['lastU'] = row[5]
        
        
        return result
       

    def getAllresources(self):
        dao = ResourceDAO()
        res = dao.getAllResources()
        return jsonify(Resource = res)

    def getFindAllresources(self, args):
        dao = ResourceDAO()
        description = args.get("description")
        qty = args.get("qty")
        name = args.get("name")
        price = args.get("price")
        avaliability = args.get("avaliability")
        city = args.get("city")
        region = args.get("region")
                     
        if (len(args) == 1) and description:
            res = dao.getResourcesbyDescription(description)
        elif (len(args) == 1) and name:
            res = dao.getResourcesbyName(name)
        elif (len(args)==2) and name and description:
            res = dao.getResourcesbyName_Description(name,description)
        elif (len(args)==1) and region:
            res = dao.getResourcesbyRegion(region)
        elif (len(args)==1) and city:
            res = dao.getResourcesbyCity(city)            
        elif (len(args)==2) and region and name:
            res = dao.getResourcesbyRegion_Name(region,name)
        elif (len(args)==2) and region and description:
            res = dao.getResourcesbyRegion_Description(region,description)  
        elif (len(args)==2) and city and name:
            res = dao.getResourcesbyCity_Name(city,name)
        elif (len(args)==2) and city and description:
            res = dao.getResourcesbyCity_Description(city,description)            
        elif qty or price or avaliability:
            res = dao.getAllResources()
        else:
             return jsonify(Error = "Malformed query string"), 400

        result_list = []
        if (len(res)==0):
            return jsonify(Resourcs = "No Resources Found with that input. Try Again Later")
        for row in res:
            result = self.build_resource(row)
            result_list.append(result)  
        sorted(result_list, key=lambda k: k['name'])
        return jsonify(Resources = result_list)


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
        city = args.get("city")
        region = args.get("region")
        rid = args.get("rid")
        region = args.get("region")

        if (len(args) == 1) and description:
            res = dao.getResourcesRequestedbyDescription(description)
        elif (len(args) == 1) and name:
            res = dao.getResourcesRequestedbyName(name)
        elif (len(args)==2) and name and description:
            res = dao.getResourcesRequestedbyName_Description(name,description)
        elif (len(args)==1) and region:
            res = dao.getResourcesRequestedbyRegion(region)
        elif (len(args)==1) and city:
            res = dao.getResourcesRequestedbyCity(city)            
        elif (len(args)==2) and region and name:
            res = dao.getResourcesRequestedbyRegion_Name(region,name)
        elif (len(args)==2) and region and description:
            res = dao.getResourcesRequestedbyRegion_Description(region,description)  
        elif (len(args)==2) and city and name:
            res = dao.getResourcesRequestedbyCity_Name(city,name)
        elif (len(args)==2) and city and description:
            res = dao.getResourcesRequestedbyCity_Description(city,description)     
        elif (len(args) == 1) and rid:
            res = dao.getAllResourcesRequestedbyRequested(rid)   
        elif qty or price or avaliability:
           res = dao.getAllResourcesRequested()
        else:
             return jsonify(Error = "Malformed query string"), 400
       

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


    