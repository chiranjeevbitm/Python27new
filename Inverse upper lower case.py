name ="Chiranjeev"
name_list =[]

for i in name:
    if i.isupper():
        name_list.append(i.lower())
    elif i.islower():
        name_list.append(i.upper())
    else:
        name_list.append(i)
print ''.join(name_list)


