
import json

from flask import jsonify
class statistic_ResourceDAO:
    def __init__(self):
        pass

# DAILY STATISTICS
    def getAllDailyResInNeed(self):
        result = []
        result.append("Daily resources in need")
        return result
    
    def getAllDailyResAvailable(self):
        result = []
        result.append("Daily resources available")
        return result
    
    def getAllDailyResBetween(self):
        result = []
        result.append("Daily resources between")
        return result
    
    # TRENDING STATISTICS (7 DAY PERIOD)
    def getAllTrendingResInNeed(self):
        result = []
        result.append("Trending resources in need")
        return result
    
    def getAllTrendingResAvailable(self):
        result = []
        result.append("Trending resources available")
        return result
    
    def getAllTrendingResBetween(self):
        result = []
        result.append("Trending resources between")
        return result 
    
    # TRENDING STATICTICS (8 SENATES)
    def getAllTrendingResInNeedBySenate(self, keywords):
        result = []
        result.append("Trending resources by" + keywords + " in need")
        return result
    
    def getAllTrendingResAvailableBySenate(self, keywords):
        result = []
        result.append("Trending resources by" + keywords + " available")
        return result
    
    def getAllTrendingResBetweenBySenate(self, keywords):
        result = []
        result.append("Trending resources by" + keywords + " in between")
        return result
    
    # Account verification
    def verifyAccount(self, accountid, accountpass):
        result = []
        result.append("This is to verify if account " + accountid + "is correct")
        return result
    
