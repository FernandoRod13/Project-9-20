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
        query = "select T.purchase_id, T.resource_id, R.resource_name, " \
                "R.description, T.quantity, T.purchase_price, T.purchase_date, " \
                "T.account_id as buyer_id, T.first_name as buyer_first_name, T.last_name as buyer_last_name, " \
                "R.account_id as supplier_id, R.first_name as supplier_first_name, R.last_name as supplier_last_name, " \
                "T.city_name as buyer_city_name, T.region_name as buyer_region_name " \
                "from (select first_name, last_name, account_id, purchase_id, resource_id, " \
                "quantity, purchase_price, purchase_date, city_name, region_name " \
                "from purchases natural inner join accounts natural inner join location " \
                "natural inner join city natural inner join region) as T, " \
                "(select resource_id, resource_name, description, account_id, first_name, last_name " \
                "from accounts natural inner join resources) as R " \
                "where T.resource_id = R.resource_id " \
                "and T.account_id = %s;"
        cursor.execute(query, (accountId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain buyer by the id and by region.
    def getTransactionByBuyerIdAndRegion(self, accountId, region):
        cursor = self.conn.cursor()
        query = "select T.purchase_id, T.resource_id, R.resource_name, " \
                "R.description, T.quantity, T.purchase_price, T.purchase_date, " \
                "T.account_id as buyer_id, T.first_name as buyer_first_name, T.last_name as buyer_last_name, " \
                "R.account_id as supplier_id, R.first_name as supplier_first_name, R.last_name as supplier_last_name, " \
                "T.city_name as buyer_city_name, T.region_name as buyer_region_name " \
                "from (select first_name, last_name, account_id, purchase_id, resource_id, " \
                "quantity, purchase_price, purchase_date, city_name, region_name " \
                "from purchases natural inner join accounts natural inner join location " \
                "natural inner join city natural inner join region) as T, " \
                "(select resource_id, resource_name, description, account_id, first_name, last_name " \
                "from accounts natural inner join resources) as R " \
                "where T.resource_id = R.resource_id " \
                "and T.account_id = %s and T.region_name = %s;"
        cursor.execute(query, (accountId, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain buyer by the id and by city.
    def getTransactionByBuyerIdAndCity(self, accountId, city):
        cursor = self.conn.cursor()
        query = "select T.purchase_id, T.resource_id, R.resource_name, " \
                "R.description, T.quantity, T.purchase_price, T.purchase_date, " \
                "T.account_id as buyer_id, T.first_name as buyer_first_name, T.last_name as buyer_last_name, " \
                "R.account_id as supplier_id, R.first_name as supplier_first_name, R.last_name as supplier_last_name, " \
                "T.city_name as buyer_city_name, T.region_name as buyer_region_name " \
                "from (select first_name, last_name, account_id, purchase_id, resource_id, " \
                "quantity, purchase_price, purchase_date, city_name, region_name " \
                "from purchases natural inner join accounts natural inner join location " \
                "natural inner join city natural inner join region) as T, " \
                "(select resource_id, resource_name, description, account_id, first_name, last_name " \
                "from accounts natural inner join resources) as R " \
                "where T.resource_id = R.resource_id " \
                "and T.account_id = %s and T.city_name = %s;"
        cursor.execute(query, (accountId, city))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id.
    def getTransactionBySupplierId(self, accountId):
        cursor = self.conn.cursor()
        query = "select T.purchase_id, T.resource_id, R.resource_name, " \
                "R.description, T.quantity, T.purchase_price, T.purchase_date, " \
                "T.account_id as buyer_id, T.first_name as buyer_first_name, T.last_name as buyer_last_name, " \
                "R.account_id as supplier_id, R.first_name as supplier_first_name, R.last_name as supplier_last_name, " \
                "T.city_name as buyer_city_name, T.region_name as buyer_region_name " \
                "from (select first_name, last_name, account_id, purchase_id, resource_id, " \
                "quantity, purchase_price, purchase_date, city_name, region_name " \
                "from purchases natural inner join accounts natural inner join location " \
                "natural inner join city natural inner join region) as T, " \
                "(select resource_id, resource_name, description, account_id, first_name, last_name " \
                "from accounts natural inner join resources) as R " \
                "where T.resource_id = R.resource_id " \
                "and R.account_id = %s;"
        cursor.execute(query, (accountId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id and by region.
    def getTransactionBySupplierIdAndRegion(self, accountId, region):
        cursor = self.conn.cursor()
        query = "select T.purchase_id, T.resource_id, R.resource_name, " \
                "R.description, T.quantity, T.purchase_price, T.purchase_date, " \
                "T.account_id as buyer_id, T.first_name as buyer_first_name, T.last_name as buyer_last_name, " \
                "R.account_id as supplier_id, R.first_name as supplier_first_name, R.last_name as supplier_last_name, " \
                "T.city_name as buyer_city_name, T.region_name as buyer_region_name " \
                "from (select first_name, last_name, account_id, purchase_id, resource_id, " \
                "quantity, purchase_price, purchase_date, city_name, region_name " \
                "from purchases natural inner join accounts natural inner join location " \
                "natural inner join city natural inner join region) as T, " \
                "(select resource_id, resource_name, description, account_id, first_name, last_name, " \
                "city_name, region_name " \
                "from accounts natural inner join resources " \
                "natural inner join location natural inner join city natural inner join region) as R " \
                "where T.resource_id = R.resource_id " \
                "and R.account_id = %s and R.region_name = %s;"
        cursor.execute(query, (accountId, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id and by city.
    def getTransactionBySupplierIdAndCity(self, accountId, city):
        cursor = self.conn.cursor()
        query = "select T.purchase_id, T.resource_id, R.resource_name, " \
                "R.description, T.quantity, T.purchase_price, T.purchase_date, " \
                "T.account_id as buyer_id, T.first_name as buyer_first_name, T.last_name as buyer_last_name, " \
                "R.account_id as supplier_id, R.first_name as supplier_first_name, R.last_name as supplier_last_name, " \
                "T.city_name as buyer_city_name, T.region_name as buyer_region_name " \
                "from (select first_name, last_name, account_id, purchase_id, resource_id, " \
                "quantity, purchase_price, purchase_date, city_name, region_name " \
                "from purchases natural inner join accounts natural inner join location " \
                "natural inner join city natural inner join region) as T, " \
                "(select resource_id, resource_name, description, account_id, first_name, last_name, " \
                "city_name, region_name " \
                "from accounts natural inner join resources " \
                "natural inner join location natural inner join city natural inner join region) as R " \
                "where T.resource_id = R.resource_id " \
                "and R.account_id = %s and R.city_name = %s;"
        cursor.execute(query, (accountId, city))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of a certain resource id
    def getTransactionByResourceId(self, resourceId):
        cursor = self.conn.cursor()
        query = "select T.purchase_id, T.resource_id, R.resource_name, " \
                "R.description, T.quantity, T.purchase_price, T.purchase_date, " \
                "T.account_id as buyer_id, T.first_name as buyer_first_name, T.last_name as buyer_last_name, " \
                "R.account_id as supplier_id, R.first_name as supplier_first_name, R.last_name as supplier_last_name, " \
                "T.city_name as buyer_city_name, T.region_name as buyer_region_name " \
                "from (select first_name, last_name, account_id, purchase_id, resource_id, " \
                "quantity, purchase_price, purchase_date, city_name, region_name " \
                "from purchases natural inner join accounts natural inner join location " \
                "natural inner join city natural inner join region) as T, " \
                "(select resource_id, resource_name, description, account_id, first_name, last_name " \
                "from accounts natural inner join resources) as R " \
                "where T.resource_id = R.resource_id " \
                "and R.resource_id = %s;"
        cursor.execute(query, (resourceId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of a certain resource name
    def getTransactionByResourceName(self, resourceName):
        cursor = self.conn.cursor()
        query = "select T.purchase_id, T.resource_id, R.resource_name, " \
                "R.description, T.quantity, T.purchase_price, T.purchase_date, " \
                "T.account_id as buyer_id, T.first_name as buyer_first_name, T.last_name as buyer_last_name, " \
                "R.account_id as supplier_id, R.first_name as supplier_first_name, R.last_name as supplier_last_name, " \
                "T.city_name as buyer_city_name, T.region_name as buyer_region_name " \
                "from (select first_name, last_name, account_id, purchase_id, resource_id, " \
                "quantity, purchase_price, purchase_date, city_name, region_name " \
                "from purchases natural inner join accounts natural inner join location " \
                "natural inner join city natural inner join region) as T, " \
                "(select resource_id, resource_name, description, account_id, first_name, last_name " \
                "from accounts natural inner join resources) as R " \
                "where T.resource_id = R.resource_id " \
                "and R.resource_name = %s;"
        cursor.execute(query, (resourceName,))
        result = []
        for row in cursor:
            result.append(row)
        return result