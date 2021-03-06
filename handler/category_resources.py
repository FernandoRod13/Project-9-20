from flask import jsonify
from dao.category_resourcesDAO import category_ResourceDAO

class CategoryHandler: 


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
        result['requested_date'] = row[6]
        result['city'] = row[7]
        return result

    def build_resource_avaliable(self,row):
        result = {}
        result['resource_id'] = row[0]
        result['name'] = row[1]
        result['category'] = row[2]
        result['supplier_id'] = row[3]
        result['price'] = row[4]
        result['description'] = row[5]
        result['availability'] = row[6]
        result['dateAdded'] = row[7]
        result['lastUpdate'] = row[8]  
        result['city'] = row[9] 
        return result  

    def __init__(self):
        pass    

    def categories(self):
        dao = category_ResourceDAO()        
        res = dao.getCategories()        
        result_list = []        
        for row in res:
            result = self.build_resource(row)
            result_list.append(result)  
        return jsonify(Resources = result_list)
        

    def category(self,args):
        dao = category_ResourceDAO()
        category = args.get("cat")
        qty = args.get("qty")        
        city = args.get("city")
        region = args.get("region")
       
        if (len(args) == 1 ) and category:
            res = dao.getCategory(category) 
        elif (len(args) == 2 ) and category and qty:
            res = dao.getCategory_Qty(category,qty)
        elif (len(args) == 2 ) and category and city:
            res = dao.getCategory_City(category,city)                 
        elif (len(args) == 2 ) and category and region:
            res = dao.getCategory_Region(category,region)    
        else:
            return jsonify(Error = "Malformed query string"), 400       
        result_list = []        
        for row in res:
            result = self.build_resource(row)
            result_list.append(result)  
        sorted(result_list, key=lambda k: k['category'])
        return jsonify(Resources = result_list)
    
    def categoryRequested(self,args):
        dao = category_ResourceDAO() 
        category = args.get("cat")
        qty = args.get("qty")        
        city = args.get("city")
        region = args.get("region")
       
        if (len(args) == 1 ) and category:
            res = dao.getCategoryRequested(category) 
        elif (len(args) == 2 ) and category and qty:
            res = dao.getCategoryRequested_Qty(category,qty)         
        elif (len(args) == 2 ) and category and city:
            res = dao.getCategoryRequested_City(category,city)                 
        elif (len(args) == 2 ) and category and region:
            res = dao.getCategoryRequested_Region(category,region)                        
        else:
            return jsonify(Error = "Malformed query string"), 400      
        result_list = []        
        for row in res:
            result = self.build_resource_requested(row)
            result_list.append(result)  
        sorted(result_list, key=lambda k: k['category'])
        return jsonify(Resources = result_list)
    
    def categoriesRequested(self):
        dao = category_ResourceDAO()       
        res = dao.getCategoriesRequested()    
        result_list = []        
        for row in res:
            result = self.build_resource_requested(row)
            result_list.append(result)  
        sorted(result_list, key=lambda k: k['category'])
        return jsonify(Resources = result_list)    
    
     
    def categoryAvaliable(self,args):
        dao = category_ResourceDAO() 
        category = args.get("cat") 
        qty = args.get("qty")
        price = args.get("price")
        city = args.get("city")
        region = args.get("region")
       
        if (len(args) == 1 ) and category:
            res = dao.getCategoryAvaliable(category) 
        elif (len(args) == 2 ) and category and qty:
            res = dao.getCategoryAvaliable_Qty(category,qty)
        elif (len(args) == 2 ) and category and price:
            res = dao.getCategoryAvaliable_Price(category,price) 
        elif (len(args) == 2 ) and category and city:
            res = dao.getCategoryAvaliable_City(category,city)                 
        elif (len(args) == 2 ) and category and region:     
            res = dao.getCategoryAvaliable_Region(category, region)
        else:
            return jsonify(Error = "Malformed query string"), 400     
           
        result_list = []        
        for row in res:
            result = self.build_resource_avaliable(row)
            result_list.append(result)  
        sorted(result_list, key=lambda k: k['category'])
        return jsonify(Resources = result_list)   
    
    def categoriesAvaliable(self):
        dao = category_ResourceDAO()       
        res = dao.getCategoriesAvaliable()       
        result_list = []        
        for row in res:
            result = self.build_resource_avaliable(row)
            result_list.append(result)  
        sorted(result_list, key=lambda k: k['category'])
        return jsonify(Resources = result_list)    
    
    