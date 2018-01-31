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
        result['resource_name'] = row[2]
        result['description'] = row[3]
        result['quantity'] = row[4]
        result['purchase_price'] = row[5]
        result['purchase_date'] = row[6]
        result['buyer_id'] = row[7]
        result['buyer_first_name'] = row[8]
        result['buyer_last_name'] = row[9]
        result['supplier_id'] = row[10]
        result['supplier_first_name'] = row[11]
        result['supplier_last_name'] = row[12]
        result['buyer_city_name'] = row[13]
        result['buyer_region_name'] = row[14]
        return result

    # METHODS

    # For updating a current payment method for a particular account id.
    def updatePaymentMethod(self, args, parsed_json):
        if len(args) == 0:
            cardHolder = parsed_json['card_holder']
            cardNumber = parsed_json['card_number']
            expDate = parsed_json['expiration_date']
            zipCode = parsed_json['zip_code']
            accountId = parsed_json['accountid']
            pmid = parsed_json['payment_method_id']
        else:
            cardHolder = args.get("card_holder")
            cardNumber = args.get("card_number")
            expDate = args.get("expiration_date")
            zipCode = args.get("zip_code")
            accountId = args.get("accountid")
            pmid = args.get("payment_method_id")

        if cardHolder and cardNumber and expDate and zipCode and accountId and pmid:
            dao = TransactionDAO()
            res = dao.addPaymentMethod(cardHolder, cardNumber, expDate, zipCode, accountId)
            if isinstance(res, int):
                result = {}
                result['payment_method_id'] = pmid
                result['card_holder'] = cardHolder
                result['card_number'] = cardNumber
                result['expiration_date'] = expDate
                result['zip_code'] = zipCode
                return jsonify(PaymentMethod = result)
                 
            else:
                return jsonify(Error=res)
        else:
            return jsonify(Error="Malformed post request")

    # Add payment method for a particular account id.
    def addPaymentMethod(self, args, parsed_json):
        if len(args) == 0:
            cardHolder = parsed_json['card_holder']
            cardNumber = parsed_json['card_number']
            expDate = parsed_json['expiration_date']
            zipCode = parsed_json['zip_code']
            accountId = parsed_json['accountid']
        else:
            cardHolder = args.get("card_holder")
            cardNumber = args.get("card_number")
            expDate = args.get("expiration_date")
            zipCode = args.get("zip_code")
            accountId = args.get("accountid")

        if cardHolder and cardNumber and expDate and zipCode and accountId:
            dao = TransactionDAO()
            pmid = dao.addPaymentMethod(cardHolder, cardNumber, expDate, zipCode, accountId)
            if isinstance(pmid, int):
                result = {}
                result['payment_method_id'] = pmid
                result['card_holder'] = cardHolder
                result['card_number'] = cardNumber
                result['expiration_date'] = expDate
                result['zip_code'] = zipCode
                return jsonify(PaymentMethod = result)
            else:
                return jsonify(Error=pmid)
        else:
            return jsonify(Error="Malformed post request")




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
        requesterId = args.get("requesterid")
        region = args.get("region")
        city = args.get("city")
        dao = TransactionDAO()

        transactionsList = []
        if(len(args) == 2 and requesterId and region):
            transactionsList = dao.getTransactionByBuyerIdAndRegion(requesterId, region)
        elif(len(args) == 2 and requesterId and city):
            transactionsList = dao.getTransactionByBuyerIdAndCity(requesterId, city)
        elif(len(args) == 1 and requesterId):
            transactionsList = dao.getTransactionByBuyerId(requesterId)
        else:
            return jsonify(Error = "Malfored query string"), 400

        result_list = []
        for row in transactionsList:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    # Get transaction history of certain supplier by the id.
    def getTransactionBySupplier(self, args):
        supplierId = args.get("supplierid")
        region = args.get("region")
        city = args.get("city")
        dao = TransactionDAO()

        transactionsList = []
        if (len(args) == 2 and supplierId and region):
            transactionsList = dao.getTransactionBySupplierIdAndRegion(supplierId, region)
        elif (len(args) == 2 and supplierId and city):
            transactionsList = dao.getTransactionBySupplierIdAndCity(supplierId, city)
        elif (len(args) == 1 and supplierId):
            transactionsList = dao.getTransactionBySupplierId(supplierId)
        else:
            return jsonify(Error="Malfored query string"), 400

        result_list = []
        for row in transactionsList:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)


    # Get transaction history of certain buyer by the id.
    def getTransactionByResource(self, args):
        resourceId = args.get("resourceid")
        resourceName = args.get("resourcename")
        dao = TransactionDAO()

        transactionsList = []
        if(len(args) == 1 and resourceId):
            transactionsList = dao.getTransactionByResourceId(resourceId)
        elif(len(args) == 1 and resourceName):
            transactionsList = dao.getTransactionByResourceName(resourceName)
        else:
            return jsonify(Error = "Malfored query string"), 400

        result_list = []
        for row in transactionsList:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    # Buy resource transaction.
    def buyResource(self, args, parsed_json):
        if len(args) == 0:
            resourceId = parsed_json['resourceid']
            requesterId = parsed_json['requesterid']
            purchaseQty = parsed_json['purchaseqty']
        else:
            resourceId = args.get("resourceid")
            requesterId = args.get("requesterid")
            purchaseQty = args.get("purchaseqty")

        if resourceId and requesterId and purchaseQty:
            dao = TransactionDAO()
            pid = dao.buyResource(purchaseQty, resourceId, requesterId)
            if isinstance(pid, int):
                result = {}
                result["purchase_id"] = pid
                result["resource_id"] = resourceId
                result["requester_id"] = requesterId
                result["purchase_qty"] = purchaseQty
                return jsonify(Transaction=result)
            else:
                return jsonify(Error=pid)
        else:
            return jsonify(Error="Malformed post request")







