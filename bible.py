class Bible:
    def __init__(self, version, color, price):
        self.version = version
        self.color = color
        self.price = price

    def see(self):
        print("version:", self.version)
        print("color:", self.color)
        print("Price:", self.price)

allsaints = Bible("NIV", "Black", "$20000.0")
allsaints.see()
