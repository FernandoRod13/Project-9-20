import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config

class ResourceDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable',hostaddr='35.196.249.53')     

    def getAllResources(self):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City order by resource_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City order by requested_name ;"

        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesbyAid(self, aid):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where account_id = %s order  by resource_name;"
        cursor.execute(query,(aid,))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where account_id = %s order by requested_name ;"
        cursor.execute(query,(aid,))
        for row in cursor:
            result.append(row)        
        return result
        
    def getResourcesbyDescription(self,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where lower(description) LIKE '%%' || %s || '%%' order by resource_name ;"

        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"

        cursor.execute(query,(description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyName(self,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where lower(resource_name) = %s order by resource_name ;"

        cursor.execute(query,(name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where lower(requested_name)= %s order by requested_name ;"

        cursor.execute(query,(name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyName_Description(self,name,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where lower(description) LIKE '%%' || %s || '%%' and lower(resource_name)= %s order by resource_name  ;"

        cursor.execute(query,(description,name) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where lower(description) LIKE '%%' || %s || '%%' and lower(requested_name)= %s order by requested_name  ;"
        cursor.execute(query,(description,name) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyRegion(self, Region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s order by resource_name   ;"
        cursor.execute(query,(Region,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s order by requested_name ;"
        cursor.execute(query,(Region,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyCity(self, City):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name = %s  order by resource_name ;"
        cursor.execute(query,(City,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where city_name = %s  order by requested_name;"
        cursor.execute(query,(City,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesbyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(resource_name)= %s order by resource_name  ;"
        cursor.execute(query,(Region,name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(requested_name)= %s order by requested_name ;"
        cursor.execute(query,(Region,name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query,(Region,description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(Region,description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyCity_Name(self, City,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join region where city_name = %s and lower(resource_name)= %s order by resource_name  ;"
        cursor.execute(query,(City,name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join region  where city_name = %s and lower(requested_name)= %s  order by requested_name;"
        cursor.execute(query,(City,name,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesbyCity_Description(self, City,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity , city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query,(City,description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%'order by requested_name  ;"
        cursor.execute(query,(City,description,) )
        for row in cursor:
            result.append(row)        
        return result
    def getResourcesbyKeywords(self, keywords):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity ,city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resource_keyword where lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query, (keywords,))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join resources_requested_keywords where lower(keyword) LIKE '%%' || %s || '%%'  order by requested_name;"
        cursor.execute(query, (keywords,))
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesbyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity,city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resource_keyword where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query,(city,keywords,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join resources_requested_keywords where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%'  order by requested_name;"
        cursor.execute(query,(city,keywords,) )
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesbyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity,city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join resource_keyword where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query,(region,keywords,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region   natural inner join resources_requested_keywords where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(region,keywords,) )
        for row in cursor:
            result.append(row)          
        return result

    def getAllResourcesbyQty(self, qty):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity= %s order by resource_name ;"
        cursor.execute(query,(qty,))
        result = []        
        for row in cursor:
            result.append(row)
    
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity= %s order by requested_name ;"
        cursor.execute(query,(qty,))
        for row in cursor:
            result.append(row)        
        return result

      
    def getAllResourcesbyQty_City(self,qty,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity,city_name from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and city_name = %s   order by resource_name  ;"
        cursor.execute(query,(qty,city,))

        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and city_name = %s order by requested_name ;"
        cursor.execute(query,(qty,city,))

        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesbyQty_Region(self,qty,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity ,city_name from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and region_name = %s   order by resource_name  ;"
        cursor.execute(query,(qty,region,))

        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and region_name = %s order by requested_name  ;"
        cursor.execute(query,(qty,region,))

        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesbyQty_Keywords(self,qty,keywords):       
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity,city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join resource_keyword where quantity = %s and lower(keyword) LIKE '%%' || %s || '%%'  order by resource_name ;"      
        cursor.execute(query,(qty,keywords,))

        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested

        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resources_requested_keywords where quantity = %s and  lower(keyword) LIKE '%%' || %s || '%%'  order by requested_name;"
        cursor.execute(query,(qty,keywords,))
        for row in cursor:
            result.append(row)        
        return result      
       
    def getAllResourcesbyQty_Name(self,qty,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where quantity = %s and lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(qty,name,) )

        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested

        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s and lower(requested_name)= %s order by requested_name ;"
        cursor.execute(query,(qty,name,) )
        for row in cursor:
            result.append(row)        
        return result
    
############################################################################
#############            RESOURCES REQUESTED   
#############################################################################
        
      
     
    def getAllResourcesRequested(self):
        cursor = self.conn.cursor()
        query = " Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join location natural inner join City natural inner join Region order by requested_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result  
               

    def getResourcesRequestedbyDescription(self,description):
        cursor = self.conn.cursor()
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result
      

    def getResourcesRequestedbyName(self,name):
        cursor = self.conn.cursor()
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where lower(requested_name)= %s order by requested_name ;"

        cursor.execute(query,(name,) )
        result = []        
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyName_Description(self,name,description):
        cursor = self.conn.cursor()
        result = []
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where lower(description) LIKE '%%' || %s || '%%' and lower(requested_name)= %s order by requested_name  ;"

        cursor.execute(query,(description,name) )
        for row in cursor:
            result.append(row)        
        return result
        
    def getResourcesRequestedbyRegion(self, Region):
        cursor = self.conn.cursor()        
        result = [] 
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s order by requested_name ;"

        cursor.execute(query,(Region,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyCity(self, City):
        cursor = self.conn.cursor()        
        result = []
        
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where city_name = %s order by requested_name ;"

        cursor.execute(query,(City,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesRequestedbyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()       
        result = []
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(requested_name)= %s order by requested_name ;"
        cursor.execute(query,(Region,name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(Region,description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyCity_Name(self, City,name):
        cursor = self.conn.cursor()       
        result = []        
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where city_name = %s and lower(requested_name)= %s order by requested_name ;"
        cursor.execute(query,(City,name,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesRequestedbyCity_Description(self, City,description):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(City,description,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourceRequestedByRID(self, rid):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where request_id = %s order by requested_name ;"
        cursor.execute(query,(rid,) )
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords(self, keywords):
        cursor = self.conn.cursor()        
        result = []        
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_date ,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join resources_requested_keywords where lower(keyword) LIKE '%%' || %s || '%%' order by requested_name  ;"
        cursor.execute(query, (keywords,))
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()       
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date ,city_name   from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join resources_requested_keywords where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(city,keywords,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()        
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_date  ,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join Region natural inner join resources_requested_keywords where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(region,keywords) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyQty(self, qty):
        cursor = self.conn.cursor()
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_date ,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s order by requested_name ;"
        cursor.execute(query,(qty,))
        result = []
        for row in cursor:
            result.append(row)        
        return result

      
    def getAllResourcesRequestedbyQty_City(self,qty,city):
        cursor = self.conn.cursor()
        result = []
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_date ,city_name  from resources_requested natural inner join Resource_Type Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and city_name = %s order by requested_name  ;"
        cursor.execute(query,(qty,city,))
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyQty_Region(self,qty,region):
        cursor = self.conn.cursor()
        result = []
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_date  ,city_name from resources_requested natural inner join Resource_Type Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and region_name = %s  order by requested_name;"
        cursor.execute(query,(qty,region,))

        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesRequestedbyQty_Keywords(self,qty,keywords):       
        cursor = self.conn.cursor()
        result = []
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, account_id, description , quantity, creation_date  ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resources_requested_keywords where quantity = %s and  lower(keyword) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(qty,keywords,))
        for row in cursor:
            result.append(row)        
        return result      
       
    def getAllResourcesRequestedbyQty_Name(self,qty,name):
        cursor = self.conn.cursor()
        result = []
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_date  ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s and lower(requested_name)= %s order by requested_name  ;"
        cursor.execute(query,(qty,name,) )
        for row in cursor:
            result.append(row)        
        return result
    
###################################################################
#RESOURCES AVALIABLE
####################################################################

    def getAllResourcesAvaliable(self):
        cursor = self.conn.cursor()
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update  ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  order by resource_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result  
    def getResourcesAvaliablebyDescription(self,description):
        cursor = self.conn.cursor()
        result = []
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update  ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where lower(description) LIKE '%%' || %s || '%%'  order by resource_name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesAvaliablebyName(self,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update  ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(name,) )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesAvaliablebyName_Description(self,name,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update  ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where lower(description) LIKE '%%' || %s || '%%' and lower(resource_name)= %s  order by resource_name;"
        cursor.execute(query,(description,name) )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvaliablebyRegion(self, Region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s order by resource_name ;"
        cursor.execute(query,(Region,) )
        result = []
        for row in cursor:
            result.append(row)           
        return result


    def getResourcesAvaliablebyCity(self,City):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s order by resource_name  ;"
        cursor.execute(query,(City,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesAvaliablebyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(resource_name) = %s order by resource_name ;"

        cursor.execute(query,(Region,name,) )
        result = []
        for row in cursor:
            result.append(row)                
        return result

    def getResourcesAvaliabledbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%'  order by resource_name;"
        cursor.execute(query,(Region,description,) )
        result = []
        for row in cursor:
            result.append(row)           
        return result

    def getResourcesAvaliablebyCity_Name(self, City,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name = %s and lower(resource_name)= %s order by resource_name ;"
        cursor.execute(query,(City,name,) )
        result = []
        for row in cursor:
            result.append(row)               
        return result


    def getResourcesAvaliablebyCity_Description(self, City,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%'  order by resource_name;"
        cursor.execute(query,(City,description,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result

    def getResourceAvaliableByRID(self, rid):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where resource_id = %s order by resource_name  ;"
        cursor.execute(query,(rid,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result

    def getAllResourcesAvaliablebyKeywords(self, keywords):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join resource_keyword where lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query, (keywords,))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getAllResourcesAvaliablebyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resource_keyword natural inner join Region where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name ;"

        cursor.execute(query,(city,keywords,) )
        result = []
        for row in cursor:
            result.append(row)    
        return result

    def getAllResourcesAvaliablebyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join resource_keyword where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name ;"
        cursor.execute(query,(region,keywords,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesAvaliablebyQty(self, qty):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where quantity = %s order by resource_name ;"
        cursor.execute(query,(qty,))
        result = []
        for row in cursor:
            result.append(row)
         
        return result

      
    def getAllResourcesAvaliablebyQty_City(self,ty,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and city_name = %s  order by resource_name ;"
        cursor.execute(query,(qty,city,))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getAllResourcesAvaliablebyQty_Region(self,qty,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and region_name = %s order by resource_name ;"
        cursor.execute(query,(qty,region,))
        result = []
        for row in cursor:
            result.append(row)
           
        return result

    def getAllResourcesAvaliablebyQty_Keywords(self,qty,keywords):       
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join resource_keyword where quantity = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name ;"      
        cursor.execute(query,(qty,keywords,))
        result = []
        for row in cursor:
            result.append(row)
             
        return result      
       

    def getResourcesAvaliablebyQty_Name(self,qty,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where quantity = %s and lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(qty,name,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result

    def getAllResourcesAvaliablebyQty(self, qty):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where quantity = %s order by resource_name ;"
        cursor.execute(query,(qty,))
        result = []
        for row in cursor:
            result.append(row)
         
        return result

      
    def getAllResourcesAvaliablebyQty_City(self,qty,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and city_name = %s  order by resource_name  ;"
        cursor.execute(query,(qty,city,))
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesAvaliablebyQty_Region(self,qty,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where quantity = %s and region_name = %s  order by resource_name  ;"
        cursor.execute(query,(qty,region,))
        result = []
        for row in cursor:
            result.append(row)
           
        return result

    def getAllResourcesAvaliablebyQty_Keywords(self, qty,keywords):       
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join resource_keyword where quantity = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name ;"      
        cursor.execute(query,(qty,keywords,))
        result = []
        for row in cursor:
            result.append(row)
             
        return result      
       
    def getAllResourcesAvaliablebyQty_Name(self,qty,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where quantity = %s and lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(qty,name,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result
    
    def getAllResourcesAvaliablebyPrice(self, price):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where price = %s  order by resource_name;"
        cursor.execute(query,(price,))
        result = []
        for row in cursor:
            result.append(row)
         
        return result

    def getAllResourcesAvaliablebyPrice_City(self,price,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where price = %s and city_name = %s order by resource_name   ;"
        cursor.execute(query,(price,city,))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getAllResourcesAvaliablebyPrice_Region(self,price,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where price = %s and region_name = %s order by resource_name   ;"
        cursor.execute(query,(price,region,))
        result = []
        for row in cursor:
            result.append(row)
           
        return result

    def getAllResourcesAvaliablebyPrice_Keywords(self,price,keywords):       
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join resource_keyword where price = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"      
        cursor.execute(query,(price,keywords,))
        result = []
        for row in cursor:
            result.append(row)
             
        return result      
       
    def getAllResourcesAvaliablebyPrice_Name(self,price,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  where price = %s and lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(price,name,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result
    
    def getSupplierOfResourceAvaliablebyRID(self, rid):
        cursor = self.conn.cursor()
        query = "Select account_id as supplier_id, first_name, last_name, email, phone, city_name from resources natural inner join accounts natural inner join location natural inner join city where resource_id = %s and account_type = 'Supplier';"
        cursor.execute(query,(rid,))       
        result = []
        for row in cursor:
            result.append(row)
        return result  

################################################################################
#############    INSERT
################################################################################
    def insertRequested(self, name, resource_type, requester_id, description, qty, dt):
        cursor = self.conn.cursor()       
        query = "insert into resources_requested(name, resource_type_id, account_id,description, quantity, creation_date) values (%s, %s, %s, %s, %s, %s ) returning request_id;"
        cursor.execute(query, (name, resource_type, requester_id,description, qty,dt,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def insertAvailable(self, name,resource_type, supplier_id,price,description,qty,availability,dt,dt2):
        cursor = self.conn.cursor()       
        query = "insert into resources(resource_name, resource_type_id, account_id,price, description, quantity,availability, creation_date, last_update) values (%s, %s, %s, %s, %s, %s, %s, %s, %s ) returning resource_id;"
        cursor.execute(query, ( name,resource_type,supplier_id,price,description,qty,availability,dt,dt2,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid


    ##############################################################################
    ###################  UPDATE
    ##############################################################################


    def updateRequested(self,id,name, resource_type, requester_id,description, qty ):
        cursor = self.conn.cursor()       
        query = "update resources_requested set requested_name = %s, resource_type = %s, requester_id = %s, description = %s, quantity = %s where resource_id = %s;"
        cursor.execute(query, (name, resource_type, requester_id,description, qty,id,))
        self.conn.commit()

    def updateRequestedQty(self,id,qty ):
        cursor = self.conn.cursor()       
        query = "update resources_requested set quantity = %s where resource_id = %s;"
        cursor.execute(query, (name, qty, id,))
        self.conn.commit()

/
    def updateAvailable(self,id, name,resource_type,supplier_id,price,description,qty,availability):
        cursor = self.conn.cursor()       
        query = "update resources set resource_name = %s, resource_type_id = %s, account_id = %s ,price=%s, description=%s, quantity=%s,availability=%s where resource_id = %s;"
        cursor.execute(query, (name,resource_type,supplier_id,price,description,qty,availability,id,))
        self.conn.commit()

    def updateAvailableQty(self,id, qty):
        cursor = self.conn.cursor()       
        query = "update resources set quantity=%s where resource_id = %s;"
        cursor.execute(query, (qty,id,))
        self.conn.commit()

    def updateAvailableQty(self,id, price):
        cursor = self.conn.cursor()       
        query = "update resources set price=%s where resource_id = %s;"
        cursor.execute(query, (price,id,))
        self.conn.commit()

    def updateAvailableAvailability(self,id, availability):
        cursor = self.conn.cursor()       
        query = "update resources set availability=%s where resource_id = %s;"
        cursor.execute(query, (availability,id,))
        self.conn.commit()
        
        
        