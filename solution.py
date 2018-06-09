import requests 
import json

## Awesome calculator that calucates the average volume of any category of
#  products
#  
#  API_LINK : http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com/api/products/

class MyAwesomeCalculator:

    ## API_LINK - The link for which the API will be called
    API_LINK = http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com/api/products/

    ## The constructor
    def __init__(self, category):
        self.category = category
        self.next_page = 1
        self.sum = 0
        self.count = 0

    def __iter__(self):
        self.count = 0
        self.sum = 0
        self.next_page = 1
        return self

    def __next__(self):
        self.sum += self.

    def callAPI(next_page):
        r = requests.get(API_LINK + self.next_page)
        contents = r.json() # Convert to JSON
        objects = contents['objects']
        self.next_page = contents['next']

