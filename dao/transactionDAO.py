import json
import psycopg2
import datetime
from flask import jsonify


class TransactionDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable',hostaddr='35.196.249.53')

    # Get all payment method for a particular account id.
    def getPaymentMethods(self, accountId):
        cursor = self.conn.cursor()
        query = "select payment_method_id, card_holder, card_number," \
                " expiration_date, zip_code" \
                " from accounts natural inner join payment_method" \
                " where account_id = %s;"
        cursor.execute(query, (accountId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # For updating an old payment method for a particular account id.
    def updatePaymentMethod(self, cardHolder, cardNumber, expirationDate, zipCode, accountId, pmid):
        cursor = self.conn.cursor()

        # Check if the account id exist
        query0 = "select * from accounts" \
                 " where account_id = %s;"
        cursor.execute(query0, (accountId,))
        result = []
        for row in cursor:
            result.append(row)

        if len(result) != 0:
            query = "update payment_method" \
                    " set card_holder = %s, card_number = %s, expiration_date = %s," \
                    " zip_code = %s" \
                    " where account_id = %s and payment_method_id = %s"
            cursor.execute(query, (cardHolder, cardNumber, expirationDate, zipCode, accountId))
            self.conn.commit()
            return pmid
        else:
            return "The account id doesnt exist."

    # For adding a new payment method for a particular account id.
    def addPaymentMethod(self, cardHolder, cardNumber, expirationDate, zipCode, accountId):
        cursor = self.conn.cursor()

        # Check if the account id exist
        query0 = "select * from accounts" \
                " where account_id = %s;"
        cursor.execute(query0, (accountId,))
        result = []
        for row in cursor:
            result.append(row)

        if len(result) != 0:
            query = "insert into payment_method(card_holder, card_number," \
                    " expiration_date, zip_code, account_id)" \
                   " values(%s, %s, %s, %s, %s) returning payment_method_id;"
            cursor.execute(query, (cardHolder, cardNumber, expirationDate, zipCode, accountId))
            pmid = cursor.fetchone()[0]
            self.conn.commit()
            return pmid
        else:
            return "The account id doesnt exist."

    # For Buyers when they going to buy a resource from a supplier.
    def buyResource(self, purchaseQty, resourceId, requesterId):

        # Check if the resource is available.
        cursor = self.conn.cursor()
        query1 = "select resource_name, availability, price" \
                 " from resources where resource_id = %s;"
        cursor.execute(query1, (resourceId,))
        result1 = []
        for row in cursor:
            result1.append(row)
        resourceName = result1[0][0]
        rAvailable = result1[0][1]
        purchasePrice = result1[0][2]
        print(resourceName, " ---> available: ", rAvailable
              , " Requesting: ", purchaseQty)

        if int(purchaseQty) <= int(rAvailable):
            # Check that the requester id exist
            query0 = "select * from requester" \
                     " where requester_id = %s;"
            cursor.execute(query0, (requesterId,))
            result0 = []
            for row in cursor:
                result0.append(row)
            if len(result0) != 0:
                # Look for the latest payment method of the requester
                query2 = "select payment_method_id" \
                        " from payment_method natural inner join requester" \
                        " where requester_id = %s" \
                        " order by payment_method_id desc;"
                cursor.execute(query2, (requesterId,))
                result2 = []
                for row in cursor:
                   result2.append(row)

                if len(result2) != 0:
                    paymentMethodId = result2[0][0]
                    print("requester id: ", requesterId, " payment method id:", paymentMethodId)

                    # If there is sufficient resources to buy, update the resource table.
                    difQuantity = int(rAvailable) - int(purchaseQty)
                    print("Remaining resources after buy: ", difQuantity)
                    query3 = "update resources" \
                          " set availability = %s" \
                           " where resource_id = %s;"
                    cursor.execute(query3, (difQuantity, resourceId))
                    self.conn.commit()

                    # Set purchases values.
                    purchaseDate = datetime.date.today()
                    print("Purchase date: ", purchaseDate, " purchase price: ", purchasePrice)
                    query4 = "insert into purchases(resource_id, requester_id, " \
                         "purchase_quantity, payment_method_id, purchase_date, " \
                       "purchase_price)" \
                      "values(%s, %s, %s, %s, %s, %s) returning purchase_id;"
                    cursor.execute(query4, (resourceId, requesterId, purchaseQty, paymentMethodId, purchaseDate, purchasePrice))
                    pid = cursor.fetchone()[0]
                    print("Generated Purchase id: ", pid)
                    self.conn.commit()
                    return pid
                else:
                    errorLog = "The requester do not have a payment method set."
                    print(errorLog)
                    return errorLog
            else:
                errorLog = "The requester id do not exist."
                print(errorLog)
                return errorLog
        else:
            errorLog = "There is no sufficient resources to buy."
            print(errorLog)
            return errorLog

    # Get all transactions
    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id order by purchase_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain buyer by the id.
    def getTransactionByBuyerId(self, requesterId):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id and requester_id = %s order by purchase_id;"
        cursor.execute(query, (requesterId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain buyer by the id and by region.
    def getTransactionByBuyerIdAndRegion(self, requesterId, region):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id" \
                " and requester_id = %s and region_name = %s order by purchase_id;"
        cursor.execute(query, (requesterId, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain buyer by the id and by city.
    def getTransactionByBuyerIdAndCity(self, requesterId, city):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id" \
                " and requester_id = %s and city_name = %s order by purchase_id;"
        cursor.execute(query, (requesterId, city))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id.
    def getTransactionBySupplierId(self, supplierId):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id and supplier_id = %s order by purchase_id;"
        cursor.execute(query, (supplierId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id and by region.
    def getTransactionBySupplierIdAndRegion(self, supplierId, region):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id" \
                " and supplier_id = %s and region_name = %s order by purchase_id;"
        cursor.execute(query, (supplierId, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of certain supplier by the id and by city.
    def getTransactionBySupplierIdAndCity(self, supplierId, city):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id" \
                " and supplier_id = %s and city_name = %s order by purchase_id;"
        cursor.execute(query, (supplierId, city))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of a certain resource id
    def getTransactionByResourceId(self, resourceId):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id and B.resource_id = %s order by purchase_id;"
        cursor.execute(query, (resourceId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transaction history of a certain resource name
    def getTransactionByResourceName(self, resourceName):
        cursor = self.conn.cursor()
        query = "select B.purchase_id, B.resource_id, B.resource_name, B.description, B.purchase_quantity, " \
                "B.purchase_price, B.purchase_date, B.requester_id, " \
                "B.first_name, B.last_name, B.supplier_id, S.sfn, S.sln, city_name, region_name " \
                "from (select * from " \
                "purchases natural inner join resources natural inner join accounts " \
                "natural inner join requester natural inner join location " \
                "natural inner join city natural inner join region) as B, " \
                "(select resource_id, first_name as sfn, last_name as sln " \
                "from resources natural inner join accounts " \
                "natural inner join supplier) as S " \
                "where B.resource_id = S.resource_id and B.resource_name = %s order by purchase_id;"
        cursor.execute(query, (resourceName,))
        result = []
        for row in cursor:
            result.append(row)
        return result
