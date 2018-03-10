def fibb(x):
    assert type(x)==int and x<=0
    if x==0 or x==1:
        return 1
    else:
        return fibb(x-1)+fibb(x-2)
fibb(5)