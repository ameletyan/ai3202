# TEST FILE
from Meletyan_Assignment3 import *

a = Node(1,2,3,4,5)
print(a.getLocation())
print(a.getDistance())
print(a.getH())
print(a.getF())
print(a.getParent())

a.setLocation(6,7)
a.setDistance(8)
a.setH(9)
a.setF(10)
print(a.getLocation())
print(a.getDistance())
print(a.getH())
print(a.getF())

b = Node(11,12,13,14,15)
print(b.getLocation())
print(b.getDistance())
print(b.getH())
print(b.getF())
print(b.getParent())

b.setParent(a)
print(b.getParent())
print(b.getParent().getLocation())
print(b.getParent().getDistance())
print(b.getParent().getH())
print(b.getParent().getF())
print(b.getParent().getParent())

worldMatrix = generate('World1.txt')
print(worldMatrix)

world = Graph(worldMatrix)
print(world.getCoord(7,0).getH())

#worldStart = world.getCoord(7, 0)
#worldEnd = world.getCoord(0, 9)
#print(aStar1(world, worldStart, worldEnd))
