from dao.supplierDAO import SupplierDAO
from flask import jsonify
from datetime import datetime
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
        res = dao.searchSuppliersByID(id)
        if not res:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            result_list = []
            for row in res:
                result = self.build_supplier(row)
                result_list.append(result)          
        return jsonify(Supplier = result_list)

###################################################################
###########  POST

    def hash_password(self,password):
        # uuid is used to generate a random number
        salt =uuid.uuid3(uuid.NAMESPACE_DNS, 'proyect920.org').hex
        return hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def insertSupplier(self, form, parsed_json):
        first_name = form.get('first_name')  
        last_name = form.get('last_name')
        email = form.get('email')
        phone = form.get('phone')
        address = form.get('address')
        city_id = form.get('city_id')
        latitude = form.get('latitude')
        longitud = form.get('longitud')   
        password = form.get('password')
        dt = datetime.now()  
        photo_url = 'https://robohash.org/quiautdolores.png?size=50x50&set=set1'

        if len(form)==0:
            # parsed_json = json.loads(test)
            first_name = parsed_json['first_name']  
            last_name = parsed_json['last_name']
            email = parsed_json['email']
            phone = parsed_json['phone']
            address = parsed_json['address']
            city_id = parsed_json['city_id']
            latitude = parsed_json['latitude']
            longitud = parsed_json['longitud']   
            password = parsed_json['password']
            #Hash password
            password = self.hash_password(password)
            dao = SupplierDAO()
            id = dao.addSupplier(first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url , 'Supplier' , password,dt)
            result = self.getSupplierByID(id)
            return (result), 201     
                
        if first_name and last_name and email and phone and address and city_id and latitude and longitud and password :
            dao = SupplierDAO()
            password = self.hash_password(password)
            id = dao.addSupplier(first_name , last_name , email , phone , address , city_id , latitude , longitud , 'https://robohash.org/quiautdolores.png?size=50x50&set=set1' , 'Supplier' , password,dt)
            result = self.getSupplierByID(id)
            return (result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


############################################################################
############ UPDATE
#############################################################################


    def PutSupplier(self, form, parsed_json):
        first_name = form.get('first_name')  
        last_name = form.get('last_name')
        email = form.get('email')
        phone = form.get('phone')
        address = form.get('address')
        city_id = form.get('city_id')
        latitude = form.get('latitude')
        longitud = form.get('longitud')   
        photo = 'https://robohash.org/quiautdolores.png?size=50x50&set=set1'    
        id = form.get('id')

        if len(form)==0:
            id = parsed_json['id']
            first_name = parsed_json['first_name']  
            last_name = parsed_json['last_name']
            email = parsed_json['email']
            phone = parsed_json['phone']
            address = parsed_json['address']
            city_id = parsed_json['city_id']
            latitude = parsed_json['latitude']
            longitud = parsed_json['longitud']
            id = dao.UpdateSupplier(id,first_name , last_name , email , phone , address , city_id , latitude , longitud , photo)
            result = self.getSupplierByID(id)
            return (result), 201   
        
        elif first_name and last_name and email and phone and address and city_id and latitude and longitud and photo and id:
            dao = SupplierDAO()
            id = dao.UpdateSupplier(id,first_name , last_name , email , phone , address , city_id , latitude , longitud , photo)
            result = self.getSupplierByID(id)
            return (result), 201
        
        elif email and id and (len(form)==2):
            dao = SupplierDAO()
            tid = dao.updateSupplierEmail(id,email)
            result = self.getSupplierByID(id)
            return (result), 201

        elif phone and id and (len(form)==2):
            dao = SupplierDAO()
            tid = dao.updateSupplierPhone(id,phone)
            result = self.getSupplierByID(id)
            return (result), 201

        elif first_name and id and (len(form)==2):
            dao = SupplierDAO()
            tid = dao.updateSupplierFirst_name(id,first_name)
            result = self.getSupplierByID(id)
            return (result), 201

        elif last_name and id and (len(form)==2):
            dao = SupplierDAO()
            tid = dao.updateSupplierLast_name(id,last_name)
            result = self.getSupplierByID(id)
            return (result), 201    
        
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


       