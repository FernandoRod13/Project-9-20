from flask import jsonify
import json

class accountDAO:
    
    def __init__(self):
        self.conn = psycopg2.connect(database='project920', user='natalia', password='none', sslmode='disable',hostaddr='35.196.249.53')
    
      # Account verification
    def verifyAccount(self, accountid, accountpass):
        cursor = self.conn.cursor()
        query = "select * from Accounts where account_ID = %s and password = %s;"
        cursor.execute(query, accountid, accountpass)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from Accounts where account_type='supplier"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersbyCity(self,city):
        cursor = self.conn.cursor()
        query = "select * from Accounts natural inner join Location natural inner join City where city_name = %s;"
        cursor.execute(query, city)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequester(self):
        cursor = self.conn.cursor()
        query = "select * from Resources_Requested natural inner Accounts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterByCity(self,city):
        cursor = self.conn.cursor()
        query = "select * from Resources_Requested natural inner Accounts natural inner join Location natural inner join City where city_name = %s;"
        cursor.execute(query, city)
        result = []
        for row in cursor:
            result.append(row)
        return result