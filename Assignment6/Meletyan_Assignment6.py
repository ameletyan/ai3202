# Artur Meletyan
# 10/4/15
# CSCI 3202 Assignment 6
#
# As of the final commit before the due time, I was only able to get most of
# the code to work as assigned.  The details that I failed to implement are 
# the following:
#	- getting Prof. Hoenigman's "getopt" code to work, so no terminal stuff
#	- having predictive reasoning work for nodes that are not one node apart
#	- having diagnostic reasoning work for nodes that are not one node apart
#	- implementing the combined reasoning function
#	- removing smelly code (I used A LOT of conditionals)
#
# I think my biggest mistake was focusing too heavily on solving the math for
# this assignment.  I spent most of the time wrapping my head around the 
# equations, so I left myself very little time to actually code.  I assumed
# that the coding would be simpler once I figured out the math and though
# it was to an extent, it was not simple enough for me to finish it in the
# time that was left.  Nonetheless, I feel confident in my ability to analyze
# Bayesian Networks mathematically, so partial mission success!

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
	
	# Predictive reasoning
	def predictive(self, prob, given, probBang = False, givenBang = False):
		probability = 0
		if(prob == given):
			probability = 1
		else:
			enum = 0
			denom = 0
			parentMP1 = 1
			parentMP2 = 1
			cptKey1 = ''
			cptKey2 = ''
			
			for parent in prob.getParents().values():
				if(parent == given):
					cptKey1 = parent.getName()[0]
					parentMP1 = parent.getMP()
				else:
					cptKey2 = parent.getName()[0]
					parentMP2 = parent.getMP()
					
			for key in prob.getCPT().keys():
				enumTemp = 0
				denomTemp = 0
				if('!' + cptKey1 in key):
					if(givenBang):
						enumTemp += prob.getCPT()[key]
						denomTemp += 1 - enumTemp
						enumTemp *= 1 - parentMP1
						denomTemp *= 1 - parentMP1
						if('!' + cptKey2 in key):
							enumTemp *= 1 - parentMP2
							denomTemp *= 1 - parentMP2
						else:
							enumTemp *= parentMP2
							denomTemp *= parentMP2
						enum += enumTemp
						denom += denomTemp
				else:
					if(givenBang == False):
						enumTemp += prob.getCPT()[key]
						denomTemp += 1 - enumTemp
						enumTemp *= parentMP1
						denomTemp *= parentMP1
						if('!' + cptKey2 in key):
							enumTemp *= 1 - parentMP2
							denomTemp *= 1 - parentMP2
						else:
							enumTemp *= parentMP2
							denomTemp *= parentMP2
						enum += enumTemp
						denom += denomTemp
			
			denom += enum
			if(probBang):
				probability = 1 - (enum/denom)
			else:
				probability = enum/denom
			
		return probability
		
	# Diagnostic reasoning
	def diagnostic(self, prob, given, probBang = False, givenBang = False):
		probability = 0
		if(prob == given):
			probability = 1
		else:
			enum = 0
			denom = 0
			childMP1 = 1
			childMP2 = 1
			cptKey1 = ''
			cptKey2 = ''
			
			for child in prob.getChildren().values():
				if(child == given):
					cptKey1 = child.getName()[0]
					childMP1 = child.getMP()
				else:
					cptKey2 = child.getName()[0]
					childMP2 = child.getMP()
			
			
			for key in prob.getCPT().keys():
				enumTemp = 0
				denomTemp = 0
				if('!' + cptKey1 in key):
					if(givenBang):
						enumTemp += prob.getCPT()[key]
						denomTemp += 1 - enumTemp
						enumTemp *= 1 - childMP1
						denomTemp *= 1 - childMP1
						if('!' + cptKey2 in key):
							enumTemp *= 1 - childMP2
							denomTemp *= 1 - childMP2
						else:
							enumTemp *= childMP2
							denomTemp *= childMP2
						enum += enumTemp
						denom += denomTemp
				else:
					if(givenBang == False):
						enumTemp += prob.getCPT()[key]
						denomTemp += 1 - enumTemp
						enumTemp *= childMP1
						denomTemp *= childMP1
						if('!' + cptKey2 in key):
							enumTemp *= 1 - childMP2
							denomTemp *= 1 - childMP2
						else:
							enumTemp *= childMP2
							denomTemp *= childMP2
						enum += enumTemp
						denom += denomTemp
			
			denom += enum
			if(probBang):
				probability = 1 - (enum/denom)
			else:
				probability = enum/denom
			
			
		return probability
	
	# Intercausal reasoning
	def intercausal(self, prob, given1, given2 = None, probBang = False, givenBang1 = False, givenBang2 = False):
		probability = 0
		if(given2 == None):
			if(prob == given1):
				probability = 1
			elif(given1 in prob.getChildren().values()):
				probPG = self.predictive(given1, prob, givenBang1, probBang)
				
				if(probBang == True):
					probPMP = 1 - prob.getMP()
				else:
					probPMP = prob.getMP()
				
				if(givenBang1 == True):
					probGMP = 1 - given1.getMP()
				else:
					probGMP = given1.getMP()
				
				probability = probPG * probPMP / probGMP
			else:
				probability = self.diagnostic(prob, given1, probBang, givenBang1)
		else:
			if((prob == given1)or(prob == given2)):
				probability = 1
			elif((given1.getChildren().values() == prob.getChildren().values())or(given2.getChildren().values() == prob.getChildren().values())):
				if(given1.getChildren().values() == prob.getChildren().values()):
					enum = 0
					denom = 0
					mp1 = given1.getMP()
					mp2 = prob.getMP()
					cptKey1 = given1.getName()[0]
					cptKey2 = prob.getName()[0]
					
					for key in given2.getCPT().keys():
						if(('!' + cptKey1 in key)and('!' + cptKey2 in key)):
							if(givenBang1 and probBang):
								enum += given2.getCPT()[key] * (1-mp1) * (1-mp2)
							if(givenBang1 and ~probBang):
								denom += given2.getCPT()[key] * (1-mp1) * (1-mp2)
						elif('!' + cptKey1 in key):
							if(givenBang1):
								enum += given2.getCPT()[key] * (1-mp1) * mp2
							if(givenBang1 and ~probBang):
								denom += given2.getCPT()[key] * (1-mp1) * mp2
						elif('!' + cptKey2 in key):
							if(probBang):
								enum += given2.getCPT()[key] * mp1 * (1-mp2)
							if(givenBang1 and ~probBang):
								denom += given2.getCPT()[key] * mp1 * (1-mp2)
						else:
							if((givenBang1 == False)and(probBang == False)):
								enum += given2.getCPT()[key] * mp1 * mp2
							if(~probBang):
								denom += given2.getCPT()[key] * mp1 * mp2
					
					denom += enum
					probability = enum/denom
				elif(given2.getChildren().values() == prob.getChildren().values()):
					enum = 0
					denom = 0
					mp1 = given2.getMP()
					mp2 = prob.getMP()
					cptKey1 = given2.getName()[0]
					cptKey2 = prob.getName()[0]
					
					for key in given1.getCPT().keys():
						if(('!' + cptKey1 in key)and('!' + cptKey2 in key)):
							if(givenBang2 and probBang):
								enum += given1.getCPT()[key] * (1-mp1) * (1-mp2)
							if(givenBang2 and ~probBang):
								denom += given1.getCPT()[key] * (1-mp1) * (1-mp2)
						elif('!' + cptKey1 in key):
							if(givenBang2):
								enum += given1.getCPT()[key] * (1-mp1) * mp2
							if(givenBang2 and ~probBang):
								denom += given1.getCPT()[key] * (1-mp1) * mp2
						elif('!' + cptKey2 in key):
							if(probBang):
								enum += given1.getCPT()[key] * mp1 * (1-mp2)
							if(givenBang2 and ~probBang):
								denom += given1.getCPT()[key] * mp1 * (1-mp2)
						else:
							if((givenBang2 == False)and(probBang == False)):
								enum += given1.getCPT()[key] * mp1 * mp2
							if(~probBang):
								denom += given1.getCPT()[key] * mp1 * mp2
					
					denom += enum
					probability = enum/denom
			else:
				if(given1 in given2.getChildren().values()):
					probability = self.diagnostic(prob, given1, probBang, givenBang1)
				else:
					probability = self.diagnostic(prob, given2, probBang, givenBang2)
				
		return probability
	
	# Combined reasoning
	def combined(self, prob, given1, given2, probBang = False, givenBang1 = False, givenBang2 =False):
		probability = 0
		if((prob == given1)or(prob == given2)):
			probability = 1
		else:
			# check parameter node that is the youngest
			# set conditional with probability of the youngest given the next youngest
			# unroll probability from there with given information
			# For example:
			#	P(C|D,S) = P(C,D,S)/P(D,S) = 
			#	(P(D|C)*P(C|P,S)*P(P)*P(S) + P(D|C)*P(C|!P,S)*P(!P)*P(S))/
			#	(P(D|C)*P(C|P,S)*P(P)*P(S) + P(D|C)*P(C|!P,S)*P(!P)*P(S) + 
			#	P(D|!C)*P(!C|P,S)*P(P)*P(S) + P(D|!C)*P(!C|!P,S)*P(!P)*P(S))
			#
			# Unfortunately, I ran out of time before I could implement this.
		return probability
					

if __name__ == "__main__":
	# Prof. Hoenigman's code, have not gotten it to work yet
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
