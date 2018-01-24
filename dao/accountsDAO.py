import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config

class AccountsDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable', hostaddr='35.196.249.53')

    def getAllAdmin(self):
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Administrator';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchAdminByID(self,id):
        cursor = self.conn.cursor()
        query = "select admin_id , first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join administrator where admin_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def accountLogin(self, email,password):
        cursor = self.conn.cursor()
        query = "select account_id , first_name, last_name, email, phone, city_name from accounts natural inner join city natural inner join location where email = %s and password = %s;"
        cursor.execute(query, (email,password,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def accountChangePassword(self, email,password):
        cursor = self.conn.cursor()
        query = "update accounts set password =%s  where email = %s;"
        cursor.execute(query, (password,email))
        self.conn.commit()
        return'Password as been change'
        
       
         
#########################################################################
####  INSERT
############################################################################




    def addAdmin(self, first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url , account_type , password, dt):
        cursor = self.conn.cursor()       
        query = "insert into location (address, city_id, latitude, longitude) values (%s, %s, %s, %s ) returning location_id;"
        cursor.execute(query, ( address,city_id,latitude, longitud,))
        location_id = cursor.fetchone()[0]
        query = "insert into accounts (first_name , last_name , email , phone , location_id , photo_url , account_type , creation_date, password) values (%s, %s, %s, %s, %s, %s, %s, %s, %s ) returning account_id;"
        cursor.execute(query, (first_name , last_name , email , phone , location_id , photo_url , account_type , dt, password,))
        account_id = cursor.fetchone()[0]
        query = "insert into administrator (account_id) values (%s) returning admin_id;"
        cursor.execute(query, ( account_id,))
        id = cursor.fetchone()[0]
        self.conn.commit()
        return id;


#########################################################################
####  Update
############################################################################

    def updateAdmin(self,id,first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url):
        cursor = self.conn.cursor() 
        query = "Select account_id from administrator where admin_id = %s;"
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


    def updateAdminPhone(self,id, phone):
        cursor = self.conn.cursor() 
        query = "Select account_id from administrator where admin_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set phone  = %s where account_id = %s;"
        cursor.execute(query, (phone,account_id))
        self.conn.commit()        
        return id;

    def updateAdminEmail(self,id, email):
        cursor = self.conn.cursor() 
        query = "Select account_id from administrator where admin_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set email = %s where account_id = %s;"
        cursor.execute(query, (email,account_id,))
        self.conn.commit()        
        return id;


    def updateAdminFirst_name(self,id, name):
        cursor = self.conn.cursor() 
        query = "Select account_id from administrator where admin_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set first_name = %s where account_id = %s;"
        cursor.execute(query, (name,account_id,))
        self.conn.commit()        
        return id;

    def updateAdminLast_name(self,id, name):
        cursor = self.conn.cursor() 
        query = "Select account_id from administrator where admin_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]  
        query = "update accounts set last_name = %s where account_id = %s;"
        cursor.execute(query, (name,account_id))
        self.conn.commit()        
        return id;