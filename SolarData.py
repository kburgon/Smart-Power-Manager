import scrape
import pandas

# ----------------SOLAR------------------------

# Get the data for wind speed, wind direction, data dates, 
#   and sky cover in a tuple list
def getNoaaData():
    return scrape.getWeather()

# Get the GHI radiation from a solar data source (National Solar Radiation Data Base)
def getRawSolarRadiation():
    with open('./Data/SolarData.txt') as solarData:
        return [int(currentData) for currentData in solarData]

# Get the solar data needed to model a solar panel.
# NOTE: This data is only sample data.  It doesn't come from the same time or source
def getSolarOutputData(efficiency=0.15, panelArea=25):
    noaaData = getNoaaData()
    skyCoverData = [float(data.skyCover) / 100 for data in noaaData]
    solarRadiationData = getRawSolarRadiation()
    dataList = []
    for dataIndex in range(0, int(min(len(skyCoverData), len(solarRadiationData)))):
        dataList += [(1-float(skyCoverData[dataIndex]) / 100) * solarRadiationData[dataIndex] * efficiency * panelArea]
    return dataList


# --------------------- FIXED POWER ----------------------------------

# Get a dataset of the given power for the given number of days.
def getFixedHourlyOutput(daysOfOutput, power):
    return [power] * (24 * daysOfOutput)


# ------------------------ PLOT ---------------------------

# Draw a plot from the given set of data.
def plotData(outputData):
    p_data = pandas.Series(outputData)
    p_data.plot()