inventory = {
    "items": [],
    "capacity": 10,
    "locked": False,
}


def add_item(inventory, item):
    if inventory["locked"]:
        raise ValueError("Inventory is locked")

    if item == "":
        raise ValueError("Item cannot be empty")

    if len(inventory["items"]) >= inventory["capacity"]:
        raise ValueError("Inventory is full")

    inventory["items"].append(item)