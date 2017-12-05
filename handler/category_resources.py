from flask import jsonify
from dao.category_resourcesDAO import category_ResourceDAO

class CategoryHandler:    

    def __init__(self):
        pass    

    def categories(self):
        dao = category_ResourceDAO()
        return jsonify(dao.getCategories())
    
    def categoryRequested(self,keywords):
        dao = category_ResourceDAO()
        return jsonify(dao.getCategoryRequested(keywords) )      
    
    def categoryRequested_subcategory(self,keywords,subkeywords):
        dao = category_ResourceDAO()
        return jsonify(dao.getCategoryRequested_subcategory(keywords,subkeywords))
     
    def categoryAvaliable(self,keywords):
        dao = category_ResourceDAO()
        return jsonify(dao.getCategoryAvaliable(keywords))   
    
    def categoryAvaliable_subcategory(self,keywords,subkeywords):
        dao = category_ResourceDAO()
        return jsonify(dao.getCategoryAvaliable_subcategory(keywords,subkeywords))