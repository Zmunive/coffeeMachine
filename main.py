import os
import json


def getDataFromJason(fileName: str): 
    
    ext = ".json"
    ncoding = "utf-8"
    readData = "r"

    pathFile =  os.path.join(getCurrentPath,fileName + ext)
    
    with open(pathFile,readData,encoding=ncoding) as file:
        data = json.load(file)
    return data
    



getCurrentPath = os.getcwd()
coinsData = getDataFromJason("coins")
cookbookData = getDataFromJason("cookbook")
resourcesData = getDataFromJason("resources")

print(coinsData)
print(cookbookData)
print(resourcesData)

