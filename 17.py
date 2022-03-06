class Rectangle:

    def __init__(self):

        self.length=int(input("Enter the length: "))
        self.breadth=int(input("Enter the breadth: "))

    def area(self):

        return self.length*self.breadth

    def perimeter(self):

        return 2*(self.length+self.breadth)

    def compare(self,area1,area2):

        if(area1-area2!=0):
            return False
        else:
            return True


rec1=Rectangle()
rec2=Rectangle()

print("Area of Rectangle 1 : ",rec1.area())
print("Perimeter of Rectangle 1 : ",rec1.perimeter())

print("Area of Rectangle 2 : ",rec2.area())
print("Perimeter of Rectangle 2 : ",rec2.perimeter())

print("Is Both Rectangle's area similar? ",rec1.compare(rec1.area(),rec2.area()))
