class shoes:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def display(self):
        print("Name:", self.name)
        print("brand:", self.brand)
        print("Price:", self.price)

addidassamba = shoes("addidassamba", "addidas", "$1000.0")
addidassamba.display()