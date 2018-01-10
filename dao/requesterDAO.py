import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config

class RequesterDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable', hostaddr='35.196.249.53')

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Requester';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersByCity(self,city):
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Requester' and city_name = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersByRegion(self,region):
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join region where account_type = 'Requester' and region_name = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequesterByID(self,id):
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Requester' and account_id = %s;"
        cursor.execute(query, (id,))
        return cursor.fetchone()

    def searchRequestersRequestingResource(self,resource_name):
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested where account_type = 'Requester' and requested_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersRequestingResourceByCategory(self, type_name):
        cursor = self.conn.cursor()
        if( type_name == 'fuel'):
            query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested natural inner join resource_type where account_type = 'Requester' and ( type_name = 'propane' or type_name = 'gasoline' or type_name = 'diesel');"
            cursor.execute(query)
        elif( type_name == 'water'):
            query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested natural inner join resource_type where account_type = 'Requester' and ( type_name = 'smallbottles' or type_name = 'gallonbottles' );"
            cursor.execute(query)
        else:
            query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested n  'atural inner join resource_type where account_type = 'Requester' and type_name = %s;"
            cursor.execute(query, (type_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersRequestingResourceInCity(self, resource_name, city):
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested where account_type = 'Requester' and requested_name = %s and city_name = %s;"
        cursor.execute(query, (resource_name, city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersByName(self, name): 
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Requester' and  (first_name = %s or last_name =%s);"
        cursor.execute(query, (name, name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestersByResourceKeyword(self,keyword):
        cursor = self.conn.cursor()
        query = "select account_id as requester_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources_requested natural inner join resource_keyword where account_type = 'Requester' and  keyword LIKE '%%' || %s || '%%';"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result
