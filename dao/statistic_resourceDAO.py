import json
import psycopg2
from flask import jsonify
from config.dbconfig import pg_config
class statistic_ResourceDAO:
    def __init__(self):                              
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable', hostaddr='35.196.249.53')


# DAILY STATISTICS
    def getAllDailyResInNeed(self):
        cursor = self.conn.cursor()
        query = (" with b as (Select region_name, count(region_name) as x from region natural inner join city "
        " natural inner join accounts natural inner join location natural inner join resources_requested "
        " natural inner join requester where creation_date = date_trunc('day',now())  group by region_name) "
        "Select region.region_name, x from b full outer join region on region.region_name = b.region_name;" )       
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllDailyResAvailable(self):
        cursor = self.conn.cursor()
        query = (" with a as (Select region_name, count(region_name) as y from region natural inner join city "
        "natural inner join accounts natural inner join location natural inner join resources natural inner join "
        "supplier where creation_date = date_trunc('day',now()) group by region_name) "
        "Select region.region_name, y as total from a full outer join region on region.region_name = a.region_name; ")    
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllDailyResBetween(self):
        cursor = self.conn.cursor()
        query = ( "with a as (Select region_name, count(region_name) as y from region natural inner join city natural inner join accounts "
        "natural inner join location natural inner join resources natural inner join supplier where creation_date = date_trunc('day',now()) group by region_name),"
        "a1 as (Select region.region_name, y from a full outer join region on region.region_name = a.region_name),"
        "b as (Select region_name, count(region_name) as x from region natural inner join city natural inner join accounts "    
        "natural inner join location natural inner join resources_requested natural inner join requester where creation_date = date_trunc('day',now()) group by region_name),"
        "b1 as( Select region.region_name, x from b full outer join region on region.region_name = b.region_name)"
        "Select a1.region_name, x as requested ,y as availabe, x - y as vs  from a1 full outer join b1 on a1.region_name = b1.region_name")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    # TRENDING STATISTICS (7 DAY PERIOD)
    def getAllTrendingResInNeed(self):
        cursor = self.conn.cursor()
        query = (" with b as (Select region_name, count(region_name) as x from region natural inner join city "
        " natural inner join accounts natural inner join location natural inner join resources_requested "
        " natural inner join requester "
        "where creation_date <= date_trunc('day',now()) and creation_date >= (date_trunc('day',now()) - interval '7 days') "
        "group by region_name) "
        "Select region.region_name, x from b full outer join region on region.region_name = b.region_name;" )       
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllTrendingResAvailable(self):
        cursor = self.conn.cursor()
        query = (" with a as (Select region_name, count(region_name) as y from region natural inner join city "
        "natural inner join accounts natural inner join location natural inner join resources natural inner join "
        "supplier "
        "where creation_date <= date_trunc('day',now()) and creation_date >= (date_trunc('day',now()) - interval '7 days')  "
        "group by region_name) "
        " Select region.region_name, y as total from a full outer join region on region.region_name = a.region_name; ")    
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllTrendingResBetween(self):
        cursor = self.conn.cursor()
        query = ( "with a as (Select region_name, count(region_name) as y from region natural inner join city natural inner join accounts "
        "natural inner join location natural inner join resources natural inner join supplier " 
        "where creation_date <= date_trunc('day',now()) and creation_date >= (date_trunc('day',now()) - interval '7 days') "
        "group by region_name), "
        "a1 as (Select region.region_name, y from a full outer join region on region.region_name = a.region_name), "
        "b as (Select region_name, count(region_name) as x from region natural inner join city natural inner join accounts "    
        "natural inner join location natural inner join resources_requested natural inner join requester "
        "where creation_date <= date_trunc('day',now()) and creation_date >= (date_trunc('day',now()) - interval '7 days') "
         "group by region_name), "
        "b1 as( Select region.region_name, x from b full outer join region on region.region_name = b.region_name) "
        "Select a1.region_name, x as requested ,y as availabe, x - y as vs  from a1 full outer join b1 on a1.region_name = b1.region_name")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    # TRENDING STATICTICS (8 SENATES)
    def getAllTrendingResInNeedBySenate(self):
        cursor = self.conn.cursor()
        query = (" with b as (Select region_name, count(region_name) as x from region natural inner join city "
        " natural inner join accounts natural inner join location natural inner join resources_requested "
        " natural inner join requester where creation_date <= date_trunc('day',now()) and creation_date >= (date_trunc('day',now()) - interval '30 days')"
        "  group by region_name) "
        "Select region.region_name, x from b full outer join region on region.region_name = b.region_name;" )       
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllTrendingResAvailableBySenate(self):
        cursor = self.conn.cursor()
        query = (" with a as (Select region_name, count(region_name) as y from region natural inner join city "
        "natural inner join accounts natural inner join location natural inner join resources natural inner join "
        "supplier"
        " where creation_date <= date_trunc('day',now()) and creation_date >= (date_trunc('day',now()) - interval '30 days') "
        "group by region_name) "
        "Select region.region_name, y as total from a full outer join region on region.region_name = a.region_name; ")    
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllTrendingResBetweenBySenate(self):
        cursor = self.conn.cursor()
        query = ( "with a as (Select region_name, count(region_name) as y from region natural inner join city natural inner join accounts "
        "natural inner join location natural inner join resources natural inner join supplier "
        "where creation_date <= date_trunc('day',now()) and creation_date >= (date_trunc('day',now()) - interval '30 days')"
        "group by region_name),"
        "a1 as (Select region.region_name, y from a full outer join region on region.region_name = a.region_name),"
        "b as (Select region_name, count(region_name) as x from region natural inner join city natural inner join accounts "    
        "natural inner join location natural inner join resources_requested natural inner join requester "
        "where creation_date <= date_trunc('day',now()) and creation_date >= (date_trunc('day',now()) - interval '30 days')"
        "group by region_name),"
        "b1 as( Select region.region_name, x from b full outer join region on region.region_name = b.region_name)"
        "Select a1.region_name, x as requested ,y as availabe, x - y as vs  from a1 full outer join b1 on a1.region_name = b1.region_name")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    
