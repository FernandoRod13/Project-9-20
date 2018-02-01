import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config

class RequesterDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable', hostaddr='35.196.249.53')

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Requester';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersByCity(self,city):
        cursor = self.conn.cursor()
        query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Requester' and city_name = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersByRegion(self,region):
        cursor = self.conn.cursor()
        query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join region where account_type = 'Requester' and region_name = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequesterByID(self,id):
        cursor = self.conn.cursor()
        query = "select requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join requester where account_type = 'Requester' and requester_id = %s;"
        cursor.execute(query, (id,))
        return cursor.fetchone()

    def searchRequestersRequestingResource(self,resource_name):
        cursor = self.conn.cursor()
        query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested where account_type = 'Requester' and requested_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersRequestingResourceByCategory(self, type_name):
        cursor = self.conn.cursor()
        if( type_name == 'fuel'):
            query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested natural inner join resource_type where account_type = 'Requester' and ( type_name = 'propane' or type_name = 'gasoline' or type_name = 'diesel');"
            cursor.execute(query)
        elif( type_name == 'water'):
            query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested natural inner join resource_type where account_type = 'Requester' and ( type_name = 'smallbottles' or type_name = 'gallonbottles' );"
            cursor.execute(query)
        else:
            query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested n  'atural inner join resource_type where account_type = 'Requester' and type_name = %s;"
            cursor.execute(query, (type_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersRequestingResourceInCity(self, resource_name, city):
        cursor = self.conn.cursor()
        query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested where account_type = 'Requester' and requested_name = %s and city_name = %s;"
        cursor.execute(query, (resource_name, city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersByName(self, name): 
        cursor = self.conn.cursor()
        query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Requester' and  (first_name = %s or last_name =%s);"
        cursor.execute(query, (name, name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersByResourceKeyword(self,keyword):
        cursor = self.conn.cursor()
        query = "select   requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested natural inner join resource_keyword where account_type = 'Requester' and  keyword LIKE '%%' || %s || '%%';"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result



#########################################################################
####  INSERT
############################################################################

    def addRequester(self, first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url , account_type , password, dt):
        cursor = self.conn.cursor()       
        query = "insert into location (address, city_id, latitude, longitude) values (%s, %s, %s, %s ) returning location_id;"
        cursor.execute(query, ( address,city_id,latitude, longitud,))
        location_id = cursor.fetchone()[0]
        query = "insert into accounts (first_name , last_name , email , phone , location_id , photo_url , account_type , account_creation_date, password) values (%s, %s, %s, %s, %s, %s, %s, %s, %s ) returning account_id;"
        cursor.execute(query, (first_name , last_name , email , phone , location_id , photo_url , account_type , dt, password,))
        account_id = cursor.fetchone()[0]
        query = "insert into requester (account_id) values (%s) returning requester_id;"
        cursor.execute(query, ( account_id,))
        requester_id = cursor.fetchone()[0]
        self.conn.commit()
        return requester_id;    
    

#########################################################################
####  Update
############################################################################

    def updateRequester(self,id,first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url):
        cursor = self.conn.cursor() 
        query = "Select account_id from requester where requester_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "Select location_id from accounts where account_id = %s;"
        cursor.execute(query, ( account_id,))
        location_id = cursor.fetchone()[0]            
        query = "update location set address = %s, city_id = %s, latitude = %s , longitude = %s where location_id = %s"
        cursor.execute(query, ( address,city_id,latitude, longitud,location_id,))
        query = "update accounts set first_name = %s , last_name  = %s , email  = %s , phone = %s , photo_url  = %s where account_id = %s;"
        cursor.execute(query, (first_name , last_name , email , phone ,  photo_url  ,account_id,))
        self.conn.commit()        
        return id;

    def updateRequesterPhone(self,id, phone):
        cursor = self.conn.cursor() 
        query = "Select account_id from requester where requester_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set phone  = %s where account_id = %s;"
        cursor.execute(query, (phone,account_id,))
        self.conn.commit()        
        return id;

    def updateRequesterEmail(self,id, email):
        cursor = self.conn.cursor() 
        query = "Select account_id from requester where requester_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0] 
        query = "update accounts set email = %s where account_id = %s;"
        cursor.execute(query, (email,account_id,))
        self.conn.commit()        
        return id;


    def updateRequesterFirst_name(self,id, name):
        cursor = self.conn.cursor() 
        query = "Select account_id from requester where requester_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set first_name = %s where account_id = %s;"
        cursor.execute(query, (name,account_id,))
        self.conn.commit()        
        return id;

    def updateRequesterLast_name(self,id, name):
        cursor = self.conn.cursor() 
        query = "Select account_id from requester where requester_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set last_name = %s where account_id = %s;"
        cursor.execute(query, (name,account_id,))
        self.conn.commit()        
        return id;