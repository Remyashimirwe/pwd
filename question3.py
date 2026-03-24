class Product:
    currency = "RWF"
    def __init__(self, name, price):
        self.name = name
        self.price = price
p1 = Product("juice", 1200)
p2 = Product("Fanta", 1000)
print("------before change ------")
print(p1.name, p1.price)
print(p2.name, p2.price)
print(Product.currency)
p1.price = 1500
Product.currency = "USD"
print("-----after change-----")
print(p1.name, p1.price)
print(p2.name, p2.price)
print(Product.currency)
