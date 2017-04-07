import pandas

def getInteriorLoadData():
    with open('InteriorEquipmentLoad.txt') as loadData:
        return [float(currentData) * 10 for currentData in loadData]