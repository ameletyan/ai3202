# TEST FILE
from Meletyan_Assignment6 import *

# Pollution Node
print("Pollution Node")
pollution = Node("Pollution")
print("Printing name...   \n\t"),
print(pollution.getName())
pollution.setCPT()
print("Printing CPT...   \n\t"),
print(pollution.getCPT())
print("")

# Smoker Node
print("Smoker Node")
smoker = Node("Smoker")
print("Printing name...   \n\t"),
print(smoker.getName())
smoker.setCPT()
print("Printing CPT...   \n\t"),
print(smoker.getCPT())
print("")

# Cancer Node
print("Cancer Node")
cancer = Node("Cancer")
print("Printing name...   \n\t"),
print(cancer.getName())
cancer.setCPT()
print("Printing CPT...   \n\t"),
print(cancer.getCPT())
print("")

# X-Ray Node
print("X-Ray Node")
xray = Node("XRay")
print("Printing name...   \n\t"),
print(xray.getName())
xray.setCPT()
print("Printing CPT...   \n\t"),
print(xray.getCPT())
print("")

# Dyspnoea Node
print("Dyspnoea Node")
dyspnoea = Node("Dyspnoea")
print("Printing name...   \n\t"),
print(dyspnoea.getName())
dyspnoea.setCPT()
print("Printing CPT...   \n\t"),
print(dyspnoea.getCPT())
print("")

# Bayes Net
print("Bayes Net")
bn = BayesNet()
print("Adding nodes...")
bn.addNode(pollution)
print("Pollution added...")
bn.addNode(smoker)
print("Smoker added...")
bn.addNode(cancer)
print("Cancer added...")
bn.addNode(xray)
print("X-Ray added...")
bn.addNode(dyspnoea)
print("Dyspnoea added...")
print("All nodes added.\n")
print("Setting relationships...")
cancer.addParent(pollution)
pollution.addChild(cancer)
cancer.addParent(smoker)
smoker.addChild(cancer)
xray.addParent(cancer)
cancer.addChild(xray)
dyspnoea.addParent(cancer)
cancer.addChild(dyspnoea)
print("All relationships set.\n")
print("Printing all parents and children...")
print("Pollution (Children)")
print(pollution.getChildren().keys())
print("Smoker (Children)")
print(pollution.getChildren().keys())
print("Cancer (Parents and Children)")
print(cancer.getParents().keys())
print(cancer.getChildren().keys())
print("X-Ray (Parents)")
print(xray.getParents().keys())
print("Dyspnoea (Parents)")
print(dyspnoea.getParents().keys())
print("\nChecking Marginal Probabilities...")
bn.setMarginalProbabilities()
print("Pollution")
print(pollution.getMP())
print("Smoker")
print(smoker.getMP())
print("Cancer")
print(cancer.getMP())
print("X-Ray")
print(xray.getMP())
print("Dysnoea")
print(dyspnoea.getMP())
print("All relations and marginal probabilities processed\n")

# Predictive Reasoning
print("\nPredictive Reasoning")
print("P(!P|S): ", bn.predictive(pollution, smoker, True))
print("P(S|S): ", bn.predictive(smoker, smoker))
print("P(C|S): ", bn.predictive(cancer, smoker))
print("P(X|S): ", bn.predictive(xray, smoker))
print("P(D|S): ", bn.predictive(dyspnoea, smoker))
#print("P(C|!S): ", bn.predictive(cancer, smoker, False, True))
#print("P(C|!P): ", bn.predictive(cancer, pollution, False, True))

# Diagnostic Reasoning
print("\nDiagnostic Reasoning")
print("P(!P|D): ", bn.diagnostic(pollution, dyspnoea, True))
print("P(S|D): ", bn.diagnostic(smoker, dyspnoea))
print("P(C|D): ", bn.diagnostic(cancer, dyspnoea))
print("P(X|D): ", bn.diagnostic(xray, dyspnoea))
print("P(D|D): ", bn.diagnostic(dyspnoea, dyspnoea))

# Intercausal Reasoning
print("\nIntercausal Reasoning")
print("P(!P|C): ", bn.intercausal(pollution, cancer, None, True))
print("P(S|C): ", bn.intercausal(smoker, cancer))
print("P(C|C): ", bn.intercausal(cancer, cancer))
print("P(X|C): ", bn.intercausal(xray, cancer))
print("P(D|C): ", bn.intercausal(dyspnoea, cancer))

# Combined Reasoning

