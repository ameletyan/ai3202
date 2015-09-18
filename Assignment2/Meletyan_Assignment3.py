# Artur Meletyan
# CSCI 3202 Assignment 3
#
# This program reads in a text file to create a graph then uses A*
# search to find the fastest route between one node and another on
# that graph.

# Function that reads in a text file and converts it into a graph
def generate(self, File):
	worldFile = open(File, 'r')
	worldMatrix = []
	for line in worldFile:
		worldMatrix.append(line)
	
	return worldMatrix
	

# Node class that represent a square in a given world
class Node:
	def __init__(self, x = 0, y = 0, d = 0, h = 0, F = 0, p = None):
		self.location = [x, y]
		self.distanceToStart = d
		self.heuristic = h
		self.f = F
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
	
	def setParent(self, p):
		self.parent = p


