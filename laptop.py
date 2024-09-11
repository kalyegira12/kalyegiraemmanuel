class laptop:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def display(self):
        print("Name:", self.name)
        print("brand:", self.brand)
        print("Price:", self.price)

hpelite = laptop("hpelite", "HP", "$20000.0")
hpelite.display()
