"""
>>> Q1: Define a Circle class to create a circle with radius r using the constructor.
Define ann Area()method of the class which calculate the area of the circle.
Define a Perimeter()method of the class which allows you to calculate the perimeter of the circle.
 """

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
               #3.14
         return 22/7 * self.radius ** 2  # Law:==> Amar kase radius ase to Shetar Area Hobe: (Pi r square)
    
    def perimeter(self):
                  #3.14
        return 2 * 22/7 * self.radius # Law:==> Amar kase radius abong area ase to Shetar Perimeter Hobe: (2 pi r)
    

c1 = Circle(21)
print("Area is",c1.area())
print("Perimeter is",c1.perimeter())
