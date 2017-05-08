from simulator import simulator
import LearningAlgorithm as la
import pandas as pd

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


def getOptimalConfiguration():
    powerSimulator = simulator()
    results = la.getBestParameters(
        powerSimulator.runSimulation, 2, 0, 300, 0.01)

    with open('results.txt', 'w') as file:
        file.write(str(results))

    print(results[1][0])

    pd.Series(results[0]).plot()


def getConfigurationMatrix():
    powerSimulator = simulator()
    heatMatrix = [[powerSimulator.runSimulation([batteryCapacity / 100.0, panelArea / 100.0])
                   for batteryCapacity in xrange(0, 1001, 50)] for panelArea in xrange(0, 2001, 100)]

    with open('results.txt', 'w') as outFile:
        outFile.write(str(heatMatrix))
