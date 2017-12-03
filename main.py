from flask import Flask, jsonify
from handler.resources import ResourcesHandler
from handler.category_resources import CategoryHandler

app = Flask(__name__)

@app.route('/')
def local():
    return 'Welcome to Project 9-20!'

@app.route('/resources')
def getAllresources():
    handler = ResourcesHandler()
    return handler.getAllresources()

@app.route('/resources/requested')
def getAllResourcesRequested():
    handler = ResourcesHandler()
    return handler.getAllresources_requested()

@app.route('/resources/avaliable')
def getAllResourcesAvailable():
    handler = ResourcesHandler()
    return handler.getAllresources_avaliable()

@app.route('/resources/avaliable/find/<string:keywords>')
def getResourcesAvailable(keywords):
    handler = ResourcesHandler()
    return handler.getresources_avaliable(keywords)

@app.route('/resources/requested/find/<string:keywords>')
def getResourcesRequested_keywords(keywords):  
    handler = ResourcesHandler()  
    return handler.getresources_requested(keywords)

@app.route('/category/resources/requested/<string:keywords>')
def getResourceRequested_category(keywords):
    handler = CategoryHandler()
    return handler.categoryRequested(keywords)

@app.route('/category/resources/requested/<string:keywords>/sub/<string:subkeywords>')
def getResourceRequested_subcategory(keywords, subkeywords):
    handler = CategoryHandler()
    return handler.categoryRequested_subcategory(keywords,subkeywords)







if __name__ == '__main__':
    app.run()
