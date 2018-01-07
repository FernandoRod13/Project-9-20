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


    def getCategory(self, category):
        cursor = self.conn.cursor()
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where category = propane OR category = gas OR category = diesel orderby category;"
            cursor.execute(query)
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where category = smallbottles OR category = gallonbottles orderby category;"
            cursor.execute(query)          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where category = %s orderby category;"
            cursor.execute(query, (category,))

        for row in cursor:
            result.append(row)

        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_Type where category = propane OR category = gas OR category = diesel orderby category;"
            cursor.execute(query)
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_type where category = smallbottles OR category = gallonbottles orderby category;"
            cursor.execute(query)
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_type where category = %s orderby category;"
            cursor.execute(query, (category,))

        for row in cursor:
            result.append(row)        
        return result

    def getCategories(self):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_Type orderby category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type orderby category;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result

    def getCategory_Qty(self, category,qty):
        cursor = self.conn.cursor()
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where quantity = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (qty,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where quantity = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (qty,))          
        else:
            #Get Resources avaliable
            query = "Select name , Resource_Type.name as category, accountID, description, class, quantity from Resources natural inner join Resource_Type where category = %s and quantity = %s orderby category;"
            cursor.execute(query, (category,qty,))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_Type where quantity = %s (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (qty,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_type where quantity= %s (category = smallbottles OR category = gallonbottles) orderby category;"
            cursor.execute(query, (qty,))
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class, quantity from Resources_Requested natural inner join Resource_Type where category = %s and quantity = %s orderby category;"
            cursor.execute(query, (category,qty))
        for row in cursor:
            result.append(row)        
        return result
    
    def getCategory_Price(self, category,price):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where price = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (price,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where price = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (price,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_Type where category = %s and price = %s orderby category;"
            cursor.execute(query, (category,price))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where price = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (price,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type where price = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (price,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class, quantity from Resources_Requested natural inner join Resource_Type where category = %s and price = %s orderby category;"
            cursor.execute(query, (category,price))
        for row in cursor:
            result.append(row)        
        return result

    def getCategory_City(self, category,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name  = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (city,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (city,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where category = %s and city_name = %s orderby category;"
            cursor.execute(query, (category,city))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (price,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_anme = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (price,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where category = %s and city_name = %s orderby category;"
            cursor.execute(query, (category,city))
        for row in cursor:
            result.append(row)        
        return result

    def getCategory_Region(self, category,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name  = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (region,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (region,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where category = %s and region_name = %s orderby category;"
            cursor.execute(query, (category,region))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (price,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, class , quantity from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (price,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, class, quantity from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where category = %s and region_name = %s orderby category;"
            cursor.execute(query, (category,region))
        for row in cursor:
            result.append(row)        
        return result

###############################################################
# Resources Requested
##############################################################
    def getCategoryRequested(self, keywords):
        cursor = self.conn.cursor()
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type where category = propane OR category = gas OR category = diesel orderby category;"
            cursor.execute(query)

        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity, creationDate from Resources_Requested natural inner join Resource_Type where category = smallbottles OR category = gallonbottles orderby category;"
            cursor.execute(query)
           
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity, creationDate from Resources_Requested natural inner join Resource_Type where category = %s orderby category;"
            cursor.execute(query,(keywords,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getCategoriesRequested(self):
        cursor = self.conn.cursor()
        result =[]
        query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type orderby category;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)        
        return result
    def getCategoryRequested_Qty(self, category,qty):
        cursor = self.conn.cursor()       
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity from Resources natural inner join Resource_Type where quantity = %s (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (qty,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity from Resources natural inner join Resource_type where quantity= %s (category = smallbottles OR category = gallonbottles) orderby category;"
            cursor.execute(query, (qty,))
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type where category = %s and quantity = %s orderby category;"
            cursor.execute(query, (category,qty))
        for row in cursor:
            result.append(row)        
        return result
    
    def getCategoryRequested_Price(self, category,price):
        cursor = self.conn.cursor()
        
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity from Resources_Requested natural inner join Resource_Type where price = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (price,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity from Resources_Requested natural inner join Resource_Type where price = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (price,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type where category = %s and price = %s orderby category;"
            cursor.execute(query, (category,price))
        for row in cursor:
            result.append(row)        
        return result

    def getCategoryRequested_City(self, category,city):
        cursor = self.conn.cursor()
        
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity from Resources_Requested natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (price,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_anme = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (price,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where category = %s and city_name = %s orderby category;"
            cursor.execute(query, (category,city))
        for row in cursor:
            result.append(row)        
        return result

    def getCategoryRequested_Region(self, category,region):
        cursor = self.conn.cursor()        
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity from Resources_Requested natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (price,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate , quantity from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (price,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, description, quantity, creationDate from Resources_Requested natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where category = %s and region_name = %s orderby category;"
            cursor.execute(query, (category,region))
        for row in cursor:
            result.append(row)        
        return result
       

###################################################################
#Resoruces Avaliable
################################################

    def getCategoryAvaliable(self, keywords):
        cursor = self.conn.cursor()
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_Type where category = propane OR category = gas OR category = diesel orderby category;"
       
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_type where category = smallbottles OR category = gallonbottles orderby category;"
           
        else:
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_type where category = %s orderby category;"
            cursor.execute(query,(keywords,) )
        result = []
        for row in cursor:
            result.append(row)        
        return result

    def getCategoriesAvaliable(self):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_Type  orderby category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
        def getCategoryAvaliable_Qty(self, category,qty):
            cursor = self.conn.cursor()
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type where quantity = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (qty,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type where quantity = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (qty,))          
        else:
            #Get Resources avaliable
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdatefrom Resources natural inner join Resource_Type where category = %s and quantity = %s orderby category;"
            cursor.execute(query, (category,qty,))
        result = []
        for row in cursor:
            result.append(row)
        #Get Resources requested
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_Type where quantity = %s (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (qty,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_type where quantity= %s (category = smallbottles OR category = gallonbottles) orderby category;"
            cursor.execute(query, (qty,))
        else:
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type where category = %s and quantity = %s orderby category;"
            cursor.execute(query, (category,qty))
        for row in cursor:
            result.append(row)        
        return result
    
    def getCategoryAvaliable_Price(self, category,price):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type where price = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (price,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type where price = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (price,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_Type where category = %s and price = %s orderby category;"
            cursor.execute(query, (category,price))
        result = []
        for row in cursor:
            result.append(row)
               
        return result

    def getCategoryAvaliable_City(self, category,city):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name  = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (city,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where city_name = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (city,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where category = %s and city_name = %s orderby category;"
            cursor.execute(query, (category,city))
        result = []
        for row in cursor:
            result.append(row)             
        return result

    def getCategoryAvaliable_Region(self, category,region):
        cursor = self.conn.cursor()
        #Get Resources avaliable
        if(keywords == 'water'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name  = %s and (category = propane OR category = gas OR category = diesel) orderby category;"
            cursor.execute(query, (region,))
        elif(keywords == 'fuel'):
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources_Requested natural inner join Resource_Type natural inner join Resource_Type  natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where region_name = %s and (category = smallbottles OR category = gallonbottles ) orderby category;"
            cursor.execute(query, (region,))          
        else:
            query = "Select name , Resource_Type.name as category, accountID, price, description,avaliability, quantity, creationDate,lastUpdate from Resources natural inner join Resource_Type natural inner join Accounts natural inner join Location natural inner join City natural inner join Region where category = %s and region_name = %s orderby category;"
            cursor.execute(query, (category,region))
        result = []
        for row in cursor:
            result.append(row)
       
            result.append(row)        
        return result
