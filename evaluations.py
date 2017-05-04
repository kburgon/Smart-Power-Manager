from simulator import simulator
import LearningAlgorithm as la
import pandas as pd

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

def getOptimalConfiguration():
	powerSimulator = simulator()
	return la.getBestParameters(powerSimulator.runSimulation, 2, 0, 10, 0.01)

results = getOptimalConfiguration()
with open('results.txt', 'w') as file:
	file.write(str(results))

print(results[1][0])

pd.Series(results[0]).plot()
