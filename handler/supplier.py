from dao.supplierDAO import SupplierDAO
from flask import jsonify
import uuid
import hashlib



class SupplierHandler:
    
    def __init__(self):
            pass
    
    def build_supplier(self,row):
        result = {}
        result['supplier_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
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
        resource_name = args.get('resource_name')
        type_name = args.get('type_name')
        name = args.get('name')
        keyword = args.get('keyword')
        if len(args) == 1 and city:
            res = dao.searchSuppliersByCity(city)
        elif len(args) == 1 and region:
            res = dao.searchSuppliersByRegion(region)
        elif len(args) == 1 and resource_name:
            res = dao.searchSuppliersSupplyingResource(resource_name)
        elif len(args) == 1 and type_name:
            res = dao.searchSuppliersSupplyingResourceByCategory(type_name)
        elif len(args) == 1 and name:
            res = dao.searchSuppliersByName(name)
        elif len(args) == 1 and keyword:
            res = dao.searchSuppliersByResourceKeyword(keyword)
        elif len(args) == 2 and resource_name and city:
            res = dao.searchSuppliersSupplyingResourceInCity(resource_name, city)
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
            return jsonify(Supplier = part)

###################################################################
###########  POST

    def hash_password(self,password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def insertSupplier(self, form):
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']
        phone = form['phone']
        address = form['address']
        city_id = form['city_id']
        latitude = form['latitude']
        longitud = form['longitud']
        photo = 
        account_type = form['account_type']
        password = form['password']
        #Hash password
        password = self.hash_password(password)

        
        
       