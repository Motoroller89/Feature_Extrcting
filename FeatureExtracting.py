import math

def FeatureExtracting_CN(personData): #при добавлении условия - бесконечный цикл
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
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000 and k != 0:
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
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000 and k != 0:
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
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000 and  len(users_temporary) != 0 :
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
        if int(PersonData['timestamp'][i+1]) - int(PersonData['timestamp'][i])> 3000000 and len(massov_v) != 0:
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

def FeatureExtracting_ON(PersonData):
    i = 0
    k_on = []
    number_intersections = []
    while i+1 < len(PersonData['event_type']):
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
    date_me = []
    while i+1 < len(PersonData['event_type']):
        if int(PersonData['timestamp'][i + 1]) - int(PersonData['timestamp'][i]) > 3000000 and driving_efficiency != []:
            date_me.append(sum(driving_efficiency) / len(driving_efficiency))
            driving_efficiency = []
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
            if i+1 < len(PersonData['event_type']):
                if int(PersonData['timestamp'][i + 1]) - int(PersonData['timestamp'][i]) > 3000000 and driving_efficiency != [] :
                    date_me.append(sum(driving_efficiency) / len(driving_efficiency))
                    driving_efficiency = []
                start2 = ((float(PersonData['x'][i]), float(PersonData['y'][i])))
                i += 1
                end2 = (float(PersonData['x'][i]), float(PersonData['y'][i]))
                suma += ((end2[0]-start2[0])**2 + (end2[1]-start2[1])**2)**0.5

            else:
                i+=1

        divider = ((((end1[0]-start1[0])**2) +(end1[1]-start1[1])**2) **0.5)
        if divider != 0:
            driving_efficiency.append(suma / divider)
        i += 1
    return date_me



def FeatureExtracting_OL(PersonData):
    i = 0
    max_ol = []
    date_ol = []
    while i+1 < len(PersonData['event_type']):
        if int(PersonData['timestamp'][i + 1]) - int(PersonData['timestamp'][i]) > 3000000 and max_ol != []:
            date_ol.append(sum(max_ol) / len(max_ol))
            max_ol = []
        i2 = i
        while PersonData['event_type'][i2] != '!mousedown' and i2 + 1 < len(PersonData['event_type']):
            i2 += 1
            continue
        const = float(PersonData['x'][i2])
        max_ = (float(PersonData['x'][i2]))
        min_ = max_
        while i != i2:
            if i+1 < len(PersonData['event_type']):
                if int(PersonData['timestamp'][i + 1]) - int(PersonData['timestamp'][i]) > 3000000 and max_ol != []:
                    date_ol.append(sum(max_ol) / len(max_ol))
                    max_ol = []
                if (float(PersonData['x'][i])) > max_ :
                    if max_ < float(PersonData['x'][i]):
                        max_ = float(PersonData['x'][i])
                    if min_ > (float(PersonData['x'][i])):
                        min_ = float(PersonData['x'][i])
                i += 1

            else:
                i += 1
        if max_ - const > const - min_:
            max_ol.append(max_)
        else:
            max_ol.append(min_)
        i +=1
    return date_ol


def FeatureExtracting_MSD_45(PersonData):
    i = 0
    users_sesion = []
    users_temporary = []
    degres = []
    while i < len(PersonData['event_type']):
        myradians = math.atan2(float(PersonData['y'][i]), float(PersonData['x'][i]))
        mydegrees = math.degrees(myradians)
        if 0<mydegrees<=45:
            degres.append(i+1)
        i +=1

    for j in range(len(degres) - 1):
        if int(PersonData['timestamp'][j + 1]) - int(PersonData['timestamp'][j]) > 3000000 and len(users_temporary) != 0 :
            users_sesion.append(sum(users_temporary) / len(users_temporary))
            users_temporary = []
        if PersonData['event_type'][j] != '!mousedown' or PersonData['event_type'][j] != '!mouseup':
            x1, y1 = float(PersonData['x'][j]), float(PersonData['y'][j])
            time1 = float(PersonData['timestamp'][j])
            x2, y2 = float(PersonData['x'][j + 1]), float(PersonData['y'][j + 1])
            time2 = float(PersonData['timestamp'][j + 1])
            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                users_temporary.append(v)


    return users_sesion


def FeatureExtracting_MSD_90(PersonData):
    i = 0
    users_sesion = []
    users_temporary = []
    degres = []
    while i < len(PersonData['event_type']):
        myradians = math.atan2(float(PersonData['y'][i]), float(PersonData['x'][i]))
        mydegrees = math.degrees(myradians)
        if 45<mydegrees<=90:
            degres.append(i+1)
        i +=1

    for j in range(len(degres) - 1):
        if int(PersonData['timestamp'][j + 1]) - int(PersonData['timestamp'][j]) > 3000000 and len(users_temporary) != 0 :
            users_sesion.append(sum(users_temporary) / len(users_temporary))
            users_temporary = []
        if PersonData['event_type'][j] != '!mousedown' or PersonData['event_type'][j] != '!mouseup':
            x1, y1 = float(PersonData['x'][j]), float(PersonData['y'][j])
            time1 = float(PersonData['timestamp'][j])
            x2, y2 = float(PersonData['x'][j + 1]), float(PersonData['y'][j + 1])
            time2 = float(PersonData['timestamp'][j + 1])
            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                users_temporary.append(v)


    return users_sesion


def FeatureExtracting_MSD_135(PersonData):
    i = 0
    users_sesion = []
    users_temporary = []
    degres = []
    while i < len(PersonData['event_type']):
        myradians = math.atan2(float(PersonData['y'][i]), float(PersonData['x'][i]))
        mydegrees = math.degrees(myradians)
        if 90<mydegrees<=135:
            degres.append(i+1)
        i +=1

    for j in range(len(degres) - 1):
        if int(PersonData['timestamp'][j + 1]) - int(PersonData['timestamp'][j]) > 3000000 and len(users_temporary) != 0:
            users_sesion.append(sum(users_temporary) / len(users_temporary))
            users_temporary = []
        if PersonData['event_type'][j] != '!mousedown' or PersonData['event_type'][j] != '!mouseup':
            x1, y1 = float(PersonData['x'][j]), float(PersonData['y'][j])
            time1 = float(PersonData['timestamp'][j])
            x2, y2 = float(PersonData['x'][j + 1]), float(PersonData['y'][j + 1])
            time2 = float(PersonData['timestamp'][j + 1])

            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                users_temporary.append(v)


    return users_sesion



def FeatureExtracting_MSD_180(PersonData):
    i = 0
    users_sesion = []
    users_temporary = []
    degres = []
    while i < len(PersonData['event_type']):
        myradians = math.atan2(float(PersonData['y'][i]), float(PersonData['x'][i]))
        mydegrees = math.degrees(myradians)
        if 135<mydegrees<=180:
            degres.append(i+1)
        i +=1

    for j in range(len(degres) - 1):
        if int(PersonData['timestamp'][j + 1]) - int(PersonData['timestamp'][j]) > 3000000 and len(users_temporary) != 0:
            users_sesion.append(sum(users_temporary) / len(users_temporary))
            users_temporary = []
        if PersonData['event_type'][j] != '!mousedown' or PersonData['event_type'][j] != '!mouseup':
            x1, y1 = float(PersonData['x'][j]), float(PersonData['y'][j])
            time1 = float(PersonData['timestamp'][j])
            x2, y2 = float(PersonData['x'][j + 1]), float(PersonData['y'][j + 1])
            time2 = float(PersonData['timestamp'][j + 1])
            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                users_temporary.append(v)

    return users_sesion



def FeatureExtracting_MSD_225(PersonData):
    i = 0
    users_sesion = []
    users_temporary = []
    degres = []
    while i < len(PersonData['event_type']):
        myradians = math.atan2(float(PersonData['y'][i]), float(PersonData['x'][i]))
        mydegrees = math.degrees(myradians)
        if -135<mydegrees<=-180:
            degres.append(i+1)
        i +=1

    for j in range(len(degres) - 1):
        if int(PersonData['timestamp'][j + 1]) - int(PersonData['timestamp'][j]) > 3000000 and len(users_temporary) != 0:
            users_sesion.append(sum(users_temporary) / len(users_temporary))
            users_temporary = []
        if PersonData['event_type'][j] != '!mousedown' or PersonData['event_type'][j] != '!mouseup':
            x1, y1 = float(PersonData['x'][j]), float(PersonData['y'][j])
            time1 = float(PersonData['timestamp'][j])
            x2, y2 = float(PersonData['x'][j + 1]), float(PersonData['y'][j + 1])
            time2 = float(PersonData['timestamp'][j + 1])
            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                users_temporary.append(v)


    return users_sesion

def FeatureExtracting_MSD_270(PersonData):
    i = 0
    users_sesion = []
    users_temporary = []
    degres = []
    while i < len(PersonData['event_type']):
        myradians = math.atan2(float(PersonData['y'][i]), float(PersonData['x'][i]))
        mydegrees = math.degrees(myradians)
        if -135<mydegrees<=-90:
            degres.append(i+1)
        i +=1

    for j in range(len(degres) - 1):
         if int(PersonData['timestamp'][j + 1]) - int(PersonData['timestamp'][j]) > 3000000 and len(users_temporary) != 0:
             users_sesion.append(sum(users_temporary) / len(users_temporary))
             users_temporary = []
         if PersonData['event_type'][j] != '!mousedown' or PersonData['event_type'][j] != '!mouseup':
             x1, y1 = float(PersonData['x'][j]), float(PersonData['y'][j])
             time1 = float(PersonData['timestamp'][j])
             x2, y2 = float(PersonData['x'][j + 1]), float(PersonData['y'][j + 1])
             time2 = float(PersonData['timestamp'][j + 1])
             if time1 != time2:
                 ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                 v = ab / (time2 - time1)
                 users_temporary.append(v)


    return users_sesion


def FeatureExtracting_MSD_315(PersonData):
    i = 0
    users_sesion = []
    users_temporary = []
    degres = []
    while i < len(PersonData['event_type']):
        myradians = math.atan2(float(PersonData['y'][i]), float(PersonData['x'][i]))
        mydegrees = math.degrees(myradians)
        if -90<mydegrees<=-45:
            degres.append(i+1)
        i +=1

    for j in range(len(degres)-1):

        if int(PersonData['timestamp'][j + 1]) - int(PersonData['timestamp'][j]) > 3000000 and len(users_temporary) != 0:
            users_sesion.append(sum(users_temporary) / len(users_temporary))
            users_temporary = []
        if PersonData['event_type'][j] != '!mousedown' or PersonData['event_type'][j] != '!mouseup':
            x1, y1 = float(PersonData['x'][j]), float(PersonData['y'][j])
            time1 = float(PersonData['timestamp'][j])
            x2, y2 = float(PersonData['x'][j + 1]), float(PersonData['y'][j + 1])
            time2 = float(PersonData['timestamp'][j + 1])
            if time1 != time2:
                ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                v = ab / (time2 - time1)
                users_temporary.append(v)


    return users_sesion


def FeatureExtracting_MSD_360(PersonData):
    i = 0
    users_sesion = []
    users_temporary = []
    degres = []
    while i < len(PersonData['event_type']):
        myradians = math.atan2(float(PersonData['y'][i]), float(PersonData['x'][i]))
        mydegrees = math.degrees(myradians)
        if -45<mydegrees<=0:
            degres.append(i+1)
        i +=1

    for j in range(len(degres) - 1):
         if int(PersonData['timestamp'][j + 1]) - int(PersonData['timestamp'][j]) > 3000000 and len(users_temporary) != 0:
             users_sesion.append(sum(users_temporary) / len(users_temporary))
             users_temporary = []
         if PersonData['event_type'][j] != '!mousedown' or PersonData['event_type'][j] != '!mouseup':
             x1, y1 = float(PersonData['x'][j]), float(PersonData['y'][j])
             time1 = float(PersonData['timestamp'][j])
             x2, y2 = float(PersonData['x'][j + 1]), float(PersonData['y'][j + 1])
             time2 = float(PersonData['timestamp'][j + 1])
             if time1 != time2:
                 ab = (((x2 - x1) ** 2) + ((y2 + y1) ** 2)) ** 0.5
                 v = ab / (time2 - time1)
                 users_temporary.append(v)


    return users_sesion


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
        MSD45 = FeatureExtracting_MSD_45(data[i])
        MSD90 = FeatureExtracting_MSD_90(data[i])
        MSD135 = FeatureExtracting_MSD_135(data[i])
        MSD180 = FeatureExtracting_MSD_180(data[i])
        MSD225 = FeatureExtracting_MSD_225(data[i])
        MSD270 = FeatureExtracting_MSD_270(data[i])
        MSD315 = FeatureExtracting_MSD_315(data[i])
        MSD360 = FeatureExtracting_MSD_360(data[i])
        season.update({'Person': [int(i+1)] * max(len(MA),len(MS),len(MU),len(CD),len(MD),len(CN),len(ON),len(ME),len(OL),len(MSD45),len(MSD90),len(MSD135),len(MSD180),
                                           len(MSD225),len(MSD270),len(MSD315),len(MSD360)),'FeatureExtracting_MA': MA, 'FeatureExtracting_MS' : MS,'FeatureExtracting_MU' : MU ,'FeatureExtracting_CD' : CD,'FeatureExtracting_MD' : MD, 'FeatureExtracting_CN' :CN ,
                       'FeatureExtracting_ON': ON,'FeatureExtracting_ME': ME, 'FeatureExtracting_OL': OL, 'FeatureExtracting_MSD45': MSD45,
                       'FeatureExtracting_MSD90': MSD90, 'FeatureExtracting_MSD135': MSD135,'FeatureExtracting_MSD180': MSD180,'FeatureExtracting_MSD225': MSD225,
                       'FeatureExtracting_MSD270': MSD270,'FeatureExtracting_MSD315': MSD315,'FeatureExtracting_MSD360': MSD360
                      })
        Feature_users.append(season)

    return Feature_users
