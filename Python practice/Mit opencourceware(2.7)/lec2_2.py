x = int(raw_input('Enter  an Integer    '))
ans = 0
while ans*ans*ans < abs(x):
    ans = ans +1
    print 'current  guess =' , ans
if ans*ans*ans != abs(x):
    if x<0:
        ans = -ans
        print x, 'is not a perfect cube'
if ans*ans*ans == abs(x):
    print x, 'is  a perfect cube'
 
            
if x < 0:
        ans = -ans
        print 'cube root of ' + str(x) +' is ' + str(ans)
        
























































