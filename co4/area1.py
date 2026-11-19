class Rect:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        ar=self.l* self.b
        return ar
    def perimeter(self):
        p=2*(self.l +self.b)
        return p
x1=int(input("enter length of 1st rectangle"))
y1=int(input("enter breadth of 1st rectangle"))
r1=Rect(x1,y1)
print("area of rectangle",r1.area())
print("periemeter of rectangle1:",r1.perimeter())
x2=int(input("enter length of 2st rectangle"))
y2=int(input("enter breadth of 2st rectangle"))
r2=Rect(x2,y2)
print("area of rectangle",r2.area())
print("periemeter of rectangle1:",r2.perimeter())
if r1.area()==r2.area():
    print("\n area of both rectangles are equal")
else:
    print("\n areas of both rectangles are not equal")


        
    
