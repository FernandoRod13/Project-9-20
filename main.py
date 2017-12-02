from flask import Flask, jsonify
from handler.resources import ResourcesHandler

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
def getResourcesRequested(keywords):
    handler = ResourcesHandler()
    return handler.getresources_requested(keywords)

# @app.route('/resources/requested/water')
# def getWaterCategoryRequested(keywords):
#     handler = ResourcesHandler()
#     return handler.getWaterCategory_requested()

# @app.route('/resources/avaliable/water')
# def getWaterCategoryRequested(keywords):
#     handler = ResourcesHandler()
#     return handler.getWaterCategory_requested()


if __name__ == '__main__':
    app.run()
