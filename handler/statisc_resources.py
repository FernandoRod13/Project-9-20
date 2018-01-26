from flask import jsonify
from dao.statistic_resourceDAO import statistic_ResourceDAO

class StatiscHandler: 

    def build_Region_Amount(self,row):
        result = {}
        result['Region'] = row[0]
        if row[1] == None:
            result['Amount'] = 0;
        else:
            result['Amount'] = row[1]    
        return result

    def build_Region_Amount_Compare(self,row):
        result = {}
        result['Region'] = row[0]
        if row[1] == None: #No requested
            if row[2] == None: #Nore available
                result['Amount'] = 0;
            else:
                result['Amount'] = (-1)* row[2] #negative available
        else:
            if row[2] == None:
                result['Amount'] = row[1]  
            else:               
                result['Amount'] = row[3]    
        return result

    def getAllDailyRes_InNeed(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllDailyResInNeed()
        result_list = []
        for row in res:
            result = self.build_Region_Amount(row)
            result_list.append(result)                 
        return jsonify(Resource_Requested = result_list)

       
    
    def getAllDailyRes_Available(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllDailyResAvailable()
        result_list = []
        for row in res:
            result = self.build_Region_Amount(row)
            result_list.append(result)                 
        return jsonify(Resource_Available = result_list)

       
    
    def getAllDailyRes_Between(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllDailyResBetween()
        result_list = []
        for row in res:
            result = self.build_Region_Amount_Compare(row)
            result_list.append(result)                 
        return jsonify(Resource_Compare = result_list)

        
    # TRENDING STATISTICS (7 DAY PERIOD)
    def getAllTrendingRes_InNeed(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResInNeed()
        result_list = []
        for row in res:
            result = self.build_Region_Amount(row)
            result_list.append(result)                 
        return jsonify(Resource_Requested = result_list)
        
    
    def getAllTrendingRes_Available(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResAvailable()
        result_list = []
        for row in res:
            result = self.build_Region_Amount(row)
            result_list.append(result)                 
        return jsonify(Resource_Available = result_list)
        
    
    def getAllTrendingRes_Between(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResBetween()
        result_list = []
        for row in res:
            result = self.build_Region_Amount_Compare(row)
            result_list.append(result)                 
        return jsonify(Resource_Compare = result_list)
       

    # TRENDING STATICTICS  30 Days
    def getAllDailyRes_InNeedBySenate(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResInNeedBySenate()
        result_list = []
        for row in res:
            result = self.build_Region_Amount(row)
            result_list.append(result)                 
        return jsonify(Resource_Requested = result_list)
        
       
    
    def getAllDailyRes_AvailableBySenate(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResAvailableBySenate()
        result_list = []
        for row in res:
            result = self.build_Region_Amount(row)
            result_list.append(result)                 
        return jsonify(Resource_Available = result_list)
        
    
    def getAllDailyRes_BetweenBySenate(self):
        dao = statistic_ResourceDAO()
        res = dao.getAllTrendingResBetweenBySenate()
        result_list = []
        for row in res:
            result = self.build_Region_Amount_Compare(row)
            result_list.append(result)                 
        return jsonify(Resource_Compare = result_list)
        
   