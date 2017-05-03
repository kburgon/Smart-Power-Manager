import random
import copy as cp
import pandas as pa

# Takes a method that accepts a list of parameters and finds a set of parameters that 
# causes the method to return the target result.  This is the main method to call.
def getBestParameters(methodToFit, numberOfParameters, targetResult, solveIterations=100, variationAmount=1):
	bestResultsList = []
	baseParams = [getRandomParams(numberOfParameters) for params in xrange(10)]
	initialResults = map(methodToFit, baseParams)
	allConfigurationsList = zip(initialResults, baseParams)

	for iteration in xrange(solveIterations):
		configurationList = generateMutatedConfigurations(allConfigurationsList[0][1], variationAmount)
		
		for configuration in configurationList:
			allConfigurationsList += [scoreParamterList(configuration, methodToFit, targetResult)]

		allConfigurationsList = sorted(allConfigurationsList)[0:9]
		bestResultsList += [allConfigurationsList[0][0] + targetResult]
	return bestResultsList


# A sample method to use for testing the learning algorithm.
def simFunction(paramList):
	return paramList[0]**paramList[1] - paramList[2]/paramList[1] + paramList[3] - paramList[1]


# Generate a list of the given number of starting parameters.
def getRandomParams(numberOfParameters):
	baseVals = []
	for iteration in xrange(numberOfParameters):
		random.seed()
		baseVals += [random.uniform(0, 100)]
	return baseVals


# Create variances in the values of the given parameter list and return a list of 
# mutations of the original parameter list.
def generateMutatedConfigurations(paramList, variationAmount = 5):
	variations = []
	for changeIndex in xrange(0, len(paramList)):
		paramListCopyOne = cp.deepcopy(paramList)
		paramListCopyTwo = cp.deepcopy(paramList)
		paramListCopyOne[changeIndex] += variationAmount
		paramListCopyTwo[changeIndex] -= variationAmount

		# Set upper and lower bounds to the manipulated values.
		paramListCopyOne[changeIndex] = min(paramListCopyOne[changeIndex], 100)
		paramListCopyTwo[changeIndex] = min(paramListCopyTwo[changeIndex], 100)
		paramListCopyOne[changeIndex] = max(paramListCopyOne[changeIndex], 0.00001)
		paramListCopyTwo[changeIndex] = max(paramListCopyTwo[changeIndex], 0.00001)

		variations += [paramListCopyOne]
		variations += [paramListCopyTwo]
	return variations


# Run the given method to get a score on the parameter list and return a tuple
# of the parameter list and it's score
def scoreParamterList(parameterList, methodToFit, targetResult):
	return (abs(methodToFit(parameterList) - targetResult), parameterList)


if __name__ == '__main__':
	results = getBestParameters(simFunction, 5, 30, variationAmount=4)
	for indRes in results:
		print(indRes)
	pa.Series(results).plot()