# Artur Meletyan
# 9/15/15
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
	def __init__(self, x = 0, y = 0, t = 0, d = 0, h = 0, F = 0, p = None):
		self.location = [x, y]
		self.topVal = t
		self.distanceToStart = d
		self.heuristic = h
		self.f = F
		self.parent = p
	
	# GETTERS
	def getLocation(self):
		return self.location
	
	def getTV(self):
		return self.topVal
	
	def getDistance(self):
		return self.distanceToStart
	
	def getH(self):
		return self.heuristic
	
	def getF(self):
		return self.f
	
	def getParent(self):
		return self.parent
	
	# SETTERS
	def setLocation(self, x, y):
		self.location = [x, y]
	
	def setTV(self, t):
		if t in range(0, 3):
			self.topVal = t
	
	def setDistance(self, d):
		self.distanceToStart = d
	
	def setH(self, h):
		self.heuristic = h
	
	def setF(self, F):
		self.f = F
	
	def setParent(self, p):
		self.parent = p

# Converts a 2D list into a graph
class Graph:
	def __init__(self, matrix):
		self.world = matrix
		self.numRow = len(matrix)
		self.numCol = len(matrix[0])
		for y in range(0, self.numRow):
			for x in range(0, self.numCol):
				#h = 10 * ((numCol - 1 - x) + (y))
				self.world[y][x] = Node(y, x, matrix[y][x])
	
	# GETTERS
	def getCoord(self, x, y):
		return self.world[x][y]
	
	def getNumRow(self):
		return self.numRow
	
	def getNumCol(self):
		return self.numCol


def aStar1(graph):
		
		# Obtain dimensions of the graph
		numRow = graph.getNumRow()
		numCol = graph.getNumCol()
		
		# Set start and end nodes
		start = graph.getCoord(numRow-1, 0)
		end = graph.getCoord(0, numCol-1)
		
		# Initialize traversable and nontraversable nodes
		travAble = []
		nonTravAble = []
		
		# Set cursor
		c = start.getLocation();
		
		# Add current node to traversable nodes list
		travAble.append(graph.getCoord(c[0],c[1]))
		
		return travAble[0].getH()
