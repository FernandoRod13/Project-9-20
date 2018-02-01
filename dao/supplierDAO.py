import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config

class SupplierDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable', hostaddr='35.196.249.53')

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select supplier_id , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier where account_type = 'Supplier';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByCity(self,city):
        cursor = self.conn.cursor()
        query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier  where account_type = 'Supplier' and city_name = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByRegion(self,region):
        cursor = self.conn.cursor()
        query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier natural inner join region where account_type = 'Supplier' and region_name = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByID(self,id):
        cursor = self.conn.cursor()
        query = "select supplier_id , first_name, last_name, email, phone, city_name  from accounts natural inner join location natural inner join city natural inner join supplier  where account_type = 'Supplier' and supplier_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersSupplyingResource(self,resource_name):
        cursor = self.conn.cursor()
        query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier natural inner join resources where account_type = 'Supplier' and resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersSupplyingResourceByCategory(self, type_name):
        cursor = self.conn.cursor()
        if (type_name == 'fuel'):
            query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier natural inner join resources natural inner join resource_type  where account_type = 'Supplier' and (type_name = 'gasoline' OR type_name = 'propane' OR type_name = 'diesel') ;"
            cursor.execute(query)
        elif (type_name == 'water'):
            query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier natural inner join resources natural inner join resource_type  where account_type = 'Supplier' and (type_name = 'gallonbottles' OR type_name = 'smallbottles' ) ;"
            cursor.execute(query)
        else:
            query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier natural inner join resources natural inner join resource_type  where account_type = 'Supplier' and type_name = %s;"
            cursor.execute(query, (type_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersSupplyingResourceInCity(self, resource_name, city):
        cursor = self.conn.cursor()
        query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier natural inner join resources where account_type = 'Supplier' and resource_name = %s and city_name = %s;"
        cursor.execute(query, (resource_name, city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByName(self, name): 
        cursor = self.conn.cursor()
        query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier where account_type = 'Supplier' and  (first_name = %s or last_name =%s);"
        cursor.execute(query, (name, name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByResourceKeyword(self,keyword):
        cursor = self.conn.cursor()
        query = "select supplier_id  , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join supplier natural inner join resources natural inner join resource_keyword where account_type = 'Supplier' and  keyword LIKE '%%' || %s || '%%';"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

#########################################################################
####  INSERT
############################################################################


    def addSupplier(self, first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url , account_type , password, dt):
        cursor = self.conn.cursor()       
        query = "insert into location (address, city_id, latitude, longitude) values (%s, %s, %s, %s ) returning location_id;"
        cursor.execute(query, ( address,city_id,latitude, longitud,))
        location_id = cursor.fetchone()[0]
        query = "insert into accounts (first_name , last_name , email , phone , location_id , photo_url , account_type , account_creation_date, password) values (%s, %s, %s, %s, %s, %s, %s, %s, %s ) returning account_id;"
        cursor.execute(query, (first_name , last_name , email , phone , location_id , photo_url , account_type , dt, password,))
        account_id = cursor.fetchone()[0]
        query = "insert into supplier (account_id) values (%s) returning supplier_id;"
        cursor.execute(query, ( account_id,))
        supplier_id = cursor.fetchone()[0]
        self.conn.commit()
        return supplier_id;



#########################################################################
####  Update
############################################################################


    def UpdateSupplier(self,id,first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url):
        cursor = self.conn.cursor() 
        query = "Select account_id from supplier where supplier_id = %s;"
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

    
    def updateSupplierPhone(self,id, phone):
        cursor = self.conn.cursor() 
        query = "Select account_id from supplier where supplier_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set phone  = %s where account_id = %s;"
        cursor.execute(query, (phone,account_id,))
        self.conn.commit()        
        return id;

    def updateSupplierEmail(self,id, email):
        cursor = self.conn.cursor() 
        query = "Select account_id from supplier where supplier_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set email = %s where account_id = %s;"
        cursor.execute(query, (email,account_id,))
        self.conn.commit()        
        return id;


    def updateSupplierFirst_name(self,id, name):
        cursor = self.conn.cursor() 
        query = "Select account_id from supplier where supplier_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set first_name = %s where account_id = %s;"
        cursor.execute(query, (name,account_id,))
        self.conn.commit()        
        return id;

    def updateSupplierLast_name(self,id, name):
        cursor = self.conn.cursor() 
        query = "Select account_id from supplier where supplier_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0] 
        query = "update accounts set last_name = %s where account_id = %s;"
        cursor.execute(query, (name,account_id,))
        self.conn.commit()        
        return id;