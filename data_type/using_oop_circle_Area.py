import math

class Circle:
    def __init__(self,radius):
       self.radius=radius

    def calculator_circle_area(self):
        return math.pi * self.radius**2
       
radius=float(input("please Enter the radius:"))

circle=Circle(radius)
area=circle.calculator_circle_area()

print("Area  of the circle:",area)