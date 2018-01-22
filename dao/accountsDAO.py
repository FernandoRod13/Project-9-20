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
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join administrator where admin_id = %s;"
        cursor.execute(query, (id,))
        return cursor.fetchone()


    def accountLogin(self, email,password):
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join administrator where email = %s and password = %s;"
        cursor.execute(query, (email,password))
        return cursor.fetchone()
       

#########################################################################
####  INSERT
############################################################################


    def addAdminr(self, first_name , last_name , email , phone , address , city_id , latitude , longitud , photo , account_type , password, dt):
        cursor = self.conn.cursor()       
        query = "insert into location (address, city_id, latitude,longitud) values (%s, %s, %s, %s ) returning location_id;"
        cursor.execute(query, ( address,city_id,latitude, longitud,))
        location_id = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into resources(first_name , last_name , email , phone , location_id , photo , account_type , creation_date, password) values (%s, %s, %s, %s, %s, %s, %s, %s, %s ) returning account_id;"
        cursor.execute(query, (first_name , last_name , email , phone , location_id , photo , account_type , creation_date, password,))
        account_id = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into administrator (account_id) values (%s);"
        cursor.execute(query, ( account_id,))
        supplier_id = cursor.fetchone()[0]
        self.conn.commit()
        return supplier_id;



#########################################################################
####  Update
############################################################################


    def updateAdmin(self, id, first_name , last_name , email , phone , address , city_id , latitude , longitud , photo , account_type , password):
        cursor = self.conn.cursor() 
        query = "Select account_id from administrator where admin_id = %s;"
        cursor.execute(query, ( id,))
        account_id = cursor.fetchone()[0]            
        query = "update location set address = %s, city_id = = %s, latitude = %s ,longitud = %s where account_id = %s"
        cursor.execute(query, ( address,city_id,latitude, longitud,))
        location_id = cursor.fetchone()[0]
        self.conn.commit()
        query = "update resources(first_name = %s , last_name  = %s , email  = %s , phone = %s , location_id  = %s, photo  = %s, account_type  = %s, password  = %s) where account_id = %s;"
        cursor.execute(query, (first_name , last_name , email , phone , location_id , photo , account_type , creation_date, password,))
        account_id = cursor.fetchone()[0]
        self.conn.commit()        
        return id;


    def updateAdminPhone(id, phone):
        cursor = self.conn.cursor() 
        query = "update accounts set phone  = %s where account_id = %s;"
        cursor.execute(query, (phone,))
        account_id = cursor.fetchone()[0]
        self.conn.commit()        
        return id;

    def updateAdminEmail(id, email):
        cursor = self.conn.cursor() 
        query = "update accounts set email = %s where account_id = %s;"
        cursor.execute(query, (email,))
        account_id = cursor.fetchone()[0]
        self.conn.commit()        
        return id;


    def updateAdminFirst_name(id, name):
        cursor = self.conn.cursor() 
        query = "update accounts set first_name = %s where account_id = %s;"
        cursor.execute(query, (name,))
        account_id = cursor.fetchone()[0]
        self.conn.commit()        
        return id;

    def updateAdminLast_name(id, name):
        cursor = self.conn.cursor() 
        query = "update accounts set last_name = %s where account_id = %s;"
        cursor.execute(query, (name,))
        account_id = cursor.fetchone()[0]
        self.conn.commit()        
        return id;