import random
import copy as cp

def simFunction(paramList):
	return paramList[0]**paramList[1] - paramList[2]/paramList[1] + paramList[3] - paramList[1]

def getRandomParams():
	baseVals = []
	for iteration in range(0, 4):
		random.seed()
		baseVals += [random.uniform(0, 100)]
	return baseVals


def generateConfigurations(paramList, variationAmount = 5):
	variations = []
	for changeIndex in xrange(0, len(paramList)):
		paramListCopyOne = cp.deepcopy(paramList)
		paramListCopyTwo = cp.deepcopy(paramList)
		paramListCopyOne[changeIndex] += variationAmount
		paramListCopyTwo[changeIndex] -= variationAmount

		if paramListCopyOne[changeIndex] > 100:
			paramListCopyOne[changeIndex] = 100
		if paramListCopyTwo[changeIndex] > 100:
			paramListCopyTwo[changeIndex] = 100

		if paramListCopyOne[changeIndex] < 0:
			paramListCopyOne[changeIndex] = 0.0001
		if paramListCopyTwo[changeIndex] < 0:
			paramListCopyTwo[changeIndex] = 0.0001

		variations += [paramListCopyOne]
		variations += [paramListCopyTwo]
	return variations


def createScoredList(configurationList):
	scoredList = []
	for configuration in configurationList:
		scoredList += [(abs(simFunction(configuration)), configuration)]
	return scoredList


def solveForZero(totalIterations):
	bestScoreList = []
	baseVals = [getRandomParams() for rep in xrange(5)]
	initialScore = map(simFunction, baseVals)
	allConfigurations = zip(initialScore, baseVals)
	# print(allConfigurations)

	for iteration in range(totalIterations):
		# configurationList = generateConfigurations(allConfigurations[0][1], random.uniform(0.1, 10))
		configurationList = generateConfigurations(allConfigurations[0][1], 0.5)
		allConfigurations += createScoredList(configurationList)
		allConfigurations = sorted(allConfigurations)[0:4]
		bestScoreList += [allConfigurations[0][0]]
	return bestScoreList
