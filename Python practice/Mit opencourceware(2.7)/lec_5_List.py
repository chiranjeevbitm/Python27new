##Cj = ['BIT', 'Cal Cj']
##Kal = ['Harvard', 'Yale', 'Brown']
##Unives = []
##Unives.append(Cj)
##print 'Unives =', Unives
##
##Unives.append(Kal)
##print 'Unives =',Unives
##for e in Unives:
##    print 'e = ' ,e
##
##flat = Cj + Kal
##print 'flat =', flat
##
##artSchools = ['RISD','Harvard']
##for u2 in artSchools:
##    if u2 in flat:
##        flat.remove(u2)
##print 'flat =' ,flat
##
##flat.sort()
##print 'flat =' ,flat
##flat[1] = 'UMass'
##print 'flat =' ,flat
##
##

def copyList(LBource,LDest):
    for e in LBource:
        LDest.append(e)
        print 'LDest =', LDest
L1 =[]
L2 = [1,2,3]
copyList(L1,L2)
print L1
print L2
#copyList(L1,L2)
