from flask import Flask, jsonify,render_template,request
from handler.resources import ResourcesHandler
from handler.category_resources import CategoryHandler
from handler.statisc_resources import StatiscHandler
from handler.transaction import TransactionHandler
from handler.supplier import  SupplierHandler
from handler.requester import  RequesterHandler
from handler.accounts import  AccountHandler



app = Flask(__name__)

@app.route('/')
def local():    
    """Home"""
    return render_template('home.html'), 500
@app.route('/help', methods = ['GET'])
def help():
    """See all the Routes"""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)

#Error Handling 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

#Show Resources Routes
@app.route('/resources')
def getAllresources():
    """ Get the items requested in a given category subcategory"""    
    handler = ResourcesHandler()
    return handler.getAllresources()

@app.route('/resources/find')
def getSearchresources():
    """ Get the items requested in a given category subcategory"""    
    handler = ResourcesHandler()
    if not request.args:
        return ResourcesHandler().getAllresources()
    else:
        return handler.getFindAllresources(request.args)

@app.route('/resources/requested', methods=['GET', 'POST', 'PUT'])
def getAllResourcesRequested():
    ## """ See all the Resources Requested."""
    if  request.method == 'GET':   
        return ResourcesHandler().getAllresources_requested()
    elif request.method == 'PUT':
        return ResourcesHandler().updateResourcesRequested(request.form)       
    elif request.method == 'POST':
        return ResourcesHandler().insertResourcesRequested(request.form)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/resources/requested/<int:rid>')
def getResourceAvailableByID(rid):
    """ Get Resources Requested by id"""
    return ResourcesHandler().getResourceRequestedByID(rid)

   
@app.route('/resources/requested/find')
def getSearchResourcesRequested():
    """ See all the Resources Requested. Follow by ?name=description"""
    if not request.args:
        return ResourcesHandler().getAllresources_requested()
    else:
        return ResourcesHandler().getresources_requested(request.args)


@app.route('/resources/available/requester/<int:id>')
def getResourceSupplierByResourceID(id):
    """Get Resources that a given requester id supplies"""
    return ResourcesHandler().getResourcesRequestedOfRequesterByID(rid)

@app.route('/resources/available',methods=['GET', 'POST', 'PUT'])
def getResourcesAvailable():
    if request.method == 'GET':
   ## """ Show  Resources available."""
        return ResourcesHandler().getAllresources_avaliable()      
    elif request.method == 'PUT':
        return ResourcesHandler().updateResourcesAvailable(request.form)       
    elif request.method == 'POST':
        return ResourcesHandler().insertResourcesAvailable(request.form)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/resources/available/<int:rid>')
def getResourcesAvailableByID(rid):
    """Get Resource By ID"""
    return ResourcesHandler().getResourceAvaliableByRID(rid)


@app.route('/resources/available/<int:rid>/suppliers')
def getResouresAvaliableBySupplierID(rid):
    """Get Suppliers who supply a Resource"""
    return ResourcesHandler().getSuppliersForAvailableResourceByRID(rid)

@app.route('/resources/available/supplier/<int:id>')
def getResourceSuppliedbySupplierID(id):
    """Get Resources that a given supplier id supplies"""
    return ResourcesHandler().getResourcesAvalibleOfSupplierByID(rid)
    
@app.route('/resources/available/find')
def getSearchResourcesAvailable():
    """ Search in  the Resources Avaliable. Follow by ?name=description"""
    if not request.args:
        return ResourcesHandler().getAllresources_avaliable()
    else:
        return ResourcesHandler().getresources_avaliable(request.args)
    

# #Show Resources by Category Routes
@app.route('/resources/category')
def getCategories():
    """ See all the Categories Order by Category"""    
    if not request.args:   
        return CategoryHandler().categories()
    else:
        return CategoryHandler().category(request.args)   

@app.route('/resources/requested/category')
def getResourceRequested_category():
    """ Get the items in a given category"""
    if not request.args:   
        return CategoryHandler().categoriesRequested()
    else:
        return CategoryHandler().categoryRequested(request.args)
   

@app.route('/resources/available/category')
def getResourceAvaliable_category():
    """ Get the items available in a given category"""
    if not request.args:   
        return CategoryHandler().categoriesAvaliable()
    else:
        return CategoryHandler().categoryAvaliable(request.args)
 


# DAILY STATISTICS
@app.route('/statistics/daily/resources/requested')
def getAllDailyResInNeed():
    """ Show Stattistics for Resources Requested""" 
    handler = StatiscHandler()
    return handler.getAllDailyRes_InNeed()

@app.route('/statistics/daily/resources/available')
def getAllDailyResAvailable():
    """ Show Statistics for Resources Available""" 
    handler = StatiscHandler()
    return handler.getAllDailyRes_Available()

@app.route('/statistics/daily/resources/between_requested_available')
def getAllDailyResBetween():
    """ Show Statistics for Resources Available vs Requested"""    
    handler = StatiscHandler()
    return handler.getAllDailyRes_Between()

# TRENDING STATISTICS (7 DAY PERIOD)
@app.route('/statistics/trending/resources/requested')
def getAllTrendingResInNeed():
    """ Show Trending Statistics for Resources  Requested"""  
    handler = StatiscHandler()
    return handler.getAllTrendingRes_InNeed()

@app.route('/statistics/trending/resources/available')
def getAllTrendingResAvailable():
    """ Show Trending Statistics for Resources Avaliable """  
    handler = StatiscHandler()
    return handler.getAllTrendingRes_Available()

@app.route('/statistics/trending/resources/between_requested_available')
def getAllTrendingResBetween():
    """ Show Trending Statistics for Resources Avaliable vs Requested"""  
    handler = StatiscHandler()
    return handler.getAllTrendingRes_Between()

# TRENDING STATICTICS (8 SENATES)
@app.route('/statistics/trending/resources/requested/region/<string:region_id>')
def getAllTrendingResInNeedBySenate(region_id):
    """ Show Trending Statistics for Resources Requested by Senatorial Region"""  
    handler = StatiscHandler()
    return handler.getAllDailyRes_InNeedBySenate(region_id)

@app.route('/statistics/trending/resources/available/region/<string:region_id>')
def getAllTrendingResAvailableBySenate(region_id):
    """ Show Trending Statistics for Resources Avaliable by Senatorial Region"""  
    handler = StatiscHandler()
    return handler.getAllDailyRes_AvailableBySenate(region_id)

@app.route('/statistics/trending/resources/between_requested_available/region/<string:region_id>')
def getAllTrendingResBetweenByregion_id(region_id):
    """ Show Trending Statistics for Resources Requested vs Avaliable by Senatorial Region"""  
    handler = StatiscHandler()
    return handler.getAllDailyRes_BetweenBySenate(region_id)

@app.route('/suppliers',methods=['GET', 'POST', 'PUT'])
def getAllSuppliers():
    """ Get all suppliers"""
    handler = SupplierHandler()
    if request.method == 'GET':
        if not request.args:
            return handler.getAllSuppliers()
        else:
            return handler.searchAllSuppliersByParameter(request.form)
    elif request.method == 'PUT':
        return SupplierHandler().PutSupplier(request.form)
    elif request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        return jsonify(Error = "Method not allowed"), 405
    
@app.route('/suppliers/<int:sid>')
def getSupplierByID(sid):   
    handler = SupplierHandler()
    return handler.getSupplierByID(sid)

@app.route('/requesters',methods=['GET', 'POST', 'PUT'])
def getRequesters():
    """Get all requester"""
    handler = RequesterHandler() 
    if request.method == 'GET':
        if not request.args:
            return handler.getAllRequesters()
        else:
            return handler.searchAllRequestersByParameter(request.args)
    elif request.method == 'PUT':
        return RequesterHandler().PutRequester(request.form)
    elif request.method == 'POST':
        return RequesterHandler().insertRequester(request.form)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/requesters/<int:rid>')
def getRequesterByID(rid):
    handler = RequesterHandler()
    return handler.getRequesterByID(rid)



@app.route('/admin',methods=['GET', 'POST', 'PUT'])
def getAllAdministraror():
    """ Get all admistrator"""
    handler = AccountHandler()
    if request.method == 'GET':
        if not request.args:
            return handler.getAllAdmin()       
    elif request.method == 'PUT':
        return AccountHandler().PutAdmin(request.form)       
    elif request.method == 'POST':
        return AccountHandler().insertAdmin(request.form)
    else:
        return jsonify(Error = "Method not allowed"), 405

    
#          TRANSACTIONS ROUTES

@app.route('/transactions/getPaymentMethods', methods=['GET'])
def getPaymentMethods():
    if request.method == 'GET':
        return TransactionHandler().getPaymentMethods(request.args)

@app.route('/transactions/getBuyerTransaction', methods=['GET'])
def getBuyerTransaction():
    if request.method == 'GET':
        return TransactionHandler().getTransactionByBuyer(request.args)

@app.route('/transactions/getSupplierTransaction', methods=['GET'])
def getSupplierTransaction():
    if request.method == 'GET':
        return TransactionHandler().getTransactionBySupplier(request.args)

@app.route('/transactions/getResourceTransaction', methods=['GET'])
def getResourceTransaction():
    if request.method == 'GET':
        return TransactionHandler().getTransactionByResource(request.args)


#########################################
#### LOGIN
####################################

@app.route('/login', methods=['GET'])
def getAccountLogin():
    if request.method == 'GET':
        return AccountHandler().userLogin(request.args)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/user/changepassword', methods=['GET'])
def getChangeAccountPassword():
    if request.method == 'GET':
        return AccountHandler().userChangePassword(request.args)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/cities', methods=['GET'])
def getCityList():
    if request.method == 'GET':
        return AccountHandler().getCities()
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/resource_type', methods=['GET'])
def getResourceTypeList():
    if request.method == 'GET':
        return AccountHandler().getResourceType()
    else:
        return jsonify(Error = "Method not allowed"), 405





    
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run()


