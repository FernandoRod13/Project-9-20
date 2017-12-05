from flask import jsonify
from dao.statistic_resourceDAO import statistic_ResourceDAO

class StatiscHandler: 

    def getAllDailyRes_InNeed(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllDailyResInNeed()
        return jsonify(Resource = res)
    
    def getAllDailyRes_Available(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllDailyResAvailable()
        return jsonify(Resource = res)
    
    def getAllDailyRes_Between(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllDailyResBetween()
        return jsonify(Resource = res)
    
    # TRENDING STATISTICS (7 DAY PERIOD)
    def getAllTrendingRes_InNeed(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResInNeed()
        return jsonify(Resource = res)
    
    def getAllTrendingRes_Available(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResAvailable()
        return jsonify(Resource = res)
    
    def getAllTrendingRes_Between(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllDailyResBetween()
        return jsonify(Resource = res)

    # TRENDING STATICTICS (8 SENATES)
    def getAllDailyRes_InNeedBySenate(self, keywords):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResInNeedBySenate(keywords)
        return jsonify(Resource = res)
    
    def getAllDailyRes_AvailableBySenate(self, keywords):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResAvailableBySenate(keywords)
        return jsonify(Resource = res)
    
    def getAllDailyRes_BetweenBySenate(self, keywords):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResBetweenBySenate(keywords)
        return jsonify(Resource = res)
   