from dao.requesterDAO import RequesterDAO
from flask import jsonify

class RequesterHandler:
    
    def __init__(self):
            pass
    
    def build_requester(self,row):
        result = {}
        result['requester_id'] = row[0]
        result['first_name'] = row[1]
        result['list_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['city'] = row[5]
        return result

    def getAllRequesters(self):
        dao = RequesterDAO()
        res = dao.getAllRequester()
        result_list = []
        
        if len(res) == 0:
            return jsonify(Error = "No Requesters found"), 404
        else:
            for row in res:
                result = self.build_requester(row)
                result_list.append(result)            
            return jsonify(Requester = result_list)
    
    def searchAllRequestersByParameter(self, args):
        dao = RequesterDAO()
        city = args.get('city')
        region = args.get('region')
        resource_name = args.get('resource_name')
        type_name = args.get('type_name')
        name = args.get('name')
        keyword = args.get('keyword')
        if len(args) == 1 and city:
            res = dao.searchRequestersByCity(city)
        elif len(args) == 1 and region:
            res = dao.searchRequestersByRegion(region)
        elif len(args) == 1 and resource_name:
            res = dao.searchRequestersRequestingResource(resource_name)
        elif len(args) == 1 and type_name:
            res = dao.searchRequestersRequestingResourceByCategory(type_name)
        elif len(args) == 1 and name:
            res = dao.searchRequestersByName(name)
        elif len(args) == 1 and keyword:
            res = dao.searchRequestersByResourceKeyword(keyword)
        elif len(args) == 2 and resource_name and city:
            res = dao.searchRequestersRequestingResourcesInCity(resource_name, city)
        else:
            return jsonify(Error = "Malformed query string"), 400

        if len(res) == 0:
            return jsonify(Error = "No Requesters found"), 404
        else:
            result_list = []
            for row in res:
                result = self.build_requester(row)
                result_list.append(result)            
            return jsonify(Requester = result_list)

    def getRequesterByID(self,id):
        dao = RequesterDAO()
        row = dao.searchRequesterByID(id)
        if not row:
            return jsonify(Error = "Requester Not Found"), 404
        else:
            part = self.build_requester(row)
            return jsonify(Requester = part)