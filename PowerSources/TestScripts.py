import scrape
import pandas as pd

def getHourListFromData(scrapedData):
    return [data.date for data in scrapedData]

def getWindDirListFromData(scrapedData):
    return [data.windDir for data in scrapedData]

def getWindSpeedListFromData(scrapedData):
    return [data.windSpd for data in scrapedData]

def getSkyCoverListFromData(scrapedData):
    return [data.skyCover for data in scrapedData]

def getScrapedData():
    return scrape.getWeather()

def plotWindSpeed(scrapedData):
    timeIndex = pd.Series(getHourListFromData(scrapedData))
    windSpeedData = pd.Series(getWindSpeedListFromData(scrapedData), timeIndex)
    windSpeedData.plot()

def plotSkyCover(scrapedData):
    timeIndex = pd.Series(getHourListFromData(scrapedData))
    skyCoverData = pd.Series(getSkyCoverListFromData(scrapedData), timeIndex)
    skyCoverData.plot()