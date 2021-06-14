class Circle:
    pi = 3.14
    #circel
    #area
    #circumference
    # c = circle(radius,value of pi)
    def __init__(self,radius):
        self.radius = radius
    def circumference(self):
        return 2*Circle.pi*self.radius
    def area(self):
        return self.pi*self.radius **2
c = Circle(2)
c1 = Circle(3)
print(c.circumference())
        