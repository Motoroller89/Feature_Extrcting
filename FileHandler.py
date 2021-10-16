import  os
import  csv
import json


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
            json.dump(features[i], jsonFile)