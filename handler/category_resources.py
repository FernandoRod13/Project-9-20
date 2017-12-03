from flask import jsonify
from dao.category_resourcesDAO import category_ResourceDAO

class CategoryHandler:    

    def __init__(self):
        pass    
    
    def categoryRequested(self,keywords):
        dao = category_ResourceDAO()
        return dao.getCategoryRequested(keywords)       
    
    def categoryRequested_subcategory(self,keywords,subkeywords):
        dao = category_ResourceDAO()
        return dao.getCategoryRequested_subcategory(keywords,subkeywords)