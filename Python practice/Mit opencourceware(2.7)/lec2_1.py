y = int(raw_input('Enter a number to check even or odd\n'))
if y%2==0:
    print 'even\n'
else:
    print 'odd\n'
    if y%3 != 0:
        print 'And not divisible by 3'
    
