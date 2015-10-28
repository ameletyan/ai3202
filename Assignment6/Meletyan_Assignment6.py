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

import getopt, sys

# NODE CLASS
# - stores conditional probabilities for each node given its parents
# - possibly use a dictionary or previous implementation
class Node:
	def __init__(self, name):
		self.name = name
		self.cpt = {}		# conditional probability table
		self.parents = {}
		self.children = {}
		self.mp = 0			# marginal probability
	
	# GETTERS
	def getName(self):
		return self.name
		
	def getCPT(self):
		return self.cpt
	
	def getParents(self):
		return self.parents
	
	def getChildren(self):
		return self.children
	
	def getMP(self):
		return self.mp
	
	def getMPC(self):
		return self.mpc
		
	# SETTERS
	def setCPT(self, p = 0.9, s = 0.3):
		if(self.name == "Pollution"):
			self.cpt['P'] = p		# Low pollution
		elif(self.name == "Smoker"):
			self.cpt['S'] = s
		elif(self.name == "Cancer"):
			self.cpt['PS'] = 0.03
			self.cpt['P!S'] = 0.001
			self.cpt['!PS'] = 0.05
			self.cpt['!P!S'] = 0.02
		elif(self.name == "XRay"):
			self.cpt['C'] = 0.9		# X-Ray returns positive
			self.cpt['!C'] = 0.2
		elif(self.name == "Dyspnoea"):
			self.cpt['C'] = 0.65
			self.cpt['!C'] = 0.3
		else:
			self.cpt = {}
	
	def setMP(self, mpNew):
		self.mp = mpNew
	
	def setMPC(self, mpcNew):
		self.mpc = mpcNew
	
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
		self.nodes[node.getName()] = node
	
	# OTHER
	def setMarginalProbabilities(self):
		# Pollution
		pollution = self.nodes["Pollution"]
		pollution.setMP(pollution.getCPT()['P'])
		
		# Smoker
		smoker = self.nodes["Smoker"]
		smoker.setMP(smoker.getCPT()['S'])
		
		# Cancer
		cancer = self.nodes["Cancer"]
		cancerCPT = cancer.getCPT()
		p = pollution.getMP()
		s = smoker.getMP()
		cancer.setMP(cancerCPT['!PS']*(1-p)*s + cancerCPT['!P!S']*(1-p)*(1-s) + cancerCPT['PS']*p*s + cancerCPT['P!S']*p*(1-s))
		
		# X-Ray
		xray = self.nodes["XRay"]
		xrayCPT = xray.getCPT()
		c = cancer.getMP()
		xray.setMP(xrayCPT['C']*c + xrayCPT['!C']*(1-c))
		
		# Dyspnoea
		dyspnoea = self.nodes["Dyspnoea"]
		dyspnoeaCPT = dyspnoea.getCPT()
		dyspnoea.setMP(dyspnoeaCPT['C']*c + dyspnoeaCPT['!C']*(1-c))
	
	# NOTE: P(A|B) = P(B|A)*P(A)/P(B)
	# Diagnostic reasoning
	def diagnostic(self, prob, given, probTilda = False, givenTilda = False):
		probability = 0
		if((given in node.getParents().values())or(given in node.getParents().values().getParents().values())):
			print("Not diagnostic case")
		else:
			probability = 1
		return probability
	
	# Predictive reasoning
	def predictive(self, prob, given, probTilda = False, givenTilda = False):
		probability = 0
		if((given in node.getChildren().values())or(given in node.getChildren().values().getChildren().values())):
			print("Not predictive case")
		else:
			probability = 1
		return probability
	
	# Intercausal reasoning
	def intercausal(self):
		return 0
	
	# Combined reasoning
	def combined(self):
		return 0
					

if __name__ == "__main__":
	# Rhonda's code, have not gotten it to work yet
	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
		for o, a in opts:
			if o in ("-p"):
				print "flag", o
				print "args", a
				print a[0]
				print float(a[1:])
				#setting the prior here works if the Bayes net is already built
				#setPrior(a[0], float(a[1:])
			elif o in ("-m"):
				print "flag", o
				print "args", a
				print type(a)
				#calcMarginal(a)
			elif o in ("-g"):
				print "flag", o
				print "args", a
				print type(a)
				'''you may want to parse a here and pass the left of |
				and right of | as arguments to calcConditional
				'''
				p = a.find("|")
				print a[:p]
				print a[p+1:]
				#calcConditional(a[:p], a[p+1:])
			elif o in ("-j"):
				print "flag", o
				print "args", a
			else:
				assert False, "unhandled option"
