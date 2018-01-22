from dao.requesterDAO import RequesterDAO
from flask import jsonify

class RequesterHandler:
    
    def __init__(self):
            pass
    
    def build_requester(self,row):
        result = {}
        result['requester_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['city'] = row[5]
        return result

    def getAllRequesters(self):
        dao = RequesterDAO()
        res = dao.getAllRequester()
        result_list = []
        
        if len(res) == 0:
            return jsonify(Error = "No Requesters found"), 404
        else:
            for row in res:
                result = self.build_requester(row)
                result_list.append(result)            
            return jsonify(Requester = result_list)
    
    def searchAllRequestersByParameter(self, args):
        dao = RequesterDAO()
        city = args.get('city')
        region = args.get('region')
        resource_name = args.get('resource_name')
        type_name = args.get('type_name')
        name = args.get('name')
        keyword = args.get('keyword')
        if len(args) == 1 and city:
            res = dao.searchRequestersByCity(city)
        elif len(args) == 1 and region:
            res = dao.searchRequestersByRegion(region)
        elif len(args) == 1 and resource_name:
            res = dao.searchRequestersRequestingResource(resource_name)
        elif len(args) == 1 and type_name:
            res = dao.searchRequestersRequestingResourceByCategory(type_name)
        elif len(args) == 1 and name:
            res = dao.searchRequestersByName(name)
        elif len(args) == 1 and keyword:
            res = dao.searchRequestersByResourceKeyword(keyword)
        elif len(args) == 2 and resource_name and city:
            res = dao.searchRequestersRequestingResourcesInCity(resource_name, city)
        else:
            return jsonify(Error = "Malformed query string"), 400

        if len(res) == 0:
            return jsonify(Error = "No Requesters found"), 404
        else:
            result_list = []
            for row in res:
                result = self.build_requester(row)
                result_list.append(result)            
            return jsonify(Requester = result_list)

    def getRequesterByID(self,id):
        dao = RequesterDAO()
        row = dao.searchRequesterByID(id)
        if not row:
            return jsonify(Error = "Requester Not Found"), 404
        else:
            part = self.build_requester(row)
            return jsonify(Requester = part)


##################################################################
#############  Insert
########################################################################

    def hash_password(self,password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def insertRequester(self, form):
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']
        phone = form['phone']
        address = form['address']
        city_id = form['city_id']
        latitude = form['latitude']
        longitud = form['longitud']
        photo_url =  'https://robohash.org/quiautdolores.png?size=50x50&set=set1'
        password = form['password']
        dt = datetime.now()
        #Hash password
        password = self.hash_password(password)
        if first_name and last_name and email and phone and address and city_id and latitude and longitud and photo_url  and password :
            dao = RequesterDAO()
            pid = dao.addRequester(first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url , 'Requester' , password,dt)
            result = self.getRequesterByID(pid)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400



############################################################################
############ UPDATE
#############################################################################


    def PutRequester(self, form):
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']
        phone = form['phone']
        address = form['address']
        city_id = form['city_id']
        latitude = form['latitude']
        longitud = form['longitud']
        photo_url =  'https://robohash.org/quiautdolores.png?size=50x50&set=set1'
        account_type = form['account_type']
        password = form['password']
        dt = datetime.now()
        id = form['id']
        #Hash password
        password = self.hash_password(password)
        if first_name and last_name and email and phone and address and city_id and latitude and longitud and photo_url and  password :
            dao = RequesterDAO()
            tid = dao.updateRequester(id,first_name , last_name , email , phone , address , city_id , latitude , longitud , photo_url , 'Requester' , password,dt)
            result = self.getRequesterByID(tid)
            return jsonify(Part=result), 201

        elif email and id and (len(form)==2):
            dao = RequesterDAO()
            tid = dao.updateRequesterEmail(id,email)
            result = self.getRequesterByID(tid)
            return jsonify(Part=result), 201

        elif phone and id and (len(form)==2):
            dao = RequesterDAO()
            tid = dao.updateRequesterPhone(id,phone)
            result = self.getRequesterByID(tid)
            return jsonify(Part=result), 201

        elif first_name and id and (len(form)==2):
            dao = RequesterDAO()
            tid = dao.updateRequesterFirst_name(id,first_name)
            result = self.getRequesterByID(tid)
            return jsonify(Part=result), 201

        elif last_name and id and (len(form)==2):
            dao = RequesterDAO()
            tid = dao.updateRequesterLast_name(id,last_name)
            result = self.getRequesterByID(tid)
            return jsonify(Part=result), 201    
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400