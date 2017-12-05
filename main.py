from flask import Flask, jsonify,render_template,request
from handler.resources import ResourcesHandler
from handler.category_resources import CategoryHandler
from handler.statisc_resources import StatiscHandler
from handler.account import  AccountHandler


app = Flask(__name__)

@app.route('/')
def local():    
    """Home"""
    return 'Welcome to Project 9-20! \n To See all the Route go to /help'

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
def page_not_found(e):
    return render_template('500.html'), 500

#Show Resources Routes
@app.route('/resources')
def getAllresources():
    """ Get the items requested in a given category subcategory"""    
    handler = ResourcesHandler()
    return handler.getAllresources()

@app.route('/resources/requested')
def getAllResourcesRequested():
    """ See all the Resources Requested."""
    if not request.args:
        return ResourcesHandler().getAllresources_requested()
    else:
        return ResourcesHandler().getresources_requested(request.args)

@app.route('/resources/avaliable/')
def getResourcesAvailable():
    """ Search in  the Resources Avaliable."""
    if not request.args:
        return ResourcesHandler().getAllresources_avaliable()
    else:
        return ResourcesHandler().getresources_avaliable(request.args)

#Show Resources by Category Routes
@app.route('/resources/category')
def getCategories():
    """ See all the Categories and SubCategories."""    
    handler = CategoryHandler()
    return handler.categories()

@app.route('/resources/requested/category/<string:keywords>')
def getResourceRequested_category(keywords):
    """ Get the items in a given category"""
    handler = CategoryHandler()
    return handler.categoryRequested(keywords)

@app.route('/resources/requested/category/<string:keywords>/sub/<string:subkeywords>')
def getResourceRequested_subcategory(keywords, subkeywords):
    """ Get the items requested in a given category subcategory"""    
    handler = CategoryHandler()
    return handler.categoryRequested_subcategory(keywords,subkeywords)

@app.route('/resources/avaliable/category/<string:keywords>')
def getResourceAvaliable_category(keywords):
    """ Get the items avaliable in a given category"""
    handler = CategoryHandler()
    return handler.categoryAvaliable(keywords)

@app.route('/resources/avaliable/category/descriptiont<string:keywords>/sub/<string:subkeywords>')
def getResourceAvaliable_subcategory(keywords, subkeywords):
    """ Get the items avaliable in a given category subcategory"""      
    handler = CategoryHandler()
    return handler.categoryAvaliable_subcategory(keywords,subkeywords)

# DAILY STATISTICS
@app.route('/statistics/daily/resources/requested')
def getAllDailyResInNeed():
    """ Show Stattistics for Resources Requested""" 
    handler = StatiscHandler()
    return handler.getAllDailyRes_InNeed()

@app.route('/statistics/daily/resources/available')
def getAllDailyResAvailable():
    """ Show Statistics for Resources Avaliable""" 
    handler = StatiscHandler()
    return handler.getAllDailyRes_Available()

@app.route('/statistics/daily/resources/between%need%available')
def getAllDailyResBetween():
    """ Show Statistics for Resources Avaliable vs Requested"""    
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

@app.route('/statistics/trending/resources/between%need%available')
def getAllTrendingResBetween():
    """ Show Trending Statistics for Resources Avaliable vs Requested"""  
    handler = StatiscHandler()
    return handler.getAllTrendingRes_Between()

# TRENDING STATICTICS (8 SENATES)
@app.route('/statistics/trending/resources/requested/senate/<string:senate>')
def getAllTrendingResInNeedBySenate(senate):
    """ Show Trending Statistics for Resources Requested by Senate"""  
    handler = StatiscHandler()
    return handler.getAllDailyRes_InNeedBySenate(senate)

@app.route('/statistics/trending/resources/available/senate/<string:senate>')
def getAllTrendingResAvailableBySenate(senate):
    """ Show Trending Statistics for Resources Avaliable by Senate"""  
    handler = StatiscHandler()
    return handler.getAllDailyRes_AvailableBySenate(senate)

@app.route('/statistics/trending/resources/between%need%available/senate/<string:senate>')
def getAllTrendingResBetweenBySenate(senate):
    """ Show Trending Statistics for Resources Requested vs Avaliable by Senate"""  
    handler = StatiscHandler()
    return handler.getAllDailyRes_BetweenBySenate(senate)

#account routes
@app.route('/account/login')
def verifyAccount():    
    if not request.args:
        return jsonify("Invalid Input plese enter accountid and accountpass")
    else:       
        handler = AccountHandler()
        return handler.verifyAccount(request.args)

@app.route('/accounts/suppliers')
def getSuppliers():
    handler = AccountHandler()
    if not request.args:
        return handler.getAllSuppliers()
    else:
        return handler.getAllSuppliersInCity(request.args)
    

@app.route('/accounts')
def getAccountData():
    if not request.args:
        return jsonify("Invalid Input plese enter accountid and accountpass")
    else:
        handler = AccountHandler()
        return handler.getAccountData(request.args)



if __name__ == '__main__':
    app.run()


