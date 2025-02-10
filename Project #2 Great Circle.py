from math import acos, sin, cos, pi
print ("The Great Circle Calculator")
radius = float (input("Enter Radius of Sphere:  "))
x1 = float (input("Enter Starting point Latitude: ")) * pi / 180.0
y1 = float (input("Enter Starting Point Longitude: ")) * pi / 180.0
x2 = float (input("Enter Ending Point Latitude: ")) * pi / 180.0
y2 = float (input("Enter Ending Point Longitude:  ")) * pi / 180.0
distance = radius * acos( sin (x1)* sin (x2) + cos(x1) * cos (x2)* cos(y1 - y2) )
print (round(distance,2))

