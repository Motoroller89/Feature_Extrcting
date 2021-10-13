def kacpercky(a):
    if (a[0]== "k" or a[0]=='K') and (a[1]== "a" or a[1]=='A') and(a[2]== "s" or a[2]=='S') and(a[3]== "p" or a[3]=='P') and (a[4]== "e" or a[4]=='E') and (a[5]== "r" or a[5]=='R') and (a[6]== "s" or a[6]=='S') and (a[7]== "k" or a[7]=='K') and (a[8]== "y" or a[8]=='Y'):
        return  False
    else:
        return True

nomber = ''
a = input()
if len(a)>=10 and any([x.isdigit() for x in a]) and any([x.isupper() for x in a]):


