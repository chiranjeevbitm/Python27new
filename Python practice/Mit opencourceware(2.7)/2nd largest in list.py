#if __name__ == '__main__':
    #n = int(raw_input())
    #arr = map(int, raw_input().split())
    #arr.remove(max(arr))
    #print max(arr)
   # arr.sort()
   # arr.sort()
   # set(arr)
    #print arr
   # print arr[n-2]

raw_input()
max = max2 = -101
for n in map(int,raw_input().split()):
    if n > max2:
        if n > max:
            max,max2 = n,max
        elif n < max:
            max2 = n
print(max2)