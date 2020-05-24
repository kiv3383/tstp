import math


class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c)/2
        pre_s = p * (p-self.a) * (p-self.b) * (p-self.c)
        return math.sqrt(pre_s)


triangle = Triangle(10, 10, 10)
print(triangle.area())
