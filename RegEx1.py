import re
Nameage= ''' Janice is 22 and Thanon is 33 Gabriel is 20 and Joey is 21'''

ages = re.findall(r'\d{1,3}',Nameage)
names = re.findall(r'[A-Z][a-z]*',Nameage)
ageDict = {}
x=0
for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1
print (ageDict)


