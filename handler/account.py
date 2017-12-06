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
    def getAllSuppliers(self,args):
        dao = accountDAO()
        city = args.get("city")
        email = args.get("email")
        name = args.get("name")
        phone = args.get("phone")
        
        dao = accountDAO()
        if len(args)== 0:
            res = dao.getSuppliers()
        elif len(args)==1 and city:
            res = dao.getSuppliersbyCity(city)
        elif email or name or phone:
            res = getSuppliers()
        else:
            res = "Malformed query string", 400
        return jsonify(Account = res)

    #Requester
    def getAllRequester(self,args):
        dao = accountDAO()
        city = args.get("city")
        email = args.get("email")
        name = args.get("name")
        phone = args.get("phone")
        dao = accountDAO()
        if len(args) == 0:
            res = dao.getRequester()
        elif len(args)==1 and city:
            res = dao.getRequesterByCity(city)
        elif email or name or phone:
            res = getRequester()
        else:
            res = "Malformed query string", 400
        return jsonify(Account = res)

       
     