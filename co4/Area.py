from Graphics.RectFunctions import*
from Graphics.DGraphics.SphereFunctions import*
from Graphics.DGraphics.CuboidFunctions import*
l=int(input("enter length"))
b=int(input("enter breadth"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle periemeter=",RectPerimeter(l,b))
r=int(input("enter a radius of circle"))
print("circle area=",SpArea(r))
print("circle periemeter",CirPeriemeter(r))
r=int(input("enter radius of sphere"))
print("sphere area=",SpArea(r))
print("sphere volumne",SpPeriemeter(r))
#cuboid
l=int(input("enter cuboid length"))
b=int(input("enter cuboid breadth"))
h=int(input("enter cuboid height"))
print("cuboid area=",CubArea(l,b,h))
print("cuboid periemeter",CubPeriemeter(l,b,h))


