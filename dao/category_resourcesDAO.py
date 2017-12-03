from flask import jsonify
import json

category_list = ["medications","babyfood","cannedfood","dryfood","ice",
                "medicaldevices","tools","clothing","powergenerators","batteries"]
category_with_subcat_list = ["fuel","water"]
category_water_list = ["smallbottles", "gallonbottles"]
category_fuel_list = ["diesel","propane","gasoline"]


class category_ResourceDAO:

    def __init__(self):
        pass

    def getCategoryRequested(self, keywords):
        if (keywords not in category_list):
            if(keywords not in category_with_subcat_list):
                return 'Invalid Category Enter, Please Try Again'
            else:
                return 'Show all resources from category'    
        return 'Show All Resources from Category'
