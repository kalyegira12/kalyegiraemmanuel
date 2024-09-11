class wine:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

    def display(self):
        print("Name:", self.name)
        print("year:", self.year)
        print("Price:", self.price)

rosaho = wine("rosaho", "1920", "$1000.0")
rosaho.display()