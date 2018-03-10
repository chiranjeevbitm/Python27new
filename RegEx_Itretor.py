import re
str = "We need to inform him with the leatest informations"
for i in re.finditer("inform.",str):
    locTuple=i.span()
    print(locTuple)