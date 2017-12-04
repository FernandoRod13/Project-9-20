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
@app.route('/dashboard/trending_statistics/resources_inneed/findBySenate/<string:keywords>')
def getAllTrendingResInNeedBySenate(keywords):
    handler = ResourcesHandler()
    return handler.getAllDailyRes_InNeedBySenate(keywords)

@app.route('/dashboard/trending_statistics/resources_available/findBySenate/<string:keywords>')
def getAllTrendingResAvailableBySenate(keywords):
    handler = ResourcesHandler()
    return handler.getAllDailyRes_AvailableBySenate(keywords)

@app.route('/dashboard/trending_statistics/resources_between%need%available/findBySenate/<string:keywords>')
def getAllTrendingResBetweenBySenate(keywords):
    handler = ResourcesHandler()
    return handler.getAllDailyRes_BetweenBySenate(keywords)

if __name__ == '__main__':
    app.run()