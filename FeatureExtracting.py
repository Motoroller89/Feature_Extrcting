
def FeatureExtracting_CN(personData):
    i = 0
    featureData = []
    while i < len(personData['event_type']):
        eventType = personData['event_type'][i]
        if eventType != 'mousedown':
            i += 1;
            continue
        timestamp_prev = personData['timestamp'][i]
        cn = 1; i2 = i + 1
        while i2 < len(personData['event_type']):
            timestamp = personData['timestamp'][i2]
            if (timestamp - timestamp_prev) > (g_value_SecondsAsRange * 1000):
                i = i2 - 1
            break
            if eventType == 'mousedown':
                if (timestamp - timestamp_prev) > (g_value_SecondsAsRange * 1000) or math.sqrt((x - x_prev) ** 2 + (y - y_prev) ** 2) > g_value_DistanceAsRange_CN:
                    i = i2 - 2
                    break
            cn += 1; i2 += 1
        featureData[g_featureName_CN].append(cn)
        i += 1
    return featureData



def FeatureExtracting_CD(PersonData):
    timecklick = []
    interval = []

    for i in range(len(PersonData['timestamp'])-1):
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000 and len(timecklick)!= 0 :
            interval.append(sum(timecklick) / len(timecklick))
            timecklick = []
        if PersonData['event_type'][i] == '!mousedown' and PersonData['event_type'][i + 1] == '!mouseup':
            timecklick.append(float(PersonData['timestamp'][i + 1]) - float(PersonData['timestamp'][i]))

    return interval  # значение по сесиям


def FeatureExtracting_MA(PersonData):
    k = 0
    old_v = 0
    users_temporary = []
    users_sesion =[]
    for i in range(len(PersonData['timestamp'])-1):
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000:
            users_sesion.append(sum(users_temporary)/k)
            users_temporary = []
            k = 0
        if PersonData['event_type'][i] != '!mousedown' or PersonData['event_type'][i] != '!mouseup':
            x1, y1 = float(PersonData['x'][i]), float(PersonData['y'][i])
            time1 = float(PersonData['timestamp'][i])
            x2, y2 = float(PersonData['x'][i+1]), float(PersonData['y'][i+1])
            time2 = float(PersonData['timestamp'][i+1])

            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                if v > old_v:
                    a = v / (time2 - time1)
                    users_temporary.append(a)
                old_v = v
                k += 1

    return users_sesion

def FeatureExtracting_MD(PersonData):
    k = 0
    old_v = 0
    users_temporary = []
    users_sesion =[]
    for i in range(len(PersonData['timestamp'])-1):
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000:
            users_sesion.append(sum(users_temporary)/k)
            users_temporary = []
            k = 0
        if PersonData['event_type'][i] != '!mousedown' or PersonData['event_type'][i] != '!mouseup':
            x1, y1 = float(PersonData['x'][i]), float(PersonData['y'][i])
            time1 = float(PersonData['timestamp'][i])
            x2, y2 = float(PersonData['x'][i+1]), float(PersonData['y'][i+1])
            time2 = float(PersonData['timestamp'][i+1])

            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                if v < old_v:
                    a = v / (time2 - time1)
                    users_temporary.append(a)
                old_v = v
                k += 1

    return users_sesion



def FeatureExtracting_MS(PersonData):
    users_sesion = []
    users_temporary = []
    for i in range(len(PersonData['timestamp'])-1):
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000:
            users_sesion.append(sum(users_temporary) / len(users_temporary))
            users_temporary = []
        if PersonData['event_type'][i] != '!mousedown' or PersonData['event_type'][i] != '!mouseup':
            x1, y1 = float(PersonData['x'][i]), float(PersonData['y'][i])
            time1 = float(PersonData['timestamp'][i])
            x2, y2 = float(PersonData['x'][i+1]), float(PersonData['y'][i+1])
            time2 = float(PersonData['timestamp'][i+1])

            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                users_temporary.append(v)

    return users_sesion


def FeatureExtracting_MU(PersonData):
    suma = 0
    mu = []
    massov_v = []


    for i in range(len(PersonData['timestamp'])-1):
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000:
            average_v = sum(massov_v) / len(massov_v)
            for i in range(len(massov_v)):
                suma += (massov_v[i] - average_v) ** 2
            mu.append((suma / len(massov_v)) ** 0.5)
            massov_v = []
            suma = 0


        if PersonData['event_type'][i] != '!mousedown' or PersonData['event_type'][i] != '!mouseup':
            x1, y1 = float(PersonData['x'][i]), float(PersonData['y'][i])
            time1 = float(PersonData['timestamp'][i])
            x2, y2 = float(PersonData['x'][i+1]), float(PersonData['y'][i+1])
            time2 = float(PersonData['timestamp'][i+1])

            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                massov_v.append(v)

    return mu








def FeatureExtracting_ALL(data):
    Feature_users = []
    for i in range(len(data)):
        season = dict()
        MA = FeatureExtracting_MA(data[i])
        MS = FeatureExtracting_MS(data[i])
        MU = FeatureExtracting_MU(data[i])
        CD = FeatureExtracting_CD(data[i])
        MD = FeatureExtracting_MD(data[i])
        CN = FeatureExtracting_CN(data[i])
        season.update({'FeatureExtracting_MA': MA, 'FeatureExtracting_MS' : MS,'FeatureExtracting_MU' : MU ,'FeatureExtracting_CD' : CD,'FeatureExtracting_MD' : MD, 'FeatureExtracting_CN' :CN})
        Feature_users.append(season)
    return Feature_users