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
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join supplier  order by resource_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester  order by requested_name ;"

        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesbyAid(self, aid):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join supplier   where account_id = %s order  by resource_name;"
        cursor.execute(query,(aid,))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester  where account_id = %s order by requested_name ;"
        cursor.execute(query,(aid,))
        for row in cursor:
            result.append(row)        
        return result
        
    def getResourcesbyDescription(self,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join supplier   where lower(description) LIKE '%%' || %s || '%%' order by resource_name ;"

        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester  where lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"

        cursor.execute(query,(description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyName(self,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join supplier   where lower(resource_name) = %s order by resource_name ;"

        cursor.execute(query,(name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity ,city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester  where lower(requested_name)= %s order by requested_name ;"

        cursor.execute(query,(name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyName_Description(self,name,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join supplier   where lower(description) LIKE '%%' || %s || '%%' and lower(resource_name)= %s order by resource_name  ;"

        cursor.execute(query,(description,name) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity, city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join requester where lower(description) LIKE '%%' || %s || '%%' and lower(requested_name)= %s order by requested_name  ;"
        cursor.execute(query,(description,name) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyRegion(self, Region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where region_name = %s order by resource_name   ;"
        cursor.execute(query,(Region,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where region_name = %s order by requested_name ;"
        cursor.execute(query,(Region,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyCity(self, City):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join supplier  where city_name = %s  order by resource_name ;"
        cursor.execute(query,(City,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity, city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join requester  where city_name = %s  order by requested_name;"
        cursor.execute(query,(City,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesbyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where region_name = %s and lower(resource_name)= %s order by resource_name  ;"
        cursor.execute(query,(Region,name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity, city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where region_name = %s and lower(requested_name)= %s order by requested_name ;"
        cursor.execute(query,(Region,name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query,(Region,description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity, city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join requester where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(Region,description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyCity_Name(self, City,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join region natural inner join supplier   where city_name = %s and lower(resource_name)= %s order by resource_name  ;"
        cursor.execute(query,(City,name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity, city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join region natural inner join requester   where city_name = %s and lower(requested_name)= %s  order by requested_name;"
        cursor.execute(query,(City,name,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesbyCity_Description(self, City,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability , city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query,(City,description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity, city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where region_name = %s and lower(description) LIKE '%%' || %s || '%%'order by requested_name  ;"
        cursor.execute(query,(City,description,) )
        for row in cursor:
            result.append(row)        
        return result
    def getResourcesbyKeywords(self, keywords):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability ,city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resource_keyword  natural inner join supplier   where lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query, (keywords,))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name from Resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join resources_requested_keywords  natural inner join requester where lower(keyword) LIKE '%%' || %s || '%%'  order by requested_name;"
        cursor.execute(query, (keywords,))
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesbyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability,city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resource_keyword natural inner join supplier   where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query,(city,keywords,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join resources_requested_keywords natural inner join requester  where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%'  order by requested_name;"
        cursor.execute(query,(city,keywords,) )
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesbyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability,city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier natural inner join resource_keyword where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query,(region,keywords,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region   natural inner join resources_requested_keywords natural inner join requester  where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(region,keywords,) )
        for row in cursor:
            result.append(row)          
        return result

    def getAllResourcesbyQty(self, qty):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join supplier   where availability= %s order by resource_name ;"
        cursor.execute(query,(qty,))
        result = []        
        for row in cursor:
            result.append(row)
    
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester where quantity= %s order by requested_name ;"
        cursor.execute(query,(qty,))
        for row in cursor:
            result.append(row)        
        return result

      
    def getAllResourcesbyQty_City(self,qty,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability,city_name from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join supplier where availability = %s and city_name = %s   order by resource_name  ;"
        cursor.execute(query,(qty,city,))

        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester where quantity = %s and city_name = %s order by requested_name ;"
        cursor.execute(query,(qty,city,))

        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesbyQty_Region(self,qty,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability ,city_name from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join supplier   where availability = %s and region_name = %s   order by resource_name  ;"
        cursor.execute(query,(qty,region,))

        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester where quantity = %s and region_name = %s order by requested_name  ;"
        cursor.execute(query,(qty,region,))

        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesbyQty_Keywords(self,qty,keywords):       
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability,city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join resource_keyword  natural inner join supplier   where availability = %s and lower(keyword) LIKE '%%' || %s || '%%'  order by resource_name ;"      
        cursor.execute(query,(qty,keywords,))

        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested

        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resources_requested_keywords natural inner join requester where quantity = %s and  lower(keyword) LIKE '%%' || %s || '%%'  order by requested_name;"
        cursor.execute(query,(qty,keywords,))
        for row in cursor:
            result.append(row)        
        return result      
       
    def getAllResourcesbyQty_Name(self,qty,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, description, class , availability,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join supplier    where availability = %s and lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(qty,name,) )

        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested

        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, class , quantity,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester where quantity = %s and lower(requested_name)= %s order by requested_name ;"
        cursor.execute(query,(qty,name,) )
        for row in cursor:
            result.append(row)        
        return result
    
############################################################################
#############            RESOURCES REQUESTED   
#############################################################################
        
      
     
    def getAllResourcesRequested(self):
        cursor = self.conn.cursor()
        query = " Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join location natural inner join City natural inner join Region  natural inner join requester order by requested_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result  
               

    def getResourcesRequestedbyDescription(self,description):
        cursor = self.conn.cursor()
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result
      

    def getResourcesRequestedbyName(self,name):
        cursor = self.conn.cursor()
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join requester where lower(requested_name)= %s order by requested_name ;"

        cursor.execute(query,(name,) )
        result = []        
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyName_Description(self,name,description):
        cursor = self.conn.cursor()
        result = []
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where lower(description) LIKE '%%' || %s || '%%' and lower(requested_name)= %s order by requested_name  ;"

        cursor.execute(query,(description,name) )
        for row in cursor:
            result.append(row)        
        return result
        
    def getResourcesRequestedbyRegion(self, Region):
        cursor = self.conn.cursor()        
        result = [] 
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where region_name = %s order by requested_name ;"

        cursor.execute(query,(Region,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyCity(self, City):
        cursor = self.conn.cursor()        
        result = []
        
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join requester  where city_name = %s order by requested_name ;"

        cursor.execute(query,(City,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesRequestedbyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()       
        result = []
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where region_name = %s and lower(requested_name)= %s order by requested_name ;"
        cursor.execute(query,(Region,name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(Region,description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyCity_Name(self, City,name):
        cursor = self.conn.cursor()       
        result = []        
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester   where city_name = %s and lower(requested_name)= %s order by requested_name ;"
        cursor.execute(query,(City,name,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesRequestedbyCity_Description(self, City,description):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join requester where region_name = %s and lower(description) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(City,description,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourceRequestedByRID(self, rid):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where request_id = %s order by requested_name ;"
        cursor.execute(query,(rid,) )
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords(self, keywords):
        cursor = self.conn.cursor()        
        result = []        
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description,  quantity, creation_date ,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join resources_requested_keywords  natural inner join requester where lower(keyword) LIKE '%%' || %s || '%%' order by requested_name  ;"
        cursor.execute(query, (keywords,))
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()       
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date ,city_name   from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join resources_requested_keywords natural inner join requester  where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(city,keywords,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()        
        #Get Resources requested
        query = "Select request_id,  requested_name  , type_name as category, requester_id, description,  quantity, creation_date  ,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join Region natural inner join resources_requested_keywords  natural inner join requester where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(region,keywords) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyQty(self, qty):
        cursor = self.conn.cursor()
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, requester_id, description,  quantity, creation_date ,city_name  from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester  where quantity = %s order by requested_name ;"
        cursor.execute(query,(qty,))
        result = []
        for row in cursor:
            result.append(row)        
        return result

      
    def getAllResourcesRequestedbyQty_City(self,qty,city):
        cursor = self.conn.cursor()
        result = []
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, requester_id, description,  quantity, creation_date ,city_name  from resources_requested natural inner join Resource_Type Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where quantity = %s and city_name = %s order by requested_name  ;"
        cursor.execute(query,(qty,city,))
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyQty_Region(self,qty,region):
        cursor = self.conn.cursor()
        result = []
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, requester_id, description,  quantity, creation_date  ,city_name from resources_requested natural inner join Resource_Type Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join requester  where quantity = %s and region_name = %s  order by requested_name;"
        cursor.execute(query,(qty,region,))

        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesRequestedbyQty_Keywords(self,qty,keywords):       
        cursor = self.conn.cursor()
        result = []
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, requester_id, description , quantity, creation_date  ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resources_requested_keywords natural inner join requester  where quantity = %s and  lower(keyword) LIKE '%%' || %s || '%%' order by requested_name ;"
        cursor.execute(query,(qty,keywords,))
        for row in cursor:
            result.append(row)        
        return result      
       
    def getAllResourcesRequestedbyQty_Name(self,qty,name):
        cursor = self.conn.cursor()
        result = []
        #Get Resources requested
        query =  "Select request_id,  requested_name  , type_name as category, requester_id, description, quantity, creation_date  ,city_name from resources_requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join requester where quantity = %s and lower(requested_name)= %s order by requested_name  ;"
        cursor.execute(query,(qty,name,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourceRequesteddbyARequesterID(self, id):
        cursor = self.conn.cursor()
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier natural inner join requester where requester_id = %s order by resource_name ;"
        cursor.execute(query,(id,))       
        result = []
        for row in cursor:
            result.append(row)
        return result 
    
###################################################################
#RESOURCES AVALIABLE
####################################################################

    def getAllResourcesAvaliable(self):
        cursor = self.conn.cursor()
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update  ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  order by resource_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result  
    def getResourcesAvaliablebyDescription(self,description):
        cursor = self.conn.cursor()
        result = []
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update  ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where lower(description) LIKE '%%' || %s || '%%'  order by resource_name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesAvaliablebyName(self,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update  ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(name,) )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesAvaliablebyName_Description(self,name,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update  ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where lower(description) LIKE '%%' || %s || '%%' and lower(resource_name)= %s  order by resource_name;"
        cursor.execute(query,(description,name) )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvaliablebyRegion(self, Region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where region_name = %s order by resource_name ;"
        cursor.execute(query,(Region,) )
        result = []
        for row in cursor:
            result.append(row)           
        return result


    def getResourcesAvaliablebyCity(self,City):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where city_name = %s order by resource_name  ;"
        cursor.execute(query,(City,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesAvaliablebyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where region_name = %s and lower(resource_name) = %s order by resource_name ;"

        cursor.execute(query,(Region,name,) )
        result = []
        for row in cursor:
            result.append(row)                
        return result

    def getResourcesAvaliabledbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update ,city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where region_name = %s and lower(description) LIKE '%%' || %s || '%%'  order by resource_name;"
        cursor.execute(query,(Region,description,) )
        result = []
        for row in cursor:
            result.append(row)           
        return result

    def getResourcesAvaliablebyCity_Name(self, City,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join supplier where city_name = %s and lower(resource_name)= %s order by resource_name ;"
        cursor.execute(query,(City,name,) )
        result = []
        for row in cursor:
            result.append(row)               
        return result


    def getResourcesAvaliablebyCity_Description(self, City,description):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where region_name = %s and lower(description) LIKE '%%' || %s || '%%'  order by resource_name;"
        cursor.execute(query,(City,description,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result

    def getResourceAvaliableByRID(self, rid):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where resource_id = %s order by resource_name  ;"
        cursor.execute(query,(rid,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result

    def getAllResourcesAvaliablebyKeywords(self, keywords):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  natural inner join resource_keyword where lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"
        cursor.execute(query, (keywords,))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getAllResourcesAvaliablebyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join resource_keyword natural inner join Region natural inner join supplier  where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name ;"

        cursor.execute(query,(city,keywords,) )
        result = []
        for row in cursor:
            result.append(row)    
        return result

    def getAllResourcesAvaliablebyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  natural inner join resource_keyword where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name ;"
        cursor.execute(query,(region,keywords,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesAvaliablebyQty(self, qty):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where quantity = %s order by resource_name ;"
        cursor.execute(query,(qty,))
        result = []
        for row in cursor:
            result.append(row)
         
        return result

      
    def getAllResourcesAvaliablebyQty_City(self,ty,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join supplier where quantity = %s and city_name = %s  order by resource_name ;"
        cursor.execute(query,(qty,city,))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getAllResourcesAvaliablebyQty_Region(self,qty,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region  natural inner join supplier where quantity = %s and region_name = %s order by resource_name ;"
        cursor.execute(query,(qty,region,))
        result = []
        for row in cursor:
            result.append(row)
           
        return result

    def getAllResourcesAvaliablebyQty_Keywords(self,qty,keywords):       
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  natural inner join resource_keyword where quantity = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name ;"      
        cursor.execute(query,(qty,keywords,))
        result = []
        for row in cursor:
            result.append(row)
             
        return result      
       

    def getResourcesAvaliablebyQty_Name(self,qty,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where quantity = %s and lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(qty,name,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result

    def getAllResourcesAvaliablebyQty(self, qty):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where quantity = %s order by resource_name ;"
        cursor.execute(query,(qty,))
        result = []
        for row in cursor:
            result.append(row)
         
        return result

      
    def getAllResourcesAvaliablebyQty_City(self,qty,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join supplier where quantity = %s and city_name = %s  order by resource_name  ;"
        cursor.execute(query,(qty,city,))
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesAvaliablebyQty_Region(self,qty,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join supplier where availability = %s and region_name = %s  order by resource_name  ;"
        cursor.execute(query,(qty,region,))
        result = []
        for row in cursor:
            result.append(row)
           
        return result

    def getAllResourcesAvaliablebyQty_Keywords(self, qty,keywords):       
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  natural inner join resource_keyword where availability = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name ;"      
        cursor.execute(query,(qty,keywords,))
        result = []
        for row in cursor:
            result.append(row)
             
        return result      
       
    def getAllResourcesAvaliablebyQty_Name(self,qty,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where quantity = %s and lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(qty,name,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result
    
    def getAllResourcesAvaliablebyPrice(self, price):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where price = %s  order by resource_name;"
        cursor.execute(query,(price,))
        result = []
        for row in cursor:
            result.append(row)
         
        return result

    def getAllResourcesAvaliablebyPrice_City(self,price,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join supplier where price = %s and city_name = %s order by resource_name   ;"
        cursor.execute(query,(price,city,))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getAllResourcesAvaliablebyPrice_Region(self,price,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join supplier where price = %s and region_name = %s order by resource_name   ;"
        cursor.execute(query,(price,region,))
        result = []
        for row in cursor:
            result.append(row)
           
        return result

    def getAllResourcesAvaliablebyPrice_Keywords(self,price,keywords):       
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  natural inner join resource_keyword where price = %s and lower(keyword) LIKE '%%' || %s || '%%' order by resource_name  ;"      
        cursor.execute(query,(price,keywords,))
        result = []
        for row in cursor:
            result.append(row)
             
        return result      
       
    def getAllResourcesAvaliablebyPrice_Name(self,price,name):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where price = %s and lower(resource_name) = %s order by resource_name ;"
        cursor.execute(query,(price,name,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result
    
    def getSupplierOfResourceAvaliablebyRID(self, rid):
        cursor = self.conn.cursor()
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier  where resource_id = %s by resource_name ;"
        cursor.execute(query,(rid,))       
        result = []
        for row in cursor:
            result.append(row)
        return result  

    def getResourceAvaliablebSuppliedbyID(self, id):
        cursor = self.conn.cursor()
        query = "Select resource_id,  resource_name , type_name as category, supplier_id, price, description, availability, creation_date,last_update,  city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region natural inner join  supplier where supplier_id = %s order by resource_name ;"
        cursor.execute(query,(id,))       
        result = []
        for row in cursor:
            result.append(row)
        return result 

################################################################################
#############    INSERT
################################################################################
    def insertRequested(self, name, resource_type, requester_id, description, qty, dt,keywords):
        cursor = self.conn.cursor()       
        query = "insert into resources_requested(requested_name, resource_type_id, description, quantity, creation_date, class,requester_id) values (%s, %s, %s, %s, %s, 'requested', %s) returning request_id;"
        cursor.execute(query, (name, resource_type, description, qty,dt,requester_id))
        
        id = cursor.fetchone()[0]
        query = "insert into resources_requested_keywords (keyword, request_id) values (%s, %s);"
        words = keywords.split()
        for key in words:  
            cursor.execute(query, (key, id,))
        self.conn.commit()
        return id        

    def insertAvailable(self, name,resource_type, supplier_id,price,description,availability,dt,dt2,keywords):
        cursor = self.conn.cursor()       
        query = "insert into resources(resource_name, resource_type_id, price, description, availability, creation_date, last_update, supplier_id, class) values (%s, %s, %s, %s, %s, %s, %s, %s ,'available') returning resource_id;"
        cursor.execute(query, ( name,resource_type,price,description,availability,dt,dt2,supplier_id,))
        id = cursor.fetchone()[0]
        query = "insert into resource_keyword (keyword, resource_id) values (%s, %s);"
        words = keywords.split()
        for key in words:  
            cursor.execute(query, (key, id,))        
        query = "insert into notifications (resource_type_id, message, title, notification_date_added, resource_id) values (%s, 'A resource from a requested resource has been added','New Resource Available', %s, %s);"
        cursor.execute(query, ( resource_type, dt,id,))
        self.conn.commit()
        return id
        


    ##############################################################################
    ###################  UPDATE
    ##############################################################################


    def updateRequested(self,id,name, resource_type, description, qty ):
        cursor = self.conn.cursor()       
        query = "update resources_requested set requested_name = %s, resource_type_id = %s, description = %s, quantity = %s where request_id = %s;"
        cursor.execute(query, (name, resource_type, description, qty,id,))
        self.conn.commit()

    def updateRequestedQty(self,id,qty ):
        cursor = self.conn.cursor()       
        query = "update resources_requested set quantity = %s where request_id = %s;"
        cursor.execute(query, (name, qty, id,))
        self.conn.commit()


    def updateAvailable(self,id, name,resource_type,price,description,availability,dt):
        cursor = self.conn.cursor()       
        query = "update resources set resource_name = %s, resource_type_id = %s, price=%s, description=%s, availability=%s , last_update = %s where resource_id = %s;"
        cursor.execute(query, (name,resource_type,price,description,availability,dt, id,))
        self.conn.commit()


    def updateAvailablePrice(self,id, price):
        cursor = self.conn.cursor()       
        query = "update resources set price=%s where resource_id = %s;"
        cursor.execute(query, (price,id,))
        self.conn.commit()

    def updateAvailableAvailability(self,id, availability):
        cursor = self.conn.cursor()       
        query = "update resources set availability=%s where resource_id = %s;"
        cursor.execute(query, (availability,id,))
        self.conn.commit()
        
        
        
