import csv
import os


def ReadfilesFrimDir_CSV(dirName="data"):
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


def FeatureExtracting_CN(PersonData):
    k = 0
    for i in range(len(PersonData['timestamp'])):
        if PersonData['event_type'][i] == '!mousedown' and PersonData['event_type'][i + 1] == '!mouseup':
            k += 1

    return k


def FeatureExtracting_CD(PersonData):
    timecklick = []
    for i in range(len(PersonData['timestamp'])):
        if PersonData['event_type'][i] == '!mousedown' and PersonData['event_type'][i + 1] == '!mouseup':
            timecklick.append(float(PersonData['timestamp'][i + 1]) - float(PersonData['timestamp'][i]))

    return int(sum(timecklick) / len(timecklick))


def acceleration(PersonData):
    s = []
    counter = 0
    dlina = len(PersonData['timestamp'])
    while counter < dlina:
        if PersonData['event_type'][counter] == '!mousedown' or PersonData['event_type'][counter] == '!mouseup':
            while PersonData['event_type'][counter] != '!mouseup':
                counter += 1

            else:
                counter += 1

        else:
            x1, y1 = float(PersonData['x'][counter]), float(PersonData['y'][counter])
            time1 = float(PersonData['timestamp'][counter])
            while PersonData['event_type'][counter] == '!mousemove':
                counter += 1
                if counter == dlina:
                    break

            x2, y2 = float(PersonData['x'][counter - 1]), float(PersonData['y'][counter - 1])
            time2 = float(PersonData['timestamp'][counter - 1])
            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                a = v / (time2 - time1)
                s.append(a)

    return sum(s) / len(s)


def FeatureExtracting_MS(PersonData):
    s = []
    counter = 0
    dlina = len(PersonData['timestamp'])
    while counter <dlina:
        if PersonData['event_type'][counter] == '!mousedown' or PersonData['event_type'][counter] == '!mouseup':
            while PersonData['event_type'][counter] != '!mouseup':
                counter += 1

            else:
                counter += 1

        else:
            x1, y1 = float(PersonData['x'][counter]), float(PersonData['y'][counter])
            time1 = float(PersonData['timestamp'][counter])
            while PersonData['event_type'][counter] == '!mousemove':
                counter += 1
                if counter == dlina:
                    break

            x2, y2 = float(PersonData['x'][counter - 1]), float(PersonData['y'][counter - 1])
            time2 = float(PersonData['timestamp'][counter - 1])
            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                s.append(v)

    return sum(s) / len(s)


dictionary = ReadfilesFrimDir_CSV('test1')
for i in range(len(dictionary)):
    d = FeatureExtracting_MS(dictionary[i])
    print(d)

