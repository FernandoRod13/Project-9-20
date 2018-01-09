from flask import Flask, jsonify,render_template,request
from handler.resources import ResourcesHandler
from handler.category_resources import CategoryHandler
from handler.statisc_resources import StatiscHandler
from handler.account import  AccountHandler
from handler.transaction import TransactionHandler
from handler.supplier import  SupplierHandler
from handler.requester import  RequesterHandler


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

#VERIFTY!!!!!!!!!!!!!!!!!!!!!!!!
@app.route('/resources/find')
def getSearchresources():
    """ Get the items requested in a given category subcategory"""    
    handler = ResourcesHandler()
    if not request.args:
        return ResourcesHandler().getAllresources()
    else:
        return handler.getFindAllresources(request.args)

@app.route('/resources/requested')
def getAllResourcesRequested():
    """ See all the Resources Requested."""
    return ResourcesHandler().getAllresources_requested()
   
@app.route('/resources/requested/find')
def getSearchResourcesRequested():
    """ See all the Resources Requested. Follow by ?name=description"""
    if not request.args:
        return ResourcesHandler().getAllresources_requested()
    else:
        return ResourcesHandler().getresources_requested(request.args)

@app.route('/resources/available')
def getResourcesAvailable():
    """ Show  Resources available."""
    return ResourcesHandler().getAllresources_avaliable()
    
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

#account routes
@app.route('/accounts/login')
def verifyAccount():
    """ Account login"""    
    if not request.args:
        return jsonify("Invalid Input plese enter accountid and accountpass")
    else:       
        handler = AccountHandler()
        return handler.verifyAccount(request.args)

@app.route('/suppliers')
def getAllSuppliers():
    """ Get all suppliers"""
    handler = SupplierHandler()
    if not request.args:
        return handler.getAllSuppliers()
    else:
        return handler.searchAllSuppliersByParameter(request.args)
    
@app.route('/suppliers/<int:sid>')
def getSupplierByID(sid):   
    handler = SupplierHandler()
    return handler.getSupplierByID(sid)

@app.route('/accounts/requester')
def getRequesters():
    """Get all requester"""
    handler = AccountHandler()   
    return handler.getAllRequester(request.args)
  
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

if __name__ == '__main__':
    app.run()


