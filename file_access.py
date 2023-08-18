#import item functions
from Items import Items

def read_items():
    path = "items.txt"
    all_items = [] #new list all_items
    with open(path) as f:
        raw_items = f.readlines()
    for item in raw_items:
        sz, tp, cl, pc = item.split(",")
        item_obj = Items(sz.strip(), tp.strip(), cl.strip(), int(pc))
        all_items.append(item_obj)
    return all_items






