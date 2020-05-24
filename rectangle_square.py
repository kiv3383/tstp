class Rectangle:
    rect = []
    def __init__(self, w, l):
        self.length = l
        self.width = w
        self.rect.append((self.length, self.width))

    def calculate_perimetr(self):
        return self.length * 2 + self.width * 2

    def print_size(self):
        print("{} на {}".format(self.length, self.width))


class Square:
    square_list = []
    
    def __init__(self, l):
        self.length = l
        self.square_list.append(self)
        

    def calculate_perimetr(self):
        return self.length * 4

    def __repr__(self):
        return ("{} на {} на {} на {}".format(self.length, self.length,self.length,self.length))


rec = Rectangle(10, 10)
sqr = Square(10)
print(rec.calculate_perimetr())
print(sqr.calculate_perimetr())
rec1 = Rectangle(20, 20)
rec2 = Rectangle(30, 30)
print(Rectangle.rect)
sqr1 = Square(20)
print(Square.square_list)
print(sqr1)
              
    
        
