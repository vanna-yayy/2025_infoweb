class Retangulo:
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def calc_area(self):
        return self.b * self.h 
    def calc_diagonal(self):
        return (self.b **2 + self.h**2) ** 0.5
    def __str__(self):
        return f"Base = {self.b}, Altura = {self.h}, Area = { self.calc_area()}"