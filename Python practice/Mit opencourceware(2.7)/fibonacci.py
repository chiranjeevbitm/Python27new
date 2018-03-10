def fibo(n):
    a=0
    b=1
    for x in range(n):
        a=b
        b=b+1
        print(a,'\n')

    return b
num = int(raw_input("Enter the value to find fibonacci series: "))
print(fibo(num))
