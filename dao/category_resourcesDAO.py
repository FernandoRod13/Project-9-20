from flask import jsonify
import json
import psycopg2


#List of the categories and their subcategories

category_list = ["medications","babyfood","cannedfood","dryfood","ice",
                "medicaldevices","tools","clothing","powergenerators","batteries"]
category_with_subcat_list = ["fuel","water"]
category_water_list = ["smallbottles", "gallonbottles"]
category_fuel_list = ["diesel","propane","gasoline"]


class category_ResourceDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='project920', user='natalia', password='none', sslmode='disable',hostaddr='35.196.249.53')


    def getCategories(self):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources natural inner join Resource_Type  orderby category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type orderby category;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result

    def getCategory(self, category):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources natural inner join Resource_Type where category = %s orderby category;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type whre category = %s orderby category;"
        cursor.execute(query, (category,))
        for row in cursor:
            result.append(row)        
        return result
    
###############################################################
# Resources Requested
##############################################################
    def getCategoryRequested(self, keywords):
        cursor = self.conn.cursor()
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type where category = propane OR category = gas OR category = diesel orderby category;"
            cursor.execute(query)

        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type where category = smallbottles OR category = gallonbottles orderby category;"
            cursor.execute(query)
           
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type where category = %s orderby category;"
            cursor.execute(query,(keywords,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getCategoriesRequested(self):
        cursor = self.conn.cursor()
        result =[]
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources_Requested natural inner join Resource_Type orderby category;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result

###################################################################
#Resoruces Avaliable
################################################

    def getCategoryAvaliable(self, keywords):
        cursor = self.conn.cursor()
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class from Resources natural inner join Resource_Type where category = propane OR category = gas OR category = diesel orderby category;"
       
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class from Resources natural inner join Resource_type where category = smallbottles OR category = gallonbottles orderby category;"
           
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class from Resources natural inner join Resource_type where category = %s orderby category;"
            cursor.execute(query,(keywords,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getCategoriesAvaliable(self):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class from Resources natural inner join Resource_Type  orderby category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
