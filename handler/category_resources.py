from flask import jsonify
from dao.category_resourcesDAO import category_ResourceDAO

class CategoryHandler: 


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
        result['avaliability'] = row[5]
        result['qty'] = row[6]
        result['dateAdded'] = row[7]
        result['lastUpdate'] = row[8]     
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
        sorted(result_list, key=lambda k: k['category'])
        return jsonify(Resources = result_list)
        

    def category(self,args):
        dao = category_ResourceDAO()
        category = args.get("cat")
        res = dao.getCategory(category)        
        result_list = []        
        for row in res:
            result = self.build_resource(row)
            result_list.append(result)  
        sorted(result_list, key=lambda k: k['category'])
        return jsonify(Resources = result_list)
    
    def categoryRequested(self,args):
        dao = category_ResourceDAO()  
        category = args.get("cat")        
        res = dao.getCategoryRequested(category)        
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
        res = dao.getCategoryAvaliable(category)       
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
    
    