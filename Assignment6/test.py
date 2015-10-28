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
print("Pollution")
print(pollution.getChildren())
print("Smoker")
print(pollution.getChildren())
print("Cancer")
print(cancer.getParents())
print(cancer.getChildren())
print("X-Ray")
print(xray.getParents())
print("Dyspnoea")
print(dyspnoea.getParents())
