from myapi import API_Caller as apc

## Calculates the average cubic weight for the given category starting from given page
def calculate_average_cubic_weight(category, first_page = "1"):
    iter_api = apc(category, first_page)
    total_sum = 0
    # Iterate over pages - Memory efficient 
    for weight in iter_api:
        total_sum += weight
    average = total_sum/iter_api.item_count
    return average


if __name__ in "__main__":
    
    print("The average cubic weight of all Air Conditioners is {:.4f}".format(calculate_average_cubic_weight("Air Conditioners")))
