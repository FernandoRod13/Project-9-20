import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config

class ResourceDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='natalia', password='none', sslmode='disable',hostaddr='35.196.249.53')
       

    def loadRequested(self):
        with open('JsonMakers/resources_requested_data.json') as data_file:    
            return json.load(data_file)

    def loadAvaliable(self):
        with open('JsonMakers/resources_avaliable_data.json') as data_file:    
            return json.load(data_file)
       
    def getAllResourcesRequested(self):
        #return self.loadRequested()
        cursor = self.conn.cursor()
        query = "select * from test where lower(name) LIKE '%%' || %s || '%%';"
       
        look = "a"
        #query = "select name, resource_type.name as category, accountID, description,quantity from resources  natural inner join resource_type orderby name;"
        cursor.execute(query,(look,))
       
        result = []
        for row in cursor:
            result.append(row)
        return result       

    def getAllResourcesAvaliable(self):
        cursor = self.conn.cursor()
        query  = "Select * from test;"
        #query = "Select name, resource_type.name as category, accountID, price, description,avaliability, quantity from resources natural inner join resource_type orderby name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result  
    
   
    def getAllResources(self):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type  orderby name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requested natural inner join resource_type orderby name;"
        cursor.execute(query,(description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyDescription(self,description):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type where lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requested natural inner join resource_type where lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyName(self,name):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type where lower(name) = %s orderby name;"
        cursor.execute(query,(name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requested natural inner join resource_type where lower(description)= %s orderby name;"
        cursor.execute(query,(name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyName_Description(self,name,description):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type where lower(description) LIKE '%%' || %s || '%%' and name= %s orderby name;"
        cursor.execute(query,(description,name) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requested natural inner join resource_type where lower(description) LIKE '%%' || %s || '%%' and name= %s orderby name;"
        cursor.execute(query,(description,name) )
        for row in cursor:
            result.append(row)        
        return result

           

    def getResourcesRequestedbyDescription(self,description):
        cursor = self.conn.cursor()
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requested natural inner join resource_type where lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result
      

    def getResourcesRequestedbyName(self,name):
        cursor = self.conn.cursor()
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requested natural inner join resource_type where lower(description)= %s orderby name;"
        cursor.execute(query,(name,) )
        result = []        
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyName_Description(self,name,description):
        cursor = self.conn.cursor()
        result = []
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requested natural inner join resource_type where lower(description) LIKE '%%' || %s || '%%' and name= %s orderby name;"
        cursor.execute(query,(description,name) )
        for row in cursor:
            result.append(row)        
        return result
        

        

    def getResourcesAvaliablebyDescription(self,description):
        cursor = self.conn.cursor()
        result = []
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type where lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesAvaliablebyName(self,name):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type where lower(name) = %s orderby name;"
        cursor.execute(query,(name,) )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesAvaliablebyName_Description(self,name,description):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type where lower(description) LIKE '%%' || %s || '%%' and name= %s orderby name;"
        cursor.execute(query,(description,name) )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesbyRegion(self, region):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type natural inner join accounts natural inner join location natural inner join city natural inner join region where region_name = %s orderby name;"
        cursor.execute(query,(region,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requests natural inner join resource_type natural inner join accounts natural inner join location natural inner join city natural inner join region where region_name = %s orderby name;"
        cursor.execute(query,(region,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyCity(self, city):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type natural inner join accounts natural inner join location natural inner join city where city_name = %s orderby name;"
        cursor.execute(query,(city,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requests natural inner join resource_type natural inner join accounts natural inner join location natural inner join city  where city_name = %s orderby name;"
        cursor.execute(query,(city,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesbyRegion_Name(self, region,name):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type natural inner join accounts natural inner join location natural inner join city natural inner join region where region_name = %s and name = %s orderby name;"
        cursor.execute(query,(region,name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requests natural inner join resource_type natural inner join accounts natural inner join location natural inner join city natural inner join region where region_name = %s and name = %s orderby name;"
        cursor.execute(query,(region,name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyRegion_Description(self, region,description):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type natural inner join accounts natural inner join location natural inner join city natural inner join region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(region,description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requests natural inner join resource_type natural inner join accounts natural inner join location natural inner join city natural inner join region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(region,description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyCity_Name(self, city,name):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type natural inner join accounts natural inner join location natural inner join city where city_name = %s and name = %s orderby name;"
        cursor.execute(query,(city,name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requests natural inner join resource_type natural inner join accounts natural inner join location natural inner join city  where city_name = %s and name = %s orderby name;"
        cursor.execute(query,(city,name,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesbyCity_Description(self, city,description):
        cursor = self.conn.cursor()
        #Get resources avaliable
        query = "Select name , resource_type.name as category, accountID, description, class from resources natural inner join resource_type natural inner join accounts natural inner join location natural inner join city natural inner join region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(region,description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get resources requested
        query = "Select name , resource_type.name as category, accountID, description, class from resources_requests natural inner join resource_type natural inner join accounts natural inner join location natural inner join city natural inner join region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(region,description,) )
        for row in cursor:
            result.append(row)        
        return result
    

      
