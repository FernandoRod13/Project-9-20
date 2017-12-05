from flask import Flask, jsonify,render_template,request
from handler.resources import ResourcesHandler
from handler.category_resources import CategoryHandler


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


#
# ****************** DASHBOARD METHODS *********************
#

# DAILY STATISTICS
@app.route('/dashboard/daily_statistics/resources_inneed')
def getAllDailyResInNeed():
    handler = ResourcesHandler()
    return handler.getAllDailyRes_InNeed()

@app.route('/dashboard/daily_statistics/resources_available')
def getAllDailyResAvailable():
    handler = ResourcesHandler()
    return handler.getAllDailyRes_Available()

@app.route('/dashboard/daily_statistics/resources_between%need%available')
def getAllDailyResBetween():
    handler = ResourcesHandler()
    return handler.getAllDailyRes_Between()

# TRENDING STATISTICS (7 DAY PERIOD)
@app.route('/dashboard/trending_statistics/resources_inneed')
def getAllTrendingResInNeed():
    handler = ResourcesHandler()
    return handler.getAllTrendingRes_InNeed()

@app.route('/dashboard/trending_statistics/resources_available')
def getAllTrendingResAvailable():
    handler = ResourcesHandler()
    return handler.getAllTrendingRes_Available()

@app.route('/dashboard/trending_statistics/resources_between%need%available')
def getAllTrendingResBetween():
    handler = ResourcesHandler()
    return handler.getAllTrendingRes_Between()

# TRENDING STATICTICS (8 SENATES)
@app.route('/dashboard/trending_statistics/resources_inneed/findBy?<string:senate>')
def getAllTrendingResInNeedBySenate(senate):
    handler = ResourcesHandler()
    return handler.getAllDailyRes_InNeedBySenate(senate)

@app.route('/dashboard/trending_statistics/resources_available/findBy?<string:senate>')
def getAllTrendingResAvailableBySenate(senate):
    handler = ResourcesHandler()
    return handler.getAllDailyRes_AvailableBySenate(senate)

@app.route('/dashboard/trending_statistics/resources_between%need%available/findBy?<string:senate>')
def getAllTrendingResBetweenBySenate(senate):
    handler = ResourcesHandler()
    return handler.getAllDailyRes_BetweenBySenate(senate)

#account method
@app.route('/account/verify?<string:accountid>&<string:accountpass>')
def verifyAccount(accountid, accountpass):
    handler = ResourcesHandler()
    return handler.verifyAccount(accountid, accountpass)

if __name__ == '__main__':
    app.run()
