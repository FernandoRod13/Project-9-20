import sys
from datetime import datetime
from flask import jsonify
from dao.resourcesDAO import ResourceDAO


class ResourcesHandler:
    def __init__(self):
        pass
               
    def build_resource(self,row):
        result = {}
        result['resource_id'] = row[0]
        result['name'] = row[1]
        result['category'] = row[2]
        result['accountID'] = row[3]
        result['description'] = row[4]
        result['class'] = row[5]
        result['qty'] = row[6]
        result['city'] = row[7]
        return result

    def build_resource_requested(self,row):
        result = {}
        result['resource_id'] = row[0]
        result['name'] = row[1]
        result['category'] = row[2]
        result['accountID'] = row[3]
        result['description'] = row[4]        
        result['qty'] = row[5]
        result['Requested_Date'] = row[6]
        result['city'] = row[7]
        return result

    def build_resource_avaliable(self,row):
        result = {}
        result['resource_id'] = row[0]
        result['name'] = row[1]
        result['category'] = row[2]
        result['accountID'] = row[3]
        result['price'] = row[4]
        result['description'] = row[5]
        result['avaliability'] = row[6]
        result['qty'] = row[7]
        result['dateAdded'] = row[8]
        result['lastUpdate'] = row[9]  
        result['city'] = row[10] 
        return result

    def build_supplier(self,row):
        result = {}
        result['supplier_id'] = row[0]
        result['first_name'] = row[1]
        result['list_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['city'] = row[5]
        return result

    def build_resoucesRequested_attributes(self, request_id, name, resource_type, requester_id, description, qty,dt):
        result = {}
        result['request_id'] = request_id
        result['name'] = name
        result['category_number'] = resource_type
        result['accountID'] = requester_id
        result['description'] = description        
        result['qty'] = qty
        result['Requested_Date'] =dt
        return result  
       

    def getAllresources(self):
        dao = ResourceDAO()
        res = dao.getAllResources()
        result_list = []
        if (len(res)==0):
            return jsonify(Resources = "No Resources Found with that input. Try Again Later")
        for row in res:
            result = self.build_resource(row)
            result_list.append(result)            
        result_list = sorted(result_list, key=lambda k: k['name'])
        return jsonify(Resources = result_list)
      
    def getFindAllresources(self, args):
        dao = ResourceDAO()
        description = args.get("description")
        qty = args.get("qty")
        name = args.get("name")
        price = args.get("price")
        avaliability = args.get("avaliability")
        city = args.get("city")
        region = args.get("region")
        keywords = args.get("keywords")
        aid = args.get('aid')                  
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
        elif (len(args) == 1) and keywords:
            res = dao.getResourcesbyKeywords(keywords)  
        elif (len(args) == 2) and keywords and city:
            res = dao.getAllResourcesbyKeywords_City(keywords,city)  
        elif (len(args) == 2) and keywords and region:
            res = dao.getAllResourcesbyKeywords_Region(keywords,region)   
        elif (len(args) == 1) and qty:
            res = dao.getAllResourcesbyQty(qty)  
        elif (len(args) == 2) and qty and city:
            res = dao.getAllResourcesbyQty_City(qty,city)
        elif (len(args) == 2) and qty and region:
            res = dao.getAllResourcesbyQty_Region(qty,region)
        elif (len(args) == 2) and qty and keywords:
            res = dao.getAllResourcesbyQty_Keywords(qty,keywords)
        elif (len(args) == 2) and qty and name:
            res = dao.getAllResourcesbyQty_Name(qty,name)
        elif (len(args) ==1) and aid:
            res = dao.getAllResourcesbyAid(aid)
        elif price or avaliability :
            return jsonify(Error = "Price and Avaliablity can be only be use with Resources Avaliable") 
        else:
            return jsonify(Error = "Malformed query string"), 400

        result_list = []
        if (len(res)==0):
            return jsonify(Resources = "No Resources Found with that input. Try Again Later")
        for row in res:
            result = self.build_resource(row)
            result_list.append(result)  
          
        result_list = sorted(result_list, key=lambda k: k['name'])
        return jsonify(Resources = res)

    def getResourceRequestedByID(self,rid):
        dao = ResourceDAO()
        res = dao.getResourceRequestedByRID(rid)
        if (len(res)==0):
            return jsonify(Error = "No Resources Found with that input."), 404  
        result_list = [] 
        for row in res:
            result = self.build_resource_requested(row)
            result_list.append(result)          
        return jsonify(Resources = result_list)


    def getAllresources_requested(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesRequested()
        if (len(res)==0):
            return jsonify(Resources = "No Resources Found with that input. Try Again Later")
        result_list = []       
        for row in res:
           result = self.build_resource_requested(row)
           result_list.append(result)  
        result_list = sorted(result_list, key=lambda k: k['name'])         
        return jsonify(Resources = result_list)

    def getAllresources_avaliable(self):
        dao = ResourceDAO()
        res = dao.getAllResourcesAvaliable()
        if (len(res)==0):
            return jsonify(Resources = "No Resources Found with that input. Try Again Later")
        result_list = []       
        for row in res:
            result = self.build_resource_avaliable(row)
            result_list.append(result)  
        result_list = result_list = sorted(result_list, key=lambda k: k['name'])
        return jsonify(Resources = result_list)
        

    def getresources_requested(self,args):
        dao = ResourceDAO()
        description = args.get("description")
        qty = args.get("qty")
        name = args.get("name")          
        city = args.get("city")
        region = args.get("region") 
        keywords = args.get("keywords") 
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
        elif (len(args) == 1) and keywords:
            res = dao.getAllResourcesRequestedbyKeywords(keywords)  
        elif (len(args) == 2) and keywords and city:
            res = dao.getAllResourcesRequestedbyKeywords_City(keywords,city)  
        elif (len(args) == 2) and keywords and region:
            res = dao.getAllResourcesRequestedbyKeywords_Region(keywords,region)  
        elif (len(args) == 1) and qty:
            res = dao.getAllResourcesRequestedbyQty(qty)  
        elif (len(args) == 2) and qty and city:
            res = dao.getAllResourcesRequestedbyQty_City(qty,city)
        elif (len(args) == 2) and qty and region:
            res = dao.getAllResourcesRequestedbyQty_Region(qty,region)
        elif (len(args) == 2) and qty and keywords:
            res = dao.getAllResourcesRequestedbyQty_Keywords(qty,keywords)
        elif (len(args) == 2) and qty and name:
            res = dao.getAllResourcesRequestedbyQty_Name(qty,name)
        else:
             return jsonify(Error = "Malformed query string"), 400
        result_list = []    
        if (len(res)==0):
            return jsonify(Resources = "No Resources Found with that input. Try Again Later")   
        for row in res:
            result = self.build_resource_requested(row)
            result_list.append(result)  
        result_list = sorted(result_list, key=lambda k: k['name'])
        return jsonify(Resources = result_list) 
       

    def getresources_avaliable(self,args):
        dao = ResourceDAO()
        description = args.get("description")
        qty = args.get("qty")
        name = args.get("name")          
        city = args.get("city")
        region = args.get("region")  
        keywords = args.get("keywords")
        price = args.get("price")
        

        if (len(args) == 1) and description:
            res = dao.getResourcesAvaliablebyDescription(description)
        elif (len(args) == 1) and name:
            res = dao.getResourcesAvaliablebyName(name)
        elif (len(args)==2) and name and description:
            res = dao.getResourcesAvaliablebyName_Description(name,description)
        elif (len(args)==1) and region:
            res = dao.getResourcesAvaliablebyRegion(region)
        elif (len(args)==1) and city:
            res = dao.getResourcesAvaliablebyCity(city)            
        elif (len(args)==2) and region and name:
            res = dao.getResourcesAvaliablebyRegion_Name(region,name)
        elif (len(args)==2) and region and description:
            res = dao.getResourcesAvaliabledbyRegion_Description(region,description)  
        elif (len(args)==2) and city and name:
            res = dao.getResourcesAvaliablebyCity_Name(city,name)
        elif (len(args)==2) and city and description:
            res = dao.getResourcesAvaliablebyCity_Description(city,description)   
        elif (len(args) == 1) and keywords:
            res = dao.getAllResourcesAvaliablebyKeywords(keywords)  
        elif (len(args) == 2) and keywords and city:
            res = dao.getAllResourcesAvaliablebyKeywords_City(keywords,city)  
        elif (len(args) == 2) and keywords and region:
            res = dao.getAllResourcesAvaliablebyKeywords_Region(keywords,region)    
        elif (len(args) == 1) and qty:
            res = dao.getAllResourcesAvaliablebyQty(qty)  
        elif (len(args) == 2) and qty and city:
            res = dao.getAllResourcesAvaliablebyQty_City(qty,city)
        elif (len(args) == 2) and qty and region:
            res = dao.getAllResourcesAvaliablebyQty_Region(qty,region)
        elif (len(args) == 2) and qty and keywords:
            res = dao.getAllResourcesAvaliablebyQty_Keywords(qty,keywords)
        elif (len(args) == 2) and qty and name:
            res = dao.getAllResourcesAvaliablebyQty_Name(qty,name)
        elif (len(args) == 1) and price:
            res = dao.getAllResourcesAvaliablebyPrice(price)  
        elif (len(args) == 2) and price and city:
            res = dao.getAllResourcesAvaliablebyPrice_City(price,city)
        elif (len(args) == 2) and price and region:
            res = dao.getAllResourcesAvaliablebyPrice_Region(price,region)
        elif (len(args) == 2) and price and keywords:
            res = dao.getAllResourcesAvaliablebyPrice_Keywords(price,keywords)
        elif (len(args) == 2) and price and name:
            res = dao.getAllResourcesAvaliablebyPrice_Name(price,name)
        else:
             return jsonify(Error = "Malformed query string"), 400        
        
        result_list = []    
        if (len(res)==0):
            return jsonify(Error = "No Resources Found with that input."), 404   
        for row in res:
            result = self.build_resource_avaliable(row)
            result_list.append(result)          
        result_list = sorted(result_list, key=lambda k: k['name'])
        return jsonify(Resources = result_list)

    def getResourceAvaliableByRID(self,rid):
        dao = ResourceDAO()
        res = dao.getResourceAvaliableByRID(rid)
        if (len(res)==0):
            return jsonify(Error = "No Resources Found with that input."), 404  
        result_list = [] 
        for row in res:
            result = self.build_resource_avaliable(row)
            result_list.append(result)          
        return jsonify(Resources = result_list)

    def getSuppliersForAvailableResourceByRID(self, rid):
        dao = ResourceDAO()
        res = dao.getSupplierOfResourceAvaliablebyRID(rid)
        
        if (len(res)==0):
            return jsonify(Error = "No Resources Found with that input."), 404 
        result_list = []  
        for row in res:
            result = self.build_supplier(row)
            result_list.append(result)          
        return jsonify(Supplier = result_list)



#########################################################
####  PUT
#########################################################

def insertResourcesRequested(self, form):
    if len(form) != 5:
        return jsonify(Error = "Malformed post request"), 400
    else:
        name = form['name']
        resource_type = form['resource_type']
        requester_id = form['requester_id']
        qty = form['qty']
        description = form['description']
        dt = datetime.now()
        if name and resource_type and requester_id and qty and description:
            dao = ResourceDAO()
            pid = dao.insertRequested(name, resource_type, requester_id,description, qty,dt)
            result = self.build_resoucesRequested_attributes(pid, name, resource_type, requester_id, qty,dt)
            return jsonify(Resource=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
    

def insertResourcesAvailable(self, form):
    if len(form) != 6:
        return jsonify(Error = "Malformed post request"), 400
    else:
        name = form['name']
        resource_type = form['resource_type']
        supplier_id = form['supplier_id']
        price = form['price']
        description = form['description']
        qty = form['qty']
        availability = form['qty']
        dt = datetime.now()
        if name and resource_type and supplier_id and qty and price and description and qty and availability:
            dao = ResourceDAO()
            pid = dao.insertAvailable(name,resource_type,supplier_id,qty,price,description,qty,availability,dt)
            result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
    

#########################################################
####  UPDATE
#########################################################

def updateResourcesRequested(self, form):
    if len(form) != 4:
        return jsonify(Error = "Malformed post request"), 400
    else:
        name = form['name']
        resource_type = form['resource_type']
        requester_id = form['requester_id']
        description = form['description']
        qty = form['qty']
        if name and resource_type and requester_id and qty and description:
            dao = ResourceDAO()
            pid = dao.updateRequested(name, resource_type, requester_id, description, qty)
            result = self.build_part_attributes(pid, name, resource_type, requester_id, description, qtye)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
 

def updateResourcesAvailable(self, form):
    if len(form) != 4:
        return jsonify(Error = "Malformed post request"), 400
    else:
        name = form['name']
        resource_type = form['resource_type']
        supplier_id = form['supplier_id']
        price = form['price']
        description = form['description']
        qty = form['qty']
        availability = form['qty']
        if name and resource_type and supplier_id and qty and price and description and qty and availability:
            dao = ResourceDAO()
            pid = dao.updateAvailable(name,resource_type,supplier_id,qty,price,description,qty,availability)
            result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400