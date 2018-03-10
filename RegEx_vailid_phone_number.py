import  re
phn = "444-122-1234"
if re.search("\d{3}-\d{3}-\d{4}",phn):
    print ("Valid phone number")
else:
    print ("Invalid phone number")