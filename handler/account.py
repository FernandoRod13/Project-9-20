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
        return jsonify(Resource = res)
    