from flask import jsonify
from dao.transactionDAO import TransactionDAO


class TransactionHandler:

    # CHANGE FROM ARRAY TO DICTIONARY

    def build_paymentMethod_dict(self, row):
        result = {}
        result['payment_method_id'] = row[0]
        result['card_holder'] = row[1]
        result['card_number'] = row[2]
        result['expiration_date'] = row[3]
        result['zip_code'] = row[4]
        return result

    def build_transaction_dict(self, row):
        result = {}
        result['purchase_id'] = row[0]
        result['resource_id'] = row[1]
        result['description'] = row[2]
        result['quantity'] = row[3]
        result['purchase_price'] = row[4]
        result['purchase_date'] = row[5]
        return result

    # METHODS

    # Get all payment method for a particular account id.
    def getPaymentMethods(self, args):
        accountId = args.get("accountid")
        dao = TransactionDAO()

        paymentMethods = []
        if accountId:
            paymentMethods = dao.getPaymentMethods(accountId)
        else:
            return jsonify(Error = "Malfored query string"), 400

        result_list = []
        for row in paymentMethods:
            result = self.build_paymentMethod_dict(row)
            result_list.append(result)
        return jsonify(PaymentMethods=result_list)

    # Get transaction history of certain buyer by the id.
    def getTransactionByBuyer(self, args):
        accountId = args.get("accountid")
        region = args.get("region")
        city = args.get("city")
        dao = TransactionDAO

        transactionsList = []
        if(len(args) == 2 and accountId and region):
            transactionsList = dao.getTransactionByBuyerIdAndRegion(accountId, region)
        elif(len(args) == 2 and accountId and city):
            transactionsList = dao.getTransactionByBuyerIdAndCity(accountId, city)
        elif(len(args) == 1 and accountId):
            transactionsList = dao.getTransactionByBuyerId(accountId)
        else:
            return jsonify(Error = "Malfored query string"), 400

        result_list = []
        for row in transactionsList:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=transactionsList)

    # Get transaction history of certain supplier by the id.
    def getTransactionBySupplier(self, args):
        accountId = args.get("accountid")
        region = args.get("region")
        city = args.get("city")
        dao = TransactionDAO

        transactionsList = []
        if (len(args) == 2 and accountId and region):
            transactionsList = dao.getTransactionBySupplierIdAndRegion(accountId, region)
        elif (len(args) == 2 and accountId and city):
            transactionsList = dao.getTransactionBySupplierIdAndCity(accountId, city)
        elif (len(args) == 1 and accountId):
            transactionsList = dao.getTransactionBySupplierId(accountId)
        else:
            return jsonify(Error="Malfored query string"), 400

        result_list = []
        for row in transactionsList:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=transactionsList)

