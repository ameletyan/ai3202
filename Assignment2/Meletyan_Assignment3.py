# Artur Meletyan
# CSCI 3202 Assignment 3
#
# This program reads in a text file to create a graph then uses A*
# search to find the fastest route between one node and another on
# that graph.

# Function that reads in a text file and converts it into a 2D list
def generate(File):
	worldFile = open(File, 'r')
	worldMatrix = []
	
	for line in worldFile:
		worldMatrix.append(line.rstrip('\n').split())
		
	numRow = len(worldMatrix)
	for y in range(0, numRow):
		numCol = len(worldMatrix[y])
		for x in range(0, numCol):
			if worldMatrix[y][x] == '0':
				worldMatrix[y][x] = 0
			if worldMatrix[y][x] == '1':
				worldMatrix[y][x] = 1
			if worldMatrix[y][x] == '2':
				worldMatrix[y][x] = 2
	
	return worldMatrix

# Node class that represent a square in a given world
class Node:
	def __init__(self, x = 0, y = 0, d = 0, h = 0, F = 0, t = 0, p = None):
		self.location = [x, y]
		self.distanceToStart = d
		self.heuristic = h
		self.f = F
		self.topVal = t
		self.parent = p
	
	# GETTERS
	def getLocation(self):
		return self.location
	
	def getDistance(self):
		return self.distanceToStart
	
	def getH(self):
		return self.heuristic
	
	def getF(self):
		return self.f
	
	def getTV(self):
		return self.topVal
	
	def getParent(self):
		return self.parent
	
	# SETTERS
	def setLocation(self, x, y):
		self.location = [x, y]
	
	def setDistance(self, d):
		self.distanceToStart = d
	
	def setH(self, h):
		self.heuristic = h
	
	def setF(self, F):
		self.f = F
	
	def gsetTV(self, t):
		if t in range(0, 3):
			self.topVal = t
	
	def setParent(self, p):
		self.parent = p

# Converts a 2D list into a graph
class Graph:
	def __init__(self, matrix):
		self.world = matrix
		numRow = len(matrix)
		for y in range(0, numRow):
			numCol = len(matrix[y])
			for x in range(0, numCol):
				h = 10 * ((numCol - 1 - x) + (y))
				self.world[y][x] = Node(y, x, 0, h, h, matrix[y][x])
	
	# GETTERS
	def getCoord(self, x, y):
		return self.world[x][y]
	
	# SETTERS
			
