# Artur Meletyan
# 11/5/2015
# CSCI 3202 Assignment 7
#
# This code is meant to analyze the samples given in the write-up.
#
# Sampling Legend:
# 
# 0	<=	u	<	0.5,	cloudy	=	true
# 0.5	<=	u	<	1,	cloudy	=	false

class BayesNet:
	def __init__(self):
		self.samples = [0.82, 0.56, 0.08, 0.81, 0.34, 0.22, 0.37, 0.99, 0.55, 0.61, 0.31, 0.66, 0.28, 1.0, 0.95, 0.71, 0.14, 0.1, 1.0, 0.71, 0.1, 0.6, 0.64, 0.73, 0.39, 0.03, 0.99, 1.0, 0.97, 0.54, 0.8, 0.97, 0.07, 0.69, 0.43, 0.29, 0.61, 0.03, 0.13, 0.14, 0.13, 0.4, 0.94, 0.19, 0.6, 0.68, 0.36, 0.67, 0.12, 0.38, 0.42, 0.81, 0.0, 0.2, 0.85, 0.01, 0.55, 0.3, 0.3, 0.11, 0.83, 0.96, 0.41, 0.65, 0.29, 0.4, 0.54, 0.23, 0.74, 0.65, 0.38, 0.41, 0.82, 0.08, 0.39, 0.97, 0.95, 0.01, 0.62, 0.32, 0.56, 0.68, 0.32, 0.27, 0.77, 0.74, 0.79, 0.11, 0.29, 0.69, 0.99, 0.79, 0.21, 0.2, 0.43, 0.81, 0.9, 0.0, 0.91, 0.01]
		self.C = 0.5		# P(C)
		self.SC = 0.1		# P(S|C)
		self.Sc = 0.5		# P(S|~C)
		self.RC = 0.8		# P(R|C)
		self.Rc = 0.2		# P(R|~C)
		self.WSR = 0.99		# P(W|S,R)
		self.WSr = 0.9		# P(W|S,~R)
		self.WsR = 0.9		# P(W|~S,R)
		self.Wsr = 0		# P(W|~S,~R)
	
	# GETTERS
	def getSamples(self):
		return self.samples
	
	def getC(self):
		return self.C
	
	def getSC(self):
		return self.SC
	
	def getSc(self):
		return self.Sc
	
	def getRC(self):
		return self.RC
	
	def getRc(self):
		return self.Rc
	
	def getWSR(self):
		return self.WSR
	
	def getWSr(self):
		return self.WSr
	
	def getWsR(self):
		return self.WsR
	
	def getWsr(self):
		return self.Wsr
	
	# SETTERS
	def setSamples(self, newSamples):
		self.samples = newSamples
	
	def setC(self, newC):
		self.C = newC
	
	def setSC(self, newSC):
		self.SC = newSC
	
	def setSc(self, newSc):
		self.Sc = newSc
	
	def setRC(self, newRC):
		self.RC = newRC
	
	def setRc(self, newRc):
		self.Rc = newRc
	
	def setWSR(self, newWSR):
		self.WSR = newWSR
	
	def setWSr(self, newWSr):
		self.WSr = newWSr
	
	def setWsR(self, newWsR):
		self.WsR = newWsR
	
	def setWsr(self, newWsr):
		self.Wsr = newWsr
	
	# OTHER
	# Takes four samples, returns list of condition Booleans
	def analyzeSamples(self, c, s, r, w):
		cloudy = False
		sprinkler = False
		rain = False
		wet = False
		
		# Analyze cloudy
		if(c < self.C):
			cloudy = True
		
		# Analyze sprinkler
		if(cloudy):
			if(s < self.SC):
				sprinkler = True
		else:
			if(s < self.Sc):
				sprinkler = True
		
		# Analyze rain
		if(cloudy):
			if(r < self.RC):
				rain = True
		else:
			if(r < self.Rc):
				rain = True
		
		# Analyze wet
		if((sprinkler)and(rain)):
			if(w < self.WSR):
				wet = True
		elif((sprinkler)and not(rain)):
			if(w < self.WSr):
				wet = True
		elif(not(sprinkler)and(rain)):
			if(w < self.WsR):
				wet = True
		elif(not(sprinkler)and not(rain)):
			if(w < self.Wsr):
				wet = True
		
		return [cloudy, sprinkler, rain, wet]

if __name__ == "__main__":
	bn = BayesNet()
	print(bn.getSamples())
