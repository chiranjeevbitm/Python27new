#import pdb
T = (0.1, 0.1)
x = 0.0
for i in range(len(T)):
    for j in T:
       x += i + j
       print x
print i
#pdb.set_trace()
