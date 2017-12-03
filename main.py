from flask import Flask, jsonify
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

#Show Resources Routes
@app.route('/resources')
def getAllresources():
    """ Get the items requested in a given category subcategory"""    
    handler = ResourcesHandler()
    return handler.getAllresources()

@app.route('/resources/requested')
def getAllResourcesRequested():
    """ See all the Resources Requested."""
    handler = ResourcesHandler()
    return handler.getAllresources_requested()

@app.route('/resources/avaliable')
def getAllResourcesAvailable():
    """ See all the Resources Avaliable."""
    handler = ResourcesHandler()
    return handler.getAllresources_avaliable()

@app.route('/resources/avaliable/find/<string:keywords>')
def getResourcesAvailable(keywords):
    """ Search in  the Resources Avaliable."""
    handler = ResourcesHandler()
    return handler.getresources_avaliable(keywords)

@app.route('/resources/requested/find/<string:keywords>')
def getResourcesRequested_keywords(keywords):  
    """ Search in  the Resources Requested."""   
    handler = ResourcesHandler()  
    return handler.getresources_requested(keywords)

#Show Resources by Category Routes
@app.route('/resources/requested/category')
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

@app.route('/resources/avaliable/category/<string:keywords>/sub/<string:subkeywords>')
def getResourceAvaliable_subcategory(keywords, subkeywords):
    """ Get the items avaliable in a given category subcategory"""      
    handler = CategoryHandler()
    return handler.categoryAvaliable_subcategory(keywords,subkeywords)







if __name__ == '__main__':
    app.run()
