from flask import jsonify
import json

#List of the categories and their subcategories

category_list = ["medications","babyfood","cannedfood","dryfood","ice",
                "medicaldevices","tools","clothing","powergenerators","batteries"]
category_with_subcat_list = ["fuel","water"]
category_water_list = ["smallbottles", "gallonbottles"]
category_fuel_list = ["diesel","propane","gasoline"]


class category_ResourceDAO:

    def __init__(self):
        pass

    def getCategories(self):
        return "The Categoires are: \n {0} \n For the Category Water the subcategory are:\n {1} \n  For the Category fuel the subcategory are:\n {2} \n".format(category_list,category_water_list,category_fuel_list)

    def getCategoryRequested(self, keywords):
        if (keywords not in category_list):
            if(keywords not in category_with_subcat_list):
                return "Invalid Category {0} , Please Try Again".format(keywords)
            else:
                return "Show all resources from category {0}, with all the elements on subcategory together".format(keywords)
        return 'Show All Resources from Category'

    def getCategoryRequested_subcategory(self, keywords,subkeywords):
        if (keywords not in category_list):
            if(keywords not in category_with_subcat_list):
                return "Invalid Category {0} , Please Try Again".format(keywords)
            else:
                if(keywords == 'water'):
                    if(subkeywords not in category_water_list):
                        return "The subcategory: {0} is invalid, Please Try Again".format(subkeywords)
                    else:
                        return "Showing all elements in subcategory: {0}".format(subkeywords)
                elif(keywords == 'fuel'):
                    if(subkeywords not in category_fuel_list):
                        return "The subcategory:{0} is invalid, Please Try Again".format(subkeywords)
                    else:
                        return "Showing all elements in subcategory: {0}".format(subkeywords)                
                return "Show all resources from Sub-Category: {0}".format(subkeywords)
        return "Category {0} does not have any subcategory, Try Again".format(subkeywords)

    def getCategoryAvaliable(self, keywords):
        if (keywords not in category_list):
            if(keywords not in category_with_subcat_list):
                return "Invalid Category {0} , Please Try Again".format(keywords)
            else:
                return "Show all resources from category {0}, with all the elements on subcategory together".format(keywords)
        return 'Show All Resources from Category'

    def getCategoryAvaliable_subcategory(self, keywords,subkeywords):
        if (keywords not in category_list):
            if(keywords not in category_with_subcat_list):
                return "Invalid Category {0} , Please Try Again".format(keywords)
            else:
                if(keywords == 'water'):
                    if(subkeywords not in category_water_list):
                        return "The subcategory: {0} is invalid, Please Try Again".format(subkeywords)
                    else:
                        return "Showing all elements in subcategory: {0}".format(subkeywords)
                elif(keywords == 'fuel'):
                    if(subkeywords not in category_fuel_list):
                        return "The subcategory:{0} is invalid, Please Try Again".format(subkeywords)
                    else:
                        return "Showing all elements in subcategory: {0}".format(subkeywords)                
                return "Show all resources from Sub-Category: {0}".format(subkeywords)
        return "Category {0} does not have any subcategory, Try Again".format(subkeywords)



