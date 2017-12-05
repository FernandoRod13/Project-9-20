from dao.accountDAO import accountDAO
from flask import jsonify



class AccountHandler:
    
    def __init__(self):
            pass
        
    # Account verification
    def verifyAccount(self,args):
        dao = accountDAO()
        accountid = args.get("accountid")
        accountpass= args.get("accountpass")
        if (len(args)==2) and accountid and accountpass:
            res = dao.verifyAccount(accountid,accountpass)
        else:
            res =  "Malformed query string", 400
        return jsonify(Account = res)
    # Account data
    def getAccountData(self,args):
        accountid = args.get("accountid")
        if len(args)==1 and accountid:
            dao = accountDAO()
            res = dao.getSuppliers()
            return jsonify(Suppliers = res)
        else: 
            res = "Malformed query string", 400
            return jsonify(Account = res)
    #suppliers
    def getAllSuppliers(self):
        dao = accountDAO()
        res = dao.getSuppliers()
        return jsonify(Suppliers = res)

    def getAllSuppliersInCity(self, args):
        city = args.get("city")
        dao = accountDAO()
        if len(args)==1 and city:
            res = dao.getSuppliers()
            return jsonify(Suppliers = res)
        else:
            res = "Malformed query string", 400
            return jsonify(Account = res)
    