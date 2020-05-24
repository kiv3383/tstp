class Hexagon():
    def __init__(self, a):
        self.a = a

    def calculate_perimetr(self):
        return 6 * self.a


hexagon = Hexagon(2)
print(hexagon.calculate_perimetr())
