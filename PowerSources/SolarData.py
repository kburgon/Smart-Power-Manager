import scrape
import pandas

# ----------------SOLAR------------------------

# Get the data for wind speed, wind direction, data dates, 
#   and sky cover in a tuple list
def getNoaaData():
    return scrape.getWeather()

# Get the GHI radiation from a solar data source (National Solar Radiation Data Base)
def getRawSolarRadiation():
    with open('SolarData.txt') as solarData:
        return [int(currentData) for currentData in solarData]

# Get a list of solar data after taking sky cover into account
# NOTE: This data is only sample data.  It doesn't come from the same time or source
def getSolarOutputWithWeather(rawSolarData, skyCoverData):
    dataList = []
    for dataIndex in range(0, int(min(len(skyCoverData), len(rawSolarData)))):
        dataList += [(1-float(skyCoverData[dataIndex]) / 100) * rawSolarData[dataIndex] / 4]
    return dataList

# Get the solar data needed to model a solar panel.
def getSolarOutputData():
    noaaData = getNoaaData()
    skyCoverData = [float(data.skyCover) / 100 for data in noaaData]
    solarRadiationData = getRawSolarRadiation()
    return getSolarOutputWithWeather(solarRadiationData, skyCoverData)


# --------------------- FIXED POWER ----------------------------------

# Get a dataset of the given power for the given number of days.
def getFixedHourlyOutput(daysOfOutput, power):
    return [power] * (12 * daysOfOutput)


# ------------------------ PLOT ---------------------------

# Draw a plot from the given set of data.
def plotData(outputData):
    p_data = pandas.Series(outputData)
    p_data.plot()