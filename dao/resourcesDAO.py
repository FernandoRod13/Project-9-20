import json
import psycopg2
from flask import jsonify


class ResourceDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='natalia', password='none', sslmode='disable',hostaddr='35.196.249.53')
           
    def getAllResourcesRequested(self):
        cursor = self.conn.cursor()
        query = "select * from test where lower(name) LIKE '%%' || %s || '%%';"
       
        look = "a"
        #query = "select name, Resource_Type.name as category, accountID, description,quantity from Resouces  natural inner join Resource_Type orderby name;"
        cursor.execute(query,(look,))
       
        result = []
        for row in cursor:
            result.append(row)
        return result       

    def getAllResourcesAvaliable(self):
        cursor = self.conn.cursor()
        query  = "Select * from test;"
        #query = "Select name, Resource_Type.name as category, accountID, price, description,avaliability, quantity from Resouces natural inner join Resource_Type orderby name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result  
    
   
    def getAllResources(self):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type  orderby name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type orderby name;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyDescription(self,description):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type where lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type where lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyName(self,name):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type where lower(name) = %s orderby name;"
        cursor.execute(query,(name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type where lower(description)= %s orderby name;"
        cursor.execute(query,(name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyName_Description(self,name,description):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type where lower(description) LIKE '%%' || %s || '%%' and name= %s orderby name;"
        cursor.execute(query,(description,name) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type where lower(description) LIKE '%%' || %s || '%%' and name= %s orderby name;"
        cursor.execute(query,(description,name) )
        for row in cursor:
            result.append(row)        
        return result     
   

    def getResourcesbyRegion(self, Region):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s orderby name;"
        cursor.execute(query,(Region,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s orderby name;"
        cursor.execute(query,(Region,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyCity(self, City):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name = %s orderby name;"
        cursor.execute(query,(City,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where city_name = %s orderby name;"
        cursor.execute(query,(City,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesbyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and name = %s orderby name;"
        cursor.execute(query,(Region,name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and name = %s orderby name;"
        cursor.execute(query,(Region,name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(Region,description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(Region,description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesbyCity_Name(self, City,name):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name = %s and name = %s orderby name;"
        cursor.execute(query,(City,name,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where city_name = %s and name = %s orderby name;"
        cursor.execute(query,(City,name,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesbyCity_Description(self, City,description):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(City,description,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(City,description,) )
        for row in cursor:
            result.append(row)        
        return result
    def getResourcesbyKeywords(self, keywords):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Resource_Keywords where lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query, (keywords,))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type natural inner join Resource_Keywords where lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query, (keywords,))
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesbyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Resource_Keywords where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(city,keywords,) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join Resource_Keywords where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(city,keywords,) )
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesbyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Resource_Keywords where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(region,keywords) )
        result = []
        for row in cursor:
            result.append(row)
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join Resource_Keywords where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(region,keywords) )
        for row in cursor:
            result.append(row)        
        return result
    
#############################################################
    #RESOURCES REQUESTED   
#############################################################################
               

    def getResourcesRequestedbyDescription(self,description):
        cursor = self.conn.cursor()
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type where lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result
      

    def getResourcesRequestedbyName(self,name):
        cursor = self.conn.cursor()
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type where lower(description)= %s orderby name;"
        cursor.execute(query,(name,) )
        result = []        
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyName_Description(self,name,description):
        cursor = self.conn.cursor()
        result = []
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type where lower(description) LIKE '%%' || %s || '%%' and name= %s orderby name;"
        cursor.execute(query,(description,name) )
        for row in cursor:
            result.append(row)        
        return result
        
    def getResourcesRequestedbyRegion(self, Region):
        cursor = self.conn.cursor()        
        result = [] 
        query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s orderby name;"
        cursor.execute(query,(Region,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyCity(self, City):
        cursor = self.conn.cursor()        
        result = []
        
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where city_name = %s orderby name;"
        cursor.execute(query,(City,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesRequestedbyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()       
        result = []
        query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and name = %s orderby name;"
        cursor.execute(query,(Region,name,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(Region,description,) )
        for row in cursor:
            result.append(row)        
        return result

    def getResourcesRequestedbyCity_Name(self, City,name):
        cursor = self.conn.cursor()       
        result = []        
        query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where city_name = %s and name = %s orderby name;"
        cursor.execute(query,(City,name,) )
        for row in cursor:
            result.append(row)        
        return result


    def getResourcesRequestedbyCity_Description(self, City,description):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(City,description,) )
        for row in cursor:
            result.append(row)        
        return result


    def getAllResourcesRequestedbyRID(self, rid):
        cursor = self.conn.cursor()        
        result = []        
        query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts where accountID = %s orderby name;"
        cursor.execute(query,(rid,) )
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords(self, keywords):
        cursor = self.conn.cursor()        
        result = []        
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces_Requested natural inner join Resource_Type natural inner join Resource_Keywords where lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query, (keywords,))
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()       
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join Resource_Keywords where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(city,keywords,) )
        for row in cursor:
            result.append(row)        
        return result

    def getAllResourcesRequestedbyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()        
        #Get Resouces requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  natural inner join Resource_Keywords where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(region,keywords) )
        for row in cursor:
            result.append(row)        
        return result
    

###################################################################
#RESOURCES AVALIABLE
####################################################################
    def getResourcesAvaliablebyDescription(self,description):
        cursor = self.conn.cursor()
        result = []
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type where lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(description,) )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesAvaliablebyName(self,name):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type where lower(name) = %s orderby name;"
        cursor.execute(query,(name,) )
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesAvaliablebyName_Description(self,name,description):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type where lower(description) LIKE '%%' || %s || '%%' and name= %s orderby name;"
        cursor.execute(query,(description,name) )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvaliablebyRegion(self, Region):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s orderby name;"
        cursor.execute(query,(Region,) )
        result = []
        for row in cursor:
            result.append(row)           
        return result


    def getResourcesAvaliablebyCity(self,City):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name = %s orderby name;"
        cursor.execute(query,(City,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result


    def getResourcesAvaliablebyRegion_Name(self, Region,name):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdatefrom Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and name = %s orderby name;"
        cursor.execute(query,(Region,name,) )
        result = []
        for row in cursor:
            result.append(row)                
        return result

    def getResourcesAvaliabledbyRegion_Description(self, Region,description):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdatefrom Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(Region,description,) )
        result = []
        for row in cursor:
            result.append(row)           
        return result

    def getResourcesAvaliablebyCity_Name(self, City,name):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name = %s and name = %s orderby name;"
        cursor.execute(query,(City,name,) )
        result = []
        for row in cursor:
            result.append(row)               
        return result


    def getResourcesAvaliablebyCity_Description(self, City,description):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and lower(description) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(City,description,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result

    def getAllResourcesAvaliablebySID(self, sid):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resouces natural inner join Resource_Type natural inner join Accounts where accountID = %s orderby name;"
        cursor.execute(query,(sid,) )
        result = []
        for row in cursor:
            result.append(row)              
        return result

    def getAllResourcesAvaliablebyKeywords(self, keywords):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Resource_Keywords where lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query, (keywords,))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getAllResourcesAvaliablebyKeywords_City(self, keywords, city):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Resource_Keywords where city_name = %s and lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(city,keywords,) )
        result = []
        for row in cursor:
            result.append(row)    
        return result

    def getAllResourcesAvaliablebyKeywords_Region(self, keywords, region):
        cursor = self.conn.cursor()
        #Get Resouces avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resouces natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Resource_Keywords where region_name = %s and lower(keyword) LIKE '%%' || %s || '%%' orderby name;"
        cursor.execute(query,(region,keywords) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    
    
    