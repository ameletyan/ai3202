# Artur Meletyan
# 10/4/15
# CSCI 3202 Assignment 4
#
# This program reads in a text file to create a graph then uses
# Markov Decision Processes to provide utility scores for possible
# paths across the world and the locations along the path.
#
# Important variables:
discount_factor = 0.9
mountains_reward = -1.0
snakes_reward = -2.0
barn_reward = 1.0
apple_reward = 50.0


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
			if worldMatrix[y][x] == '3':
				worldMatrix[y][x] = 3
			if worldMatrix[y][x] == '4':
				worldMatrix[y][x] = 4
			if worldMatrix[y][x] == '50':
				worldMatrix[y][x] = 50
	
	return worldMatrix

# Node class that represent a square in a given world
class Node:
	def __init__(self, location, value):
		self.location = location
		self.value = value
	
	# GETTERS
	def getLocation(self):
		return self.location
	
	def getValue(self):
		return self.value
	
	# SETTERS
	def setLocation(self, loc):
		self.location = loc
	
	def setValue(self, val):
		self.value = val
		
# TESTING HUB
# Print World1MDP.txt as a 2D array
print(generate("World1MDP.txt"))
