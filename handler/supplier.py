from dao.supplierDAO import SupplierDAO
from flask import jsonify



class SupplierHandler:
    
    def __init__(self):
            pass
    
    def build_supplier(self,row):
        result = {}
        result['supplier_id'] = row[0]
        result['first_name'] = row[1]
        result['list_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['city'] = row[5]
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        res = dao.getAllSuppliers()
        result_list = []
        
        if len(res) == 0:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            for row in res:
                result = self.build_supplier(row)
                result_list.append(result)            
            return jsonify(Suppliers = result_list)
    
    def searchAllSuppliersByParameter(self, args):
        dao = SupplierDAO()
        city = args.get('city')
        region = args.get('region')
        if len(args) == 1 and city:
            res = dao.searchSuppliersByCity(city)
        elif len(args) == 1 and region:
            res = dao.searchSuppliersByRegion(region)
        else:
            return jsonify(Error = "Malformed query string"), 400

        if len(res) == 0:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in res:
                result = self.build_supplier(row)
                result_list.append(result)            
            return jsonify(Suppliers = result_list)

    def getSupplierByID(self,id):
        dao = SupplierDAO()
        row = dao.searchSuppliersByID(id)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            part = self.build_supplier(row)
            return jsonify(Suppliert = part)