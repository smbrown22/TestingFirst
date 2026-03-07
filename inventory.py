inventory = {
    "items":    [],           # list of item name strings
    "capacity": 10,          # maximum number of items allowed
    "locked":   False        # if True, inventory cannot be modified
}

def add_item(inventory, item):
    if len(items) > capacity:
        raise ValueError
    elif item == "":
        raise ValueError 
    elif locked:
        raise ValueError 
    
    