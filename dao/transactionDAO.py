import json
import psycopg2
from flask import jsonify


class TransactionDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable',hostaddr='35.196.249.53')

    # Get all payment method for a particular account id.
    def getPaymentMethods(self, accountId):
        cursor = self.conn.cursor()
        query = "select payment_method_id, card_holder, card_number, expiration_date, zip_code from accounts natural inner join payment_method where account_id = %s;"
        cursor.execute(query, (accountId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # For adding a new payment method for a particular account id.
    def addPaymentMethod(self, cardHolder, cardNumber, expirationDate, zipCode, accountId):
        cursor = self.conn.cursor()
        query = "insert into payment_method(card_holder, card_number, expiration_date, zip_code, account_id) values('%s', '%s', '%s', '%s', %s);"
        cursor.execute(query, (cardHolder, cardNumber, expirationDate, zipCode, accountId))
        pmid = cursor.fetchone()[0]
        self.conn.commit()
        return pmid

    # For Buyers when they going to buy a resource from a supplier.
    def buyResources(self, quantity, purchaseDate, paymentMethodId, resourceId, accountId):
        cursor = self.conn.cursor()
        query = "insert into purchases(quantity, purchase_date, payment_method_id, resource_id, account_id) values(%s, '%s', %s, %s, %s);"
        cursor.execute(query, (quantity, purchaseDate, paymentMethodId, resourceId, accountId))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    # Get transaction history of certain buyer by the id.
    def getTransactionByBuyerId(self, accountId):
        cursor = self.conn.cursor()
        query = "select purchase_id, resource_id, resource_name, description, quantity, purchase_price, purchase_date from purchases natural inner join accounts natural inner join resources where account_id = %s and account_type = 'Requester';"
        cursor.execute(query, (accountId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain buyer by the id and by region.
    def getTransactionByBuyerIdAndRegion(self, accountId, region):
        cursor = self.conn.cursor()
        query = "select purchase_id, resource_id, resource_name, description, quantity, purchase_price, purchase_date from purchases natural inner join accounts natural inner join resources natural inner join location natural inner join city natural inner join region where account_id = %s and region_name = '%s';"
        cursor.execute(query, (accountId, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain buyer by the id and by city.
    def getTransactionByBuyerIdAndCity(self, accountId, city):
        cursor = self.conn.cursor()
        query = "select purchase_id, resource_id, resource_name, description, quantity, purchase_price, purchase_date from purchases natural inner join accounts natural inner join resources natural inner join location natural inner join city where account_id = %s and city_name = '%s';"
        cursor.execute(query, (accountId, city))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id.
    def getTransactionBySupplierId(self, accountId):
        cursor = self.conn.cursor()
        query = "select purchase_id, resource_id, resource_name, description, quantity, purchase_price, purchase_date from purchases natural inner join accounts natural inner join resources where account_id = %s and account_type = 'Supplier';"
        cursor.execute(query, (accountId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id and by region.
    def getTransactionBySupplierIdAndRegion(self, accountId, region):
        cursor = self.conn.cursor()
        query = "select purchase_id, resource_id, resource_name, description, quantity, purchase_price, purchase_date from purchases natural inner join accounts natural inner join resources natural inner join location natural inner join city natural inner join region where account_id = %s and region_name = '%s';"
        cursor.execute(query, (accountId, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id and by city.
    def getTransactionBySupplierIdAndCity(self, accountId, city):
        cursor = self.conn.cursor()
        query = "select purchase_id, resource_id, resource_name, description, quantity, purchase_price, purchase_date from purchases natural inner join accounts natural inner join resources natural inner join location natural inner join city where account_id = %s and city_name = '%s';"
        cursor.execute(query, (accountId, city))
        result = []
        for row in cursor:
            result.append(row)
        return result

