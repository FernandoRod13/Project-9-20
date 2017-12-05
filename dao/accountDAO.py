from flask import jsonify


class accountDAO:
    
    def __init__(self):
        pass
    
      # Account verification
    def verifyAccount(self, accountid, accountpass):
        result = []
        result.append("This is to verify if account " + accountid + "is correct")
        return result

    