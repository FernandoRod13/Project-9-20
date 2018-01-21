from flask import jsonify
import json
import psycopg2


#List of the categories AND their subcategories

category_list = ["medications","babyfood","cannedfood","dryfood","ice",
                "medicaldevices","tools","clothing","powergenerators","batteries"]
category_with_subcat_list = ["fuel","water"]
category_water_list = ["smallbottles", "gallonbottles"]
category_fuel_list = ["diesel","propane","gasoline"]


class category_ResourceDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='project920', user='postgres', password='ManuelDB', sslmode='disable',hostaddr='35.196.249.53')


    def getCategory(self, category):
        cursor = self.conn.cursor()
        result = []
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel' order by requested_name;"
            cursor.execute(query)
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = 'smallbottles' OR type_name = 'gallonbottles' order by requested_name;"
            cursor.execute(query)          
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s order by requested_name;"
            cursor.execute(query, (category,))
        
        for row in cursor:
            result.append(row)

        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where  type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel' order by resource_name;"
            cursor.execute(query)
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where  type_name = 'smallbottles' OR type_name = 'gallonbottles' order by resource_name;"
            cursor.execute(query)
        else:
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where type_name = %s order by resource_name;"
            cursor.execute(query, (category,))        
        for row in cursor:
            result.append(row)        
        return result

    def getCategories(self):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name  from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City order by requested_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City order by resource_name;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result

    def getCategory_Qty(self, category,qty):
        cursor = self.conn.cursor()
        result = []
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by resource_name;"
            cursor.execute(query, (qty,))
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles' ) order by resource_name;"
            cursor.execute(query, (qty,))          
        else:
            #Get Resources avaliable
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class, quantity , city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s AND quantity = %s order by resource_name;"
            cursor.execute(query, (category,qty,))
        
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by requested_name;"
            cursor.execute(query, (qty,))
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_type natural inner join Accounts natural inner join Location natural inner join City where quantity= %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles') order by requested_name;"
            cursor.execute(query, (qty,))
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class, quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s AND quantity = %s order by requested_name;"
            cursor.execute(query, (category,qty))        
        for row in cursor:
            result.append(row)        
        return result
    
    def getCategory_Price(self, category,price):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by resource_name;"
            cursor.execute(query, (price,))
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where price = %s AND (type_name =' smallbottles' OR type_name = 'gallonbottles' ) order by resource_name;"
            cursor.execute(query, (price,))          
        else:
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join type_name = %s AND price = %s order by resource_name;"
            cursor.execute(query, (category,price))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where price = %s AND (type_name = ' propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by requested_name;"
            cursor.execute(query, (price,))
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where price = %s AND (type_name =' smallbottles' OR type_name = 'gallonbottles' ) order by requested_name;"
            cursor.execute(query, (price,))          
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class, quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s AND price = %s order by requested_name;"
            cursor.execute(query, (category,price))
        for row in cursor:
            result.append(row)        
        return result

    def getCategory_City(self, category,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name  = %s AND (type_name = ' propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by resource_name;"
            cursor.execute(query, (city,))
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name = %s AND (type_name =' smallbottles' OR type_name = 'gallonbottles' ) order by resource_name;"
            cursor.execute(query, (city,))          
        else:
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where type_name = %s AND city_name = %s order by resource_name;"
            cursor.execute(query, (category,city))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s AND (type_name = ' propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by requested_name;"
            cursor.execute(query, (city,))
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s AND (type_name =' smallbottles' OR type_name = 'gallonbottles' ) order by requested_name;"
            cursor.execute(query, (city,))          
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where type_name = %s AND city_name = %s order by requested_name;"
            cursor.execute(query, (category,city))
        for row in cursor:
            result.append(row)        
        return result

    def getCategory_Region(self, category,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name  = %s AND (type_name = ' propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by resource_name;"
            cursor.execute(query, (region,))
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name  from Resources natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s AND (type_name =' smallbottles' OR type_name = 'gallonbottles' ) order by resource_name;"
            cursor.execute(query, (region,))          
        else:
            query = "Select resource_id,  resource_name , type_name as category, account_id, description, class , quantity, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where type_name = %s AND region_name = %s order by resource_name;"
            cursor.execute(query, (category,region))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name  from Resources_Requested natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s AND (type_name = ' propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by requested_name;"
            cursor.execute(query, (region,))
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class , quantity, city_name  from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s AND (type_name =' smallbottles' OR type_name = 'gallonbottles' ) order by requested_name;"
            cursor.execute(query, (region,))          
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, class, quantity, city_name  from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where type_name = %s AND region_name = %s order by requested_name;"
            cursor.execute(query, (category,region))
        for row in cursor:
            result.append(row)        
        return result

###############################################################
# Resources Requested
##############################################################
    def getCategoryRequested(self, category):
        cursor = self.conn.cursor()
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel' order by requested_name;"
            cursor.execute(query)

        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name ='smallbottles' OR type_name = 'gallonbottles' order by requested_name;"
            cursor.execute(query)
           
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s order by requested_name;"
            cursor.execute(query,(category,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getCategoriesRequested(self):
        cursor = self.conn.cursor()
        result =[]
        query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_Date , city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City order by requested_name;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result
    def getCategoryRequested_Qty(self, category,qty):
        cursor = self.conn.cursor()       
        result = []
        
        #Get Resources requested
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by requested_name;"
            cursor.execute(query, (qty,))
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity= %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles') order by requested_name;"
            cursor.execute(query, (qty,))
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s AND quantity = %s order by requested_name;"
            cursor.execute(query, (category,qty))

        for row in cursor:
            result.append(row)        
        return result
    
    def getCategoryRequested_Price(self, category,price):
        cursor = self.conn.cursor()
        
        result = []
        
        #Get Resources requested
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where price = %s AND (type_name = ' propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by requested_name;"
            cursor.execute(query, (price,))
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where price = %s AND (type_name =' smallbottles' OR type_name = 'gallonbottles' ) order by requested_name;"
            cursor.execute(query, (price,))          
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s AND price = %s order by requested_name;"
            cursor.execute(query, (category,price))
        for row in cursor:
            result.append(row)        
        return result

    def getCategoryRequested_City(self, category,city):
        cursor = self.conn.cursor()        
        result = []
       
        #Get Resources requested
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name  from Resources_Requested natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by requested_name;"
            cursor.execute(query, (city,))
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name  from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles' ) order by requested_name;"
            cursor.execute(query, (city,))          
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name   from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where type_name = %s AND city_name = %s order by requested_name;"
            cursor.execute(query, (category,city))
        for row in cursor:
            result.append(row)        
        return result

    def getCategoryRequested_Region(self, category,region):
        cursor = self.conn.cursor()        
        result = []
        
        #Get Resources requested
        if(category == 'fuel'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name  from Resources_Requested natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by category;"
            cursor.execute(query, (region,))
        elif(category == 'water'):
            query = "Select request_id,  requested_name  , type_name as category, account_id, description,  quantity, creation_Date, city_name  from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles' ) order by requested_name;"
            cursor.execute(query, (region,))          
        else:
            query = "Select request_id,  requested_name  , type_name as category, account_id, description, quantity, creation_Date, city_name  from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where type_name = %s AND region_name = %s order by requested_name;"
            cursor.execute(query, (category,region))
        for row in cursor:
            result.append(row)        
        return result       

###################################################################
#Resoruces Avaliable
################################################

    def getCategoryAvaliable(self, category):
        cursor = self.conn.cursor()
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = ' propane' OR type_name = 'gasoline' OR type_name = 'diesel' order by resource_name;"
            cursor.execute(query)
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name =' smallbottles' OR type_name = 'gallonbottles' order by resource_name;"
            cursor.execute(query)
        else:
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s order by resource_name;"
            cursor.execute(query,(category,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getCategoriesAvaliable(self):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City order by resource_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getCategoryAvaliable_Qty(self, category,qty):
        cursor = self.conn.cursor()
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by resource_name;"
            cursor.execute(query, (qty,))
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where quantity = %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles' ) order by resource_name;"
            cursor.execute(query, (qty,))          
        else:
            #Get Resources avaliable
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s AND quantity = %s order by resource_name;"
            cursor.execute(query, (category,qty,))
        result = []
        for row in cursor:
            result.append(row)               
        return result
    
    def getCategoryAvaliable_Price(self, category,price):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where price = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by resource_name;"
            cursor.execute(query, (price,))
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where price = %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles' ) order by resource_name;"
            cursor.execute(query, (price,))          
        else:
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where type_name = %s AND price = %s order by resource_name;"
            cursor.execute(query, (category,price))
        result = []
        for row in cursor:
            result.append(row)
               
        return result

    def getCategoryAvaliable_City(self, category,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City where city_name  = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by resource_name;"
            cursor.execute(query, (city,))
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where city_name = %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles' ) order by resource_name;"
            cursor.execute(query, (city,))          
        else:
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City  where type_name = %s AND city_name = %s order by resource_name;"
            cursor.execute(query, (category,city))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getCategoryAvaliable_Region(self, category,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(category == 'fuel'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type   natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name  = %s AND (type_name = 'propane' OR type_name = 'gasoline' OR type_name = 'diesel') order by resource_name;"
            cursor.execute(query, (region,))
        elif(category == 'water'):
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type   natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s AND (type_name ='smallbottles' OR type_name = 'gallonbottles' ) order by resource_name;"
            cursor.execute(query, (region,))          
        else:
            query = "Select resource_id,  resource_name , type_name as category, account_id, price, description, availability, quantity, creation_Date,last_update, city_name  from Resources natural inner join Resource_Type   natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where type_name = %s AND region_name = %s order by resource_name;"
            cursor.execute(query, (category,region))
        result = []
        for row in cursor:        
            result.append(row)        
        return result
