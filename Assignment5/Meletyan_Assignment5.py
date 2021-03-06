# Artur Meletyan
# 10/4/15
# CSCI 3202 Assignment 5
#
# This program reads in a text file to create a graph then uses
# Markov Decision Processes to provide utility scores for possible
# paths across the world and the locations along the path.

# Equation variables
discount_factor = 0.9		# discount factor used for the infinite horizon model
epsilon = 0.5				# acceptable change threshold

# Reward values
mountains_reward = -1.0		# reward value of a "mountains" square
snakes_reward = -2.0		# reward value of a "snakes" square
barn_reward = 1.0			# reward value of a "barn" square
apple_reward = 50.0			# reward value of the "apple" or destination square

# Movement probabilities
success = 0.8				# chance that the intended move is the actual move
fail = 0.1					# chance that the actual move is to the right/left of the intended move

# Node class that represents a square in a given world
class Node:
	def __init__(self, location, value):
		self.location = location
		self.value = value
		if(value == 50):
			self.utility = 50
			self.reward = apple_reward
			self.moveOptimal = 'F'	# "Finish"
		else:
			self.utility = 0
			self.moveOptimal = ''
			if(value == 0):
				self.reward = 0
			if(value == 1):
				self.reward = mountains_reward
			if(value == 2):
				self.reward = 0
				self.moveOptimal = 'W'	# "Wall"
			if(value == 3):
				self.reward = snakes_reward
			if(value == 4):
				self.reward = barn_reward
	
	# GETTERS
	def getLocation(self):
		return self.location
	
	def getValue(self):
		return self.value
	
	def getUtility(self):
		return self.utility
	
	def getReward(self):
		return self.reward
		
	def getOptimalMove(self):
		return self.moveOptimal
	
	# SETTERS
	def setLocation(self, l):
		self.location = l
	
	def setValue(self, v):
		self.value = v
	
	def setUtility(self, u):
		self.utility = u
	
	def setReward(self, r):
		self.reward = r
	
	def setOptimalMove(self, o):
		self.moveOptimal = o

# Reads in a text file and converts it into a 2D list
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
			elif worldMatrix[y][x] == '1':
				worldMatrix[y][x] = 1
			elif worldMatrix[y][x] == '2':
				worldMatrix[y][x] = 2
			elif worldMatrix[y][x] == '3':
				worldMatrix[y][x] = 3
			elif worldMatrix[y][x] == '4':
				worldMatrix[y][x] = 4
			elif worldMatrix[y][x] == '50':
				worldMatrix[y][x] = 50
	
	return worldMatrix

# Converts a 2D list of integers into a world populated by nodes
def makeWorld(matrix):
	world = []
	numRow = len(matrix)
	for i in range(0, numRow):
		world.append([])
		numCol = len(matrix[i])
		for j in range(0, numCol):
			world[i].append(Node((j, i), matrix[i][j]))
	
	return world

# Sets the utility of a node in a 2D list of nodes and all possible moves from it
def setNodeUtility(world, i, j):
	node = world[i][j]
	utilityOld = node.getUtility()
	numRow = len(world)
	numCol = len(world[i])
	
	# Check if wall or finish
	if((node.getOptimalMove() == 'W')or(node.getOptimalMove() == 'F')):
		return None
	
	else:
		# Check down bound
		if((i + 1) >= numRow):
			down = 0
		else:
			down = world[i + 1][j].getUtility()
		
		# Check up bound
		if((i - 1) < 0):
			up = 0
		else:
			up = world[i - 1][j].getUtility()
			
		# Check right bound
		if((j + 1) >= numCol):
			right = 0
		else:
			right = world[i][j + 1].getUtility()
			
		# Check left bound
		if((j - 1) < 0):
			left = 0
		else:
			left = world[i][j - 1].getUtility()
		
		# Produce utilities for all possible moves for the transition model
		# 
		# Chance to successfully move in the intended direction:	80%
		# Chance to move to the left of the intended direction:		10%
		# Chance to move to the right of the intended direction:	10%
		moveUp = success * up + fail * left + fail * right
		moveDown = success * down + fail * left + fail * right
		moveRight = success * right + fail * up + fail * down
		moveLeft = success * left + fail * up + fail * down
		
		# Find the optimal move
		moveOptimal = max(moveUp, moveDown, moveRight, moveLeft)
		
		# Set the current node's utility according to its reward, position, and optimal move's reward
		node.setUtility(node.getReward() + discount_factor * moveOptimal)
		utilityNew = node.getUtility()
		
		# Set the current node's optimal move to the determined one
		if(moveOptimal == moveUp):
			node.setOptimalMove('U')
		elif(moveOptimal == moveRight):
			node.setOptimalMove('R')
		elif(moveOptimal == moveDown):
			node.setOptimalMove('D')
		elif(moveOptimal == moveLeft):
			node.setOptimalMove('L')
		
		return abs(utilityOld - utilityNew)

# Uses the value iteration algorithm for MDP to set optimal moves for world
def valueIteration(world, epsilon):
	delta = 1 + (epsilon * (1-discount_factor)/discount_factor)
	numRow = len(world)
	numCol = len(world[0])
	
	while(delta > epsilon * (1-discount_factor)/discount_factor):
		delta = 0
		for i in range(numRow-1, -1, -1):
			for j in range(numCol-1, -1, -1):
				deltaTemp = setNodeUtility(world, i, j)
				if(deltaTemp == None):
					deltaTemp = 0
				if(deltaTemp > delta):
					delta = deltaTemp

# Finds the optimal path in a given 2D list of nodes
def findOptimalPath(world):
	i = len(world)-1
	j = 0
	cursor = world[i][j]
	print("Location: "),
	print(len(world)-i-1, j),
	print("Utility: "),
	print(world[i][j].getUtility())
	while(cursor.getOptimalMove() != 'F'):
		move = cursor.getOptimalMove()
		if(move == 'D'):
			i += 1
		elif(move == 'U'):
			i -= 1
		elif(move == 'R'):
			j += 1
		elif(move == 'L'):
			i -= 1
		cursor = world[i][j]
		print("Location: "),
		print(len(world)-i-1, j),
		print("Utility: "),
		print(world[i][j].getUtility())

if __name__ == "__main__":
	# Gather user input
	# Python 2
	#world = raw_input("Enter the file you would like to use: ")
	# Python 3
	world = input("Enter the file you would like to use: ")
	print('')
	# Python 2
	#epsilon = float(raw_input("Enter the value of epsilon you would like to use: "))
	# Python 3
	epsilon = float(input("Enter the value of epsilon you would like to use: "))
	print('')
	
	# Commence valueIteration() and find the optimal path
	print("OPTIMAL PATH (including locations and utilities):")
	print('')
	world = makeWorld(generate(world))
	valueIteration(world, epsilon)
	findOptimalPath(world)
	
	# Print the world
	print('')
	print("WORLD (utility of each space):")
	print('')
	print("Note that these values do not change with epsilon.")
	print('')
	numRow = len(world)
	numCol = len(world[0])
	for i in range(0, numRow):
		for j in range(0, numCol):
			print("%.1f"%round(world[i][j].getUtility(), 1)),
			print('\t'),
			print(''),
		print('')
	
	# Print the world
	print('')
	print("WORLD (optimal move from each space):")
	print('')
	print("Note that these values change with epsilon.")
	print('')
	numRow = len(world)
	numCol = len(world[0])
	for i in range(0, numRow):
		for j in range(0, numCol):
			print(world[i][j].getOptimalMove()),
			print('\t'),
			print(''),
		print('')
