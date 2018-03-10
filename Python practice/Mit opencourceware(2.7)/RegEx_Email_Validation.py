import re
sampleEmails="sk@aol.com md@.com @sol.com dc@ com"
print "EmailMatches:",len(re.findall("[\w.%+_-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",sampleEmails))