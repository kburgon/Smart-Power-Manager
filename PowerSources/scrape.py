import urllib2
import re
from BeautifulSoup import BeautifulSoup
from collections import namedtuple
import arrow

solarData = namedtuple("SolarData", "skyCover windDir windSpd date")
#                           " %sky cover, F, arrow"

site = 'http://forecast.weather.gov/MapClick.php?w3=sfcwind&w3u=1&w4=sky&w7=rain&w13u=0&w16u=1&w17u=1&AheadHour=*&Submit=Submit&FcstType=digital&textField1=41.8383&textField2=-111.8327&site=all&unit=0&dd=&bw='


# GETS THE WEATHER DATA FOR CLOUD COVER OFF THE WEB
def getWeather():
    #returns 6 days of weather data sampled each hour
    return getWeatherOnePage(0)+getWeatherOnePage(2)+getWeatherOnePage(4)

def getWeatherOnePage(daysAhead):
    #returns 48 hours of data
    url = site.replace('*', str(daysAhead*24)) 
    headers = {'User-Agent': 'Mozilla/5.0'} #headers
    req = urllib2.Request(url, None, headers)
    pageString = urllib2.urlopen(req, timeout=2).read() #added time out
    soup = BeautifulSoup(pageString)
    #print soup.prettify()
    table = soup.findAll("table", width=800)[2] #data table on page
    utc = arrow.utcnow()
    mst = utc.to('US/Mountain').replace(minute = 0, second = 0, microsecond = 0)
    # top half and bottom half of the table
    return getWeatherTable(table, 2,3,4,6, mst.clone().replace(days=+daysAhead)) + \
           getWeatherTable(table, 10,11,12,14, mst.clone().replace(days=+daysAhead+1))

def getWeatherTable(table, hourID, wSpdID, wDirID, skyID, mst):
    hourRow = table.findAll('tr')[hourID] #[2]
    windDirRow = table.findAll('tr')[wDirID] #[3]
    windSpdRow = table.findAll('tr')[wSpdID] #[4]
    skyRow = table.findAll('tr')[skyID] #[5]
    # get the colums
    skyColumns = skyRow.findAll('td')
    windDirColumns = windDirRow.findAll('td')
    hourColumns = hourRow.findAll('td')
    windSpdColumns = windSpdRow.findAll('td')
    # loop through each column and extract data
    solarList = []
    lastHour = 100
    addDay = False
    for i in range(1,len(skyColumns)): #start with 1
        hour = int(hourColumns[i].b.text)
        if lastHour == 23 and hour == 0: #roll over
            addDay = True
        dateTime = mst.clone().replace(hour = hour)
        if addDay:
            dateTime = dateTime.replace(days=+1)
        solarList.append(solarData(int(skyColumns[i].b.text), windDirColumns[i].b.text, int(windSpdColumns[i].b.text), dateTime))
        lastHour = hour
    return solarList

##sixDays = getWeather()
##for i in range(0, len(sixDays)):
##    print(sixDays[i].date.format('YYYY-MM-DD HH ')+str(sixDays[i].temp)+' '+str(sixDays[i].sky))
