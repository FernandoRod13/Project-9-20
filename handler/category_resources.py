from flask import jsonify
from dao.category_resourcesDAO import category_ResourceDAO

class CategoryHandler:    

    def __init__(self):
        pass    
    
    def CategoryRequested(self,keywords):
        dao = category_ResourceDAO()
        return dao.getCategoryRequested(self, keywords)
   