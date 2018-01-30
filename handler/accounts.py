from dao.accountsDAO import AccountsDAO
from flask import jsonify
from datetime import datetime
import uuid
import hashlib
import json



class AccountHandler:
    
    def __init__(self):
            pass

     
    def hash_password(self,password):
        # uuid is used to generate a random number
        salt =uuid.uuid3(uuid.NAMESPACE_DNS, 'proyect920.org').hex
        return hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha1(salt.encode() + user_password.encode()).hexdigest()
    
    def build_admin(self,row):
        result = {}
        result['admin_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['city'] = row[5]
        return result

    def build_login(self,row):
        result = {}
        result['admin_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['city'] = row[5]
        result['type'] = row[6]
        return result

    def build_city(self,row):
        result = {}
        result['city_id'] = row[0]
        result['city_name'] = row[1]    
        return result

    def build_resource_type(self,row):
        result = {}
        result['resource_type_id'] = row[0]
        result['type_name'] = row[1]    
        return result

    def build_notifications(self,row):
        result = {}
        result['resource_id'] = row[0]
        result['name'] = row[1] 
        result['category'] = row[2]  
        result['tittle'] = row[3] 
        result['message'] = row[4] 
        result['date'] = row[5] 
        return result


    def getNotifications(self):
        dao = AccountsDAO()
        res = dao.notificationsList()
        result_list = []
        for row in res:
            result = self.build_notifications(row)
            result_list.append(result)                 
        return jsonify(Notifications = result_list)

    def getCities(self):
        dao = AccountsDAO()
        res = dao.cityList()
        result_list = []
        for row in res:
            result = self.build_city(row)
            result_list.append(result)                 
        return jsonify(Cities = result_list)

    def getResourceType(self):
        dao = AccountsDAO()
        res = dao.resource_typeList()
        result_list = []
        for row in res:
            result = self.build_resource_type(row)
            result_list.append(result)                 
        return jsonify(Resource_Type = result_list)

        

    def getAllAdmin(self):
        dao = AccountsDAO()
        res = dao.getAllAdmin()
        result_list = []
        
        if len(res) == 0:
            return jsonify(Error = "No Admin found"), 404
        else:
            for row in res:
                result = self.build_admin(row)
                result_list.append(result)            
            return jsonify(Administrator = result_list)

    def getAdminByID(self,id):
        dao = AccountsDAO()
        res = dao.searchAdminByID(id)
        if not res:
            return jsonify(Error = "Admin Not Found"), 404
        else:
            result_list = []
            for row in res:
                result = self.build_admin(row)
                result_list.append(result)            
            return jsonify(Administrator = result_list)

    def userLogin(self, form):
        email = form.get('email')
        password = form.get('password')
        
        if password and email:
            dao = AccountsDAO()
            password = self.hash_password(password)
            res = dao.accountLogin(email,password)
            if len(res)==0:
                return jsonify(Error = "No User Found with that email or Password " ),404
            else:
                result_list = []
            for row in res:
                result = self.build_login(row)
                result_list.append(result)            
                return jsonify(Administrator = result_list)       
        else:
            return jsonify(Error="Unexpected attributes in Login request"), 400

    def userChangePassword(self, form):
        email = form.get('email')
        password = form.get('password')        
        if password and email and (len(form)==2):
            dao = AccountsDAO()
            password = self.hash_password(password)
            res = dao.accountChangePassword(email,password) 
            return jsonify(Administrator = res)        
            
        else:
            return jsonify(Error="Unexpected attributes in Login request"), 400

    

            

###################################################################
###########  POST

   

    def insertAdmin(self, form, parsed_json):
        
        dt = datetime.now()       
        photo_url =  'https://robohash.org/quiautdolores.png?size=50x50&set=set1'
       
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
            dao = AccountsDAO()
            id = dao.addAdmin(first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url , 'Administrator' , password,dt)
            result = self.getAdminByID(id)
            return (result), 201
           

            
        else:
            first_name = form.get('first_name')  
            last_name = form.get('last_name')
            email = form.get('email')
            phone = form.get('phone')
            address = form.get('address')
            city_id = form.get('city_id')
            latitude = form.get('latitude')
            longitud = form.get('longitud')   
            password = form.get('password')
            
            if first_name and last_name and email and phone and address and city_id and latitude and longitud and photo_url and password :
                #Hash password
                password = self.hash_password(password)
                dao = AccountsDAO()
                id = dao.addAdmin(first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url , 'Administrator' , password,dt)
                result = self.getAdminByID(id)
                return (result), 201
            else:
                return jsonify(Error= parsed_json), 400
            
            #return jsonify(Error="Unexpected attributes in post request"), 400


############################################################################
############ UPDATE
#############################################################################


    def PutAdmin(self, form, test):
        first_name = form.get('first_name')  
        last_name = form.get('last_name')
        email = form.get('email')
        phone = form.get('phone')
        address = form.get('address')
        city_id = form.get('city_id')
        latitude = form.get('latitude')
        longitud = form.get('longitud')   
        photo_url = 'https://robohash.org/quiautdolores.png?size=50x50&set=set1'    
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
            id = dao.updateAdmin(id,first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url)
            result = self.getAdminByID(id)
            return (result), 201

        elif first_name and last_name and email and phone and address and city_id and latitude and longitud and photo_url :
            dao = AccountsDAO()
            tid = dao.updateAdmin(id,first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url)
            result = self.getAdminByID(tid)
            return (result), 201

        elif email and id and (len(form)==2):
            dao = AccountsDAO()
            tid = dao.updateAdminEmail(id,email)
            result = self.getAdminByID(tid)
            return  (result), 201

        elif phone and id and (len(form)==2):
            dao = AccountsDAO()
            tid = dao.updateAdminPhone(id,phone)
            result = self.getAdminByID(tid)
            return  (result), 201

        elif first_name and id and (len(form)==2):
            dao = AccountsDAO()
            tid = dao.updateAdminFirst_name(id,first_name)
            result = self.getAdminByID(tid)
            return  (result), 201

        elif last_name and id and (len(form)==2):
            dao = AccountsDAO()
            tid = dao.updateAdminLast_name(id,last_name)
            result = self.getAdminByID(tid)
            return  (result), 201    
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

        
       
