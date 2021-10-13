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

    return k #промахи


def FeatureExtracting_CD(PersonData):
    timecklick = []
    for i in range(len(PersonData['timestamp'])):
        if PersonData['event_type'][i] == '!mousedown' and PersonData['event_type'][i + 1] == '!mouseup':
            timecklick.append(float(PersonData['timestamp'][i + 1]) - float(PersonData['timestamp'][i]))

    return int(sum(timecklick) / len(timecklick))#значение по сесиям


def FeatureExtracting_MA(PersonData):
    suma = 0
    k = 0
    counter = 0
    dlina = len(PersonData['timestamp'])
    while counter+1 < dlina:
        if PersonData['event_type'][counter] == '!mousedown' or PersonData['event_type'][counter] == '!mouseup':
            while PersonData['event_type'][counter] != '!mouseup':
                counter += 1


            counter += 1

        else:
            while PersonData['event_type'][counter] == '!mousemove' and counter + 1 < dlina:
                x1, y1 = float(PersonData['x'][counter]), float(PersonData['y'][counter])
                time1 = float(PersonData['timestamp'][counter])
                counter += 1
                x2, y2 = float(PersonData['x'][counter]), float(PersonData['y'][counter])
                time2 = float(PersonData['timestamp'][counter])

                if time1 != time2:
                    ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                    v = ab / (time2 - time1)
                    suma += v / (time2 - time1)
                    k += 1

    return suma / k


def FeatureExtracting_MS(PersonData):
    s = []
    counter = 0
    dlina = len(PersonData['timestamp'])
    while counter+1 <dlina:
        if PersonData['event_type'][counter] == '!mousedown' or PersonData['event_type'][counter] == '!mouseup':
            while PersonData['event_type'][counter] != '!mouseup':
                counter += 1


            counter += 1

        else:

            while PersonData['event_type'][counter] == '!mousemove' and counter+1 < dlina:
                x1, y1 = float(PersonData['x'][counter]), float(PersonData['y'][counter])
                time1 = float(PersonData['timestamp'][counter])
                counter += 1
                x2, y2 = float(PersonData['x'][counter ]), float(PersonData['y'][counter])
                time2 = float(PersonData['timestamp'][counter ])


                if time1 != time2:
                    ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                    v = ab / (time2 - time1)
                    s.append(v)

    return sum(s) / len(s)



def FeatureExtracting_MU(PersonData):
    s = []
    counter = 9633
    suma = 0
    dlina = len(PersonData['timestamp'])
    while counter+1 < dlina:
        if PersonData['event_type'][counter] == '!mousedown' or PersonData['event_type'][counter] == '!mouseup':
            while PersonData['event_type'][counter] != '!mouseup':
                counter += 1


            counter += 1

        else:
            while PersonData['event_type'][counter] == '!mousemove' and counter+1 < dlina:
                x1, y1 = float(PersonData['x'][counter]), float(PersonData['y'][counter])
                time1 = float(PersonData['timestamp'][counter])
                counter += 1
                x2, y2 = float(PersonData['x'][counter ]), float(PersonData['y'][counter])
                time2 = float(PersonData['timestamp'][counter ])


                if time1 != time2:
                    ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                    v = ab / (time2 - time1)
                    s.append(v)


    average_v = sum(s) / len(s)

    for i in range(len(s)):
        suma += (s[i]-average_v)**2

    return (suma / len(s)) ** 0.5





dictionary = ReadfilesFrimDir_CSV('test1')

for i in range(len(dictionary)):
    # d ,d1,d2,d3 = FeatureExtracting_MS(dictionary[i]), FeatureExtracting_MA(dictionary[i]),FeatureExtracting_CD(dictionary[i]),FeatureExtracting_CN(dictionary[i])
    # print('v =',d,'a =',d1,'время нажатий =',d2,'количество нажатий =',d3)
    print(i+1," пользователь MS =",FeatureExtracting_MA(dictionary[i]))
    print(FeatureExtracting_MA(dictionary[i]))
