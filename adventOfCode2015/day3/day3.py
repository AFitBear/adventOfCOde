#day3
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y']) #laver et object af x og y

x="green"
print(x)

f = open("/home/afitbear/Private/randomCoding/adventOfCode2015/day3/input", "r") #data file

currentP = Point(0, 0)
roboP = Point(0, 0)

houses={currentP,roboP}
print(houses)

#switch int
switch=0
while True:
    ch =f.read(1)
    if ch=="":
        break
    if (switch%2)==1:
        if ch=="^":
            roboP=Point(roboP.x,roboP.y+1)
        elif ch=="v":
            roboP=Point(roboP.x,roboP.y-1)
        elif ch=="<":
            roboP=Point(roboP.x-1,roboP.y)
        elif ch==">":
            roboP=Point(roboP.x+1,roboP.y)
        houses.add(roboP)
    else:
        if ch=="^":
            currentP=Point(currentP.x,currentP.y+1)
        elif ch=="v":
            currentP=Point(currentP.x,currentP.y-1)
        elif ch=="<":
            currentP=Point(currentP.x-1,currentP.y)
        elif ch==">":
            currentP=Point(currentP.x+1,currentP.y)
        houses.add(currentP)
    switch+=1
print(len(houses))

#while True:
#    print