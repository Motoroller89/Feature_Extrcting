def FeatureExtracting_CN(personData): 
    i = 0
    featureData = []
    while i < len(personData['event_type']):
        eventType = personData['event_type'][i]
        if eventType != '!mousedown':
            i += 1
            continue
        timestamp_prev = personData['timestamp'][i]
        x1, y1 = float(personData['x'][i]), float(personData['y'][i])
        cn = 1
        i2 = i + 1
        while i2 < len(personData['event_type']):
            timestamp = personData['timestamp'][i2]
            x2, y2 = float(personData['x'][i2]), float(personData['y'][i2])
            if (int(timestamp) - int(timestamp_prev)) > 3000000:
                i = i2 - 1
                break
            if eventType == '!mousedown':
                if (int(timestamp) - int(timestamp_prev)) > 3000000: #or ((((x2-x1)**2) + ((y2-y1)**2))**0.5) > 30:
                    i = i2 - 2
                    break
                cn += 1
                i2 += 1
        featureData.append(cn)
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

    return interval


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




def crossing(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div != 0:
        return True
    else:
        return False

def FeatureExtracting_ON(PersonData): #проверить правильность работы
    i = 0
    k_on = []
    number_intersections = []
    while i < len(PersonData['event_type']):
        start1 = (float(PersonData['x'][i]),float(PersonData['y'][i]))
        i2 = i
        while PersonData['event_type'][i2] != '!mousedown' and i2+1 < len(PersonData['event_type']):
            i2 += 1
            continue
        end1 = (float(PersonData['x'][i2]),float(PersonData['y'][i2]))
        k = 0
        while i != i2:
            start2 = (float(PersonData['x'][i]),float(PersonData['y'][i]))
            i += 1
            end2 =  (float(PersonData['x'][i]),float(PersonData['y'][i]))
            if crossing((start1,end1),(start2,end2)) == True:
                k += 1
            if int(PersonData['timestamp'][i]) - int(PersonData['timestamp'][i-1]) > 3000000 and number_intersections != []:
                k_on.append(sum(number_intersections) / len(number_intersections))
                number_intersections = []
                k = 0
        i += 1
        number_intersections.append(k)
    return k_on


def FeatureExtracting_ME(PersonData): 
    i = 0
    driving_efficiency = []
    while i < len(PersonData['event_type']):
        start1 = (float(PersonData['x'][i]), float(PersonData['y'][i]))
        i2 = i
        k = 0
        while PersonData['event_type'][i2] != '!mousedown' and i2 + 1 < len(PersonData['event_type']):
            i2 += 1
            k +=1
            continue
        end1 = (float(PersonData['x'][i2]), float(PersonData['y'][i2]))
        suma = 0
        while i != i2:
            start2 = ((float(PersonData['x'][i]), float(PersonData['y'][i])))
            i += 1
            end2 = (float(PersonData['x'][i]), float(PersonData['y'][i]))
            suma += ((end2[0]-start2[0])**2 + (end2[1]-start2[1])**2)**0.5

        divider = ((((end1[0]-start1[0])**2) +(end1[1]-start1[1])**2) **0.5)
        if divider != 0:
            driving_efficiency.append(suma / divider)
        i += 1
    return driving_efficiency



def FeatureExtracting_OL(PersonData):
    i = 0
    max_ol = []
    while i < len(PersonData['event_type']):
        i2 = i
        while PersonData['event_type'][i2] != '!mousedown' and i2 + 1 < len(PersonData['event_type']):
            i2 += 1
            continue
        const = float(PersonData['x'][i2])
        max_ = (float(PersonData['x'][i2]))
        min_ = max_
        while i != i2:
            if (float(PersonData['x'][i])) > max_ :
                if max_ < float(PersonData['x'][i]):
                    max_ = float(PersonData['x'][i])
                if min_ > (float(PersonData['x'][i])):
                    min_ = float(PersonData['x'][i])
            i += 1
        if max_ - const > const - min_:
            max_ol.append(max_)
        else:
            max_ol.append(min_)
        i +=1
    return max_ol








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
        ON = FeatureExtracting_ON(data[i])
        ME = FeatureExtracting_ME(data[i])
        OL = FeatureExtracting_OL(data[i])
        season.update({'FeatureExtracting_MA': MA, 'FeatureExtracting_MS' : MS,'FeatureExtracting_MU' : MU ,'FeatureExtracting_CD' : CD,'FeatureExtracting_MD' : MD, 'FeatureExtracting_CN' :CN ,
                       'FeatureExtracting_ON': ON,'FeatureExtracting_ME': ME, 'FeatureExtracting_OL': OL})
        Feature_users.append(season)
    return Feature_users
