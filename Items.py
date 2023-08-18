class Items:
    def __init__(self, Size, Type, Color, Price):
        self.size = Size
        self.type = Type
        self.color = Color
        self.price = Price

    def __str__(self):
        return f"{self.type} {self.color}".title() +  f'({self.size})'.title() + f"- HK${self.price}"

    def isSize(self, size):
        if self.size.lower() == size.lower():
            return True
        else:
            return False
    def isPrice(self, price):
        if self.price == price:
            return True
        else:
            return False
    def isType(self, type):
        if self.type.lower() == type.lower():
            return True
        else:
            return False
    def isColor(self, color):
        if self.color.lower() == color.lower():
            return True
        else:
            return False

#available items for search

def get_color(all_items):
    available_colors = set()
    for item in all_items:
        available_colors.add(item.color)
    return available_colors

def get_size(all_items):
    available_size = set()
    for item in all_items:
        available_size.add(item.size)
    return available_size
def get_price(all_items):
    available_price = set()
    for item in all_items:
        available_price.add(item.price)
    return available_price
def get_type(all_items):
    available_type = set()
    for item in all_items:
        available_type.add(item.type)
    return available_type