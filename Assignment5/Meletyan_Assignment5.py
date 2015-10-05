# Artur Meletyan
# 10/4/15
# CSCI 3202 Assignment 5
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
epsilon = 0.5


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
		if(value == 50):
			self.utility = 50
			self.reward = 50
		else:
			self.utility = 0
			if(value == 0):
				self.reward = 0
			if(value == 1):
				self.reward = -1
			if(value == 2):
				self.reward = 0
			if(value == 3):
				self.reward = -2
			if(value == 4):
				self.reward = 1
	
	# GETTERS
	def getLocation(self):
		return self.location
	
	def getValue(self):
		return self.value
	
	def getUtility(self):
		return self.utility
	
	def getReward(self):
		return self.reward
	
	# SETTERS
	def setLocation(self, l):
		self.location = l
	
	def setValue(self, v):
		self.value = v
	
	def setUtility(self, u):
		self.utility = u
	
	def setReward(self, r):
		self.reward = r
		
# TESTING HUB
# Print World1MDP.txt as a 2D array
print("Raw World View")
world = generate("World1MDP.txt")
print(world)
print("")

# Print World1MDP.txt more presentably
print("Better World View")
for i in range(0,len(world)):
	for j in range(0,len(world[i])):
		print(world[i][j]),
	print("")
