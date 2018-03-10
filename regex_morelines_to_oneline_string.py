import re
randstr = '''
Keep the Blues flag
flying high,
Team India..
'''
print (randstr)
regex = re.compile('\n')
randstr = regex.sub(" ",randstr)
print (randstr)
print ("*****************************************")

regex1 = re.compile('\b')
randstr1 = regex1.sub(" ",randstr)
print (randstr1)
print ("*****************************************")

regex = re.compile('\f')
randstr = regex.sub(" ",randstr)
print (randstr)
print ("*****************************************")

regex = re.compile('\r')
randstr = regex.sub(" ",randstr)
print (randstr)
print ("*****************************************")

regex = re.compile('\t')
randstr = regex.sub(" ",randstr)
print (randstr)
print ("*****************************************")

regex = re.compile('\v')
randstr = regex.sub(" ",randstr)
print (randstr)
print ("*****************************************")