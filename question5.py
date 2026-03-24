class Item:
    total_items = 0
    
    def __init__(self, name,):
        self.name = name
        Item.total_items += 1 
p1 = Item("keys")
p2 =Item("Cars")
p3 = Item("sky")
p4 = Item.total_items
print(p4)