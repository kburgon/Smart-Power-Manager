import pandas

# This is data that gives usage of interior equipment.  It may not be useful, as
# it appears to be data for commercial buildings.

def getDishwasherData():
    with open('./Data/Washer1.csv') as dwData:
        return [float(loadValue) for loadValue in dwData]

def getMicrowaveData():
    with open('./Data/Microwave2.csv') as mwData:
        return [float(loadValue) for loadValue in mwData]

def getKettleData():
    with open('./Data/Kettle1.csv') as ktData:
        return [float(loadValue) for loadValue in ktData]

def getFridgeData():
    with open('./Data/Fridge2.csv') as fData:
        return [float(loadValue) for loadValue in fData]

def getTotalLoads():
    loads = [
        getDishwasherData(),
        getMicrowaveData(),
        getKettleData(),
        getFridgeData(),
    ]
    totalLoadList = []
    loadSizes = [len(loadPart) for loadPart in loads]
    for loadIndex in range(0, min(loadSizes)):
        totalLoad = sum([indLoad[loadIndex] for indLoad in loads])
        totalLoadList += [totalLoad]
    return totalLoadList
    