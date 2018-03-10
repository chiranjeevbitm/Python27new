x=12345
epsilon = 0.01
low = 0.0
high=x
numGuess=0
ans = (low+high)/2.0
while  abs(ans**2 -x)>=epsilon and ans<=x:
    print 'ans=',ans,'low=',low,'high=',high
    numGuess+=1
    if ans**2<x:
        low = ans

    else:
        high=ans
ans=(high+low)/2.0
print  'numGuess=',numGuess
print ans,'is close to square root of',x