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
#   NOTE: lowercase letters stand for "Variable = True/Low"
#   NOTE: using '~' before the lower case letter stands for
#         "Variable = False/High"
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
	def __init__(self, cp = 0, parent = None):
		self.cp = cp
		self.parent = parent
	
	# GETTERS
	def getCP(self):
		return self.cp
	
	def getParent(self):
		return self.parent
	
	# SETTERS
	def setCP(self, cpNew):
		self.cp = cpNew
	
	def setParent(self, parentNew):
		self.parent = parentNew

# GRAPH CLASS? (BAYES NET)
