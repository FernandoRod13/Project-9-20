import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config

class SupplierDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable', hostaddr='35.196.249.53')

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Supplier';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByCity(self,city):
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Supplier' and city_name = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByRegion(self,region):
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join region where account_type = 'Supplier' and region_name = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByID(self,id):
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Supplier' and account_id = %s;"
        cursor.execute(query, (id,))
        return cursor.fetchone()

    def searchSuppliersSupplyingResource(self,resource_name):
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources where account_type = 'Supplier' and resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersSupplyingResourceByCategory(self, type_name):
        cursor = self.conn.cursor()
        if (type_name == 'fuel'):
            query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources natural inner join resource_type where account_type = 'Supplier' and (type_name = 'gasoline' OR type_name = 'propane' OR type_name = 'diesel') ;"
            cursor.execute(query)
        elif (type_name == 'water'):
            query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources natural inner join resource_type where account_type = 'Supplier' and (type_name = 'gallonbottles' OR type_name = 'smallbottles' ) ;"
            cursor.execute(query)
        else:
            query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources natural inner join resource_type where account_type = 'Supplier' and type_name = %s;"
            cursor.execute(query, (type_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersSupplyingResourceInCity(self, resource_name, city):
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources where account_type = 'Supplier' and resource_name = %s and city_name = %s;"
        cursor.execute(query, (resource_name, city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByName(self, name): 
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city where account_type = 'Supplier' and  (first_name = %s or last_name =%s);"
        cursor.execute(query, (name, name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByResourceKeyword(self,keyword):
        cursor = self.conn.cursor()
        query = "select account_id as supplier_id, first_name, last_name, email, phone, city_name from accounts natural inner join location natural inner join city natural inner join resources natural inner join resource_keyword where account_type = 'Supplier' and  keyword LIKE '%%' || %s || '%%';"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result
