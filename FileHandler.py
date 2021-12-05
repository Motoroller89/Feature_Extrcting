import  os
import  csv
import json
import pandas as pd

def ReadFilesFromDir_CSV(dirName="data"):
    data = []
    filesName = os.listdir(dirName)
    appPath = os.getcwd()

    for filesName in filesName:
        tmpFileData = dict()
        filePath = appPath + "/" + dirName + "/" + filesName

        if os.path.isdir(filePath):
            continue

        with open(filePath, "r") as fileObject:
            dataInFile = csv.reader(fileObject, delimiter=',')
            tmpFileHeader = dataInFile.__next__()

            for i in range(len(tmpFileHeader)):
                tmpFileData[tmpFileHeader[i]] = []

            for row in dataInFile:
                for i in range(len(row)):
                    if tmpFileHeader[i] == 'g_dataColumnName_Timestamp' or \
                            tmpFileHeader[i] == 'g_dataColumnName_X' or \
                            tmpFileHeader[i] == 'g_dataColumnName_Y':
                        tmpFileData[tmpFileHeader[i]].append(int(float(row[i])))
                    else:
                        tmpFileData[tmpFileHeader[i]].append(row[i])

        tmpFileData['g_dataColumnName_PathToFile'] = filePath
        data.append(tmpFileData)
    return data


def WriteFeaturesToFiles_JSON(features, dirName="features"):
    appPath     = os.getcwd()
    pathToDir   = appPath + "/" + dirName + "/"

    try: os.mkdir(pathToDir)
    except Exception: pass

    for i in range(0,len(features)):
        name = pathToDir + str(i) + ".json"
        with open(name, "w") as jsonFile:
            json.dump(features[i], jsonFile,sort_keys= True, indent=4)



def ReadFiles_JSON(dirName):
    date = []
    list = os.listdir(dirName)
    number_files = len(list)

    for i in list:
        pd_json = pd.read_json(f'C:\\Users\\danya\\PycharmProjects\\mephi_mouse\\features\\{i}', orient='index')
        pd_json = pd_json.T

        date.append(pd_json)

    result = pd.concat(date)
    result.reset_index(drop=True, inplace=True)
    result =result.dropna(axis=1, how = 'all')
    return result
