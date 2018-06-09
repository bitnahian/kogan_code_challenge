import requests 
import json

## Awesome calculator that calucates the average volume of any category of
#  products
#  
#  API_LINK : http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com/api/products/

class API_Caller:

    ## class variable API_LINK - The link for which the API will be called
    API_LINK = http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com/api/products/

    ## The constructor
    def __init__(self, category):
        self.category = category
        self.page_count = 0
        self.next_page = 1

    def __iter__(self):
        self.page_count = 0
        self.next_page = 1
        return self

    def __next__(self):
        self.sum += self.

    def __callAPI(self):
        r = requests.get("".format(API_LINK, self.next_page))
        contents = r.json() # Convert to JSON
        objects = contents['objects']
        self.next_page = contents['next']
        volume_sum = 0
        for item in objects:
            if item['category'] == self.category:
                size = item['size']
                # Calculate volume of item and add to sum
                volume_sum += size['width']*size['length']*size['height']


