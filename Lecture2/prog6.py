import math 

class Figure:
    def __init__(self, color, material):
        self.Color = color
        self.Material = material 




class Circle(Figure):
    def __init__(self, color, material, R):
        super().__init__(color, material)
        self.R = R 

    
    def perimeter(self):
        return math.pi*2*self.R


    def square(self):
        return math.pi*self.R**2


class Rectangle(Figure):
    def __init__(self, color, material, A,B):
        super().__init__(color, material)
        self.A = A
        self.B = B

    def perimeter(self):
        return 2*(self.A + self.B)

    def square(self):
        return self.A * self.B




