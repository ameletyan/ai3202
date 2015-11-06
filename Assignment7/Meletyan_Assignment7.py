# Artur Meletyan
# 11/5/2015
# CSCI 3202 Assignment 7
#
# This code is meant to analyze the samples given in the write-up.
#
# Sampling Legend:
# 
# 0		<=	u	<	0.5,	cloudy	=	true
# 0.5	<=	u	<	1,		cloudy	=	false

# Bayesian Network that carries all of the conditional probabilities
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
	
	# Takes four samples, returns list of condition Booleans
	def analyzeSample(self, c, s, r, w):
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
	
	# Runs analyzeSample() on self.samples, returns list of lists
	def analyzeSelf(self):
		results = []
		for i in range(0, 100, 4):
			results.append(self.analyzeSample(self.samples[i], self.samples[i+1], self.samples[i+2], self.samples[i+3]))
		return results

# MAIN
if __name__ == "__main__":
	bn = BayesNet()
	results = bn.analyzeSelf()
	
	C = 0.0			# P(C)
	CR = 0.0		# P(C|R)
	SW = 0.0		# P(S|W)
	SCW = 0.0		# P(S|C,W)
	
	# Legend:
	#	results[i][0] = cloudy
	#	results[i][1] = sprinkler
	#	results[i][2] = rain
	#	results[i][3] = wet
	
	for i in range(25):
		if(results[i][0]):						# Cloudy?
			C += 1								# If yes, add 1
		
		if(results[i][2]):						# Rain?
			if(results[i][0]):					# Cloudy?
				CR += 1							# If yes to both, add 1
		
		if(results[i][3]):						# Wet?
			if(results[i][1]):					# Sprinkler?
				SW += 1							# If yes to both, add 1
		
		if(results[i][0] and results[i][3]):	# Cloudy and Wet?
			if(results[i][1]):					# Sprinkler?
				SCW += 1						# If yes to all, add 1
	
	total = len(results)
	# Prior Sampling Results
	print("\nPrior Sampling Results")
	print("P(C):\t\t"),
	print(C/total)
	print("P(C|R):\t\t"),
	print(CR/total)
	print("P(S|W):\t\t"),
	print(SW/total)
	print("P(S|C,W):\t"),
	print(SCW/total)
	
	rejC = 0.0
	rejc = 0.0
	rejCR = 0.0
	rejcr = 0.0
	rejSW = 0.0
	rejsw = 0.0
	rejSCW = 0.0
	rejscw = 0.0
	
	for i in range(25):
		if(results[i][0]):							# Cloudy?
			rejC += 1								# If yes, add 1
		
		if(results[i][2]):							# Rain?
			if(results[i][0]):						# Cloudy?
				rejCR += 1							# If yes to both, add 1
		else:
			rejcr += 1								# If not Rain, remove 1 from total
		
		if(results[i][3]):							# Wet?
			if(results[i][1]):						# Sprinkler?
				rejSW += 1							# If yes to both, add 1
		else:
			rejsw += 1								# If not Wet, remove 1 from total
		
		if(results[i][0] and results[i][3]):		# Cloudy and Wet?
			if(results[i][1]):						# Sprinkler?
				rejSCW += 1							# If yes to all, add 1
		else:
			rejscw += 1								# If not Cloudy and Wet, remove 1 from total
	
	# Rejection Sampling Results
	print("\nRejection Sampling Results")
	print("P(C):\t\t"),
	print(rejC/total)
	print("P(C|R):\t\t"),
	print(rejCR/(total-rejcr))
	print("P(S|W):\t\t"),
	print(rejSW/(total-rejsw))
	print("P(S|C,W):\t"),
	print(rejSCW/(total-rejscw))
