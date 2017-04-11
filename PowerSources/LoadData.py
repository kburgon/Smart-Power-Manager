import pandas

def getInteriorLoadData():
    with open('./Data/InteriorEquipmentLoad.txt') as loadData:
        return [float(currentData) * 10 for currentData in loadData]

def getDishwasherData():
    with open('./Data/DishWasher1.txt') as dwData:
        return [float(loadValue) for loadValue in dwData]

def getMicrowaveData():
    with open('./Data/Microwave2.txt') as mwData:
        return [float(loadValue) for loadValue in mwData]

def getKettleData():
    with open('./Data/Kettle1.txt') as ktData:
        return [float(loadValue) for loadValue in ktData]

def getFridgeData():
    with open('./Data/Fridge2.txt') as fData:
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
    