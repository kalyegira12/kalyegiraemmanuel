class Perfume:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def show(self):
        print("Name:", self.name)
        print("Size:", self.size)
        print("Price:", self.price)

pegasus = Perfume("Pegasus", "100ml", 200.0)
pegasus.show()












