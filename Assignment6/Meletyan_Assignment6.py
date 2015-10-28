# Artur Meletyan
# 10/4/15
# CSCI 3202 Assignment 6
#
# REQUIREMENTS:
# - handle queries from user joint, marginal, and conditional
#   probablities for any variable in the network
# - generate queries on command line using options and arguments
#   (easiest way to do this in Python is to use the getopt module
#   at https://docs.python.org/2/library/getopt.html)
# - option flags need to be the following:
#   1. "-g" for a conditional probability
#   2. "-m" for a marginal probability
#   3. "-p" to set a prior for either pollution or smoking
# - following each option will be variable abbreviations to
#   include in calculations which will be the following:
#   1. P = pollution
#   2. S = smoker
#   3. C = cancer
#   4. D = dyspnoea
#   5. X = x-ray
#   NOTE: lowercase letters stand for "Variable = True/Low/Positive"
#   NOTE: using '~' before the lower case letter stands for
#         "Variable = False/High/Negative"
#   NOTE: use the capital letter to return the probability
#         distribution for the variable
#   NOTE: for "-p", use P or S followed by the new numeric value
# - assume this program only needs to handle one calculation each
#   time it is run UNLESS setting different priors for smoking and
#   pollution and then also performing calculations
# GRADING:
# - needs to handle all calculations given in Table 2.2 of the
#   tutorial

# VARIABLES

# NODE CLASS
# - stores conditional probabilities for each node given its parents
# - possibly use a dictionary or previous implementation
class Node:
	def __init__(self, name, presence = True):
		self.name = name
		self.presence = presence
		self.cpt = {}
		self.parents = {}
		self.children = {}
	
	# GETTERS
	def getName(self):
		return self.name
		
	def getPresence(self):
		return self.presence
		
	def getCPT(self):
		return self.cpt
	
	def getParents(self):
		return self.parents
	
	def getChildren(self):
		return self.children
		
	# SETTERS
	# Set the Conditional Probability Table of a node depending on its name
	def setCPT(self, p = 0.9, s = 0.3):
		if(self.name == "Pollution"):
			self.cpt["P(P)"] = p		# Low pollution
			self.cpt["P(!P)"] = 1-p		# High pollution
		elif(self.name == "Smoker"):
			self.cpt["P(S)"] = s
			self.cpt["P(!S)"] = 1-s
		elif(self.name == "Cancer"):
			self.cpt["P(C|!P,S)"] = 0.05
			self.cpt["P(C|!P,!S)"] = 0.02
			self.cpt["P(C|P,S)"] = 0.03
			self.cpt["P(C|P,!S)"] = 0.001
			self.cpt["P(!C|!P,S)"] = 0.95
			self.cpt["P(!C|!P,!S)"] = 0.98
			self.cpt["P(!C|P,S)"] = 0.97
			self.cpt["P(!C|P,!S)"] = 0.999
		elif(self.name == "XRay"):
			self.cpt["P(X|C)"] = 0.9	# X-Ray returns positive
			self.cpt["P(X|!C)"] = 0.2
			self.cpt["P(!X|C)"] = 0.1	# X-Ray returns negative
			self.cpt["P(!X|!C)"] = 0.8
		elif(self.name == "Dyspnoea"):
			self.cpt["P(D|C)"] = 0.65
			self.cpt["P(D|!C)"] = 0.3
			self.cpt["P(!D|C)"] = 0.35
			self.cpt["P(!D|!C)"] = 0.7
		else:
			self.cpt = {}
	
	def setPresence(self, presenceNew):
		self.presence = presenceNew
	
	# ADDERS
		
	def addParent(self, node):
		self.parents[node.getName()] = node
	
	def addChild(self, node):
		self.children[node.getName()] = node

# Bayes Net
class BayesNet:
	def __init__(self):
		self.nodes = {}
	
	# GETTERS
	def getNodes(self):
		return self.nodes
	
	# ADDERS
	def addNode(self, node):
		self.nodes[node.getName] = node

if __name__ == "__main__":
	print(0)
