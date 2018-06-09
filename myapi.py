## @package myapi
#  This module contains the implementation of API_Caller
#
#  author: Nahian-Al Hasan


import requests 
import json

## Awesome API caller that can iterate over pages returned by the API call
#
#  Calculates the total cubic weight sum for the given category in each page
#  API_LINK : http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com/api/products/
class API_Caller:

    ## class variable API_LINK - The link for which the API will be called
    API_LINK = "http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com/api/products/"

    ## The constructor
    #   
    #  The default value of next_page is "1"
    def __init__(self, category, next_page = "1"):
        self.category = category
        self.item_count = 0
        self.next_page = "1"
    
    ## The iterator
    def __iter__(self):
        self.item_count = 0
        self.next_page = "1"
        return self

    ## The next method
    def __next__(self):
        if self.next_page is not None:
            return self.__callAPI()
        else:
            raise StopIteration

    ## The __callAPI method is used to calculate the sum of the volume from the  next page
    def __callAPI(self):
        r = requests.get("{}{}".format(self.API_LINK, self.next_page))
        contents = r.json() # Convert to JSON
        objects = contents['objects']
        # Set next_page to relevant value, None otherwise
        self.next_page = contents['next'][-1] if contents['next'] is not None else None
        cubic_weight_sum = 0
        for item in objects:
            if item['category'] == self.category:
                self.item_count += 1
                size = item['size']
                # Calculate volume of item and add to sum
                ratio = 1/1000000
                volume = size['width']*size['length']*size['height']*ratio # Convert to m^3
                cubic_weight_sum += volume * item['weight']
        return cubic_weight_sum

    ## @var item_count
    #  A member variable that keeps number of items encountered
    
    ## @var next_page
    #  A member variable that keeps track of the next page the API should call

