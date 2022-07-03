import math
class Rectangle:
    len=0
    breadth=0
    def __init__(self,len,breadth):
        self.len=len
        self.breadth=breadth
    def Area(self):
        return self.len*self.breadth
class Sqaure:
    side=0
    def __init__(self,side):
        self.side=side
    def Area(self):
        return math.pi*self.side*self.side
    
if __name__=='__main__':
    print("Class Createtion Started")
    rec=Rectangle(10,5)
    area=rec.Area()
    print("Area is "+str(area))
    sqr=Sqaure(5)
    print("Area of Square is "+str(sqr.Area()))