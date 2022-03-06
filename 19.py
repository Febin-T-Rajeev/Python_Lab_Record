class Rectangle:

    __length=None
    __width=None

    def __init__(self):
        self.__length=int(input("Enter length"))
        self.__width=int(input("Enter width"))

    def area(self):

        return self.__length*self.__width

    def compare(self,area1,area2):

        return area1<area2


r1=Rectangle()
r2=Rectangle()

r1area=r1.area()
r2area=r2.area()

print(r1area)
print(r2area)

if(r1.compare(r1area,r2area)==True):
    print("Area of rectangle 1 is less than rectangle 2")
else:
    print("Area of rectangle 1 is greater than rectangle 2")
    
