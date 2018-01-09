import sys
from flask import jsonify
from dao.resourcesDAO import ResourceDAO



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
        result['qty'] = row[5]
        result['city'] = row[6]
        return result

    def build_resource_requested(self,row):
        result = {}
        result['name'] = row[0]
        result['category'] = row[1]
        result['accountID'] = row[2]
        result['description'] = row[3]        
        result['qty'] = row[4]
        result['Requested_Date'] = row[5]
        result['city'] = row[6]
        return result

    def build_resource_avaliable(self,row):
        result = {}
        result['name'] = row[0]
        result['category'] = row[1]
        result['accountID'] = row[2]
        result['price'] = row[3]
        result['description'] = row[4]
        result['avaliability'] = row[5]
        result['qty'] = row[6]
        result['dateAdded'] = row[7]
        result['lastUpdate'] = row[8]  
        result['city'] = row[9] 
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
        rid = args.get("rid")  
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
        elif (len(args) == 1) and rid:
            res = dao.getAllResourcesRequestedbyRID(rid)   
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
        sid = args.get("sid")  
        keywords = args.get("keywords")
        resID = args.get("resid")
        price = args.get("price")
        

        if (len(args) == 1) and description:
            res = dao.getResourcesAvaliablebyDescription(description)
        elif (len(args) == 1) and resID:
            res = dao.getResourcesAvaliablebyresID(resID)
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
        elif (len(args) == 1) and sid:
            res = dao.getAllResourcesAvaliablebySID(sid)   
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
            return jsonify(Resources = "No Resources Found with that input. Try Again Later")   
        for row in res:
            result = self.build_resource_avaliable(row)
            result_list.append(result)          
        result_list = sorted(result_list, key=lambda k: k['name'])
        return jsonify(Resources = result_list)
        

    