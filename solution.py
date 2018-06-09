from myapi import API_Caller as apc

def calculate_average_volume(category, first_page = "1"):
    iter_api = apc(category, first_page)
    total_sum = 0
    for vol in iter_api:
        total_sum += vol 
    average = total_sum/iter_api.item_count
    return average


if __name__ in "__main__":
    
    print("The average volume of all Air Conditioners is {:.3f}".format(calculate_average_volume("Air Conditioners")))
