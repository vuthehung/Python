

test = int(input())
for j in range(test):
    k = int(input())
    n = input()+" "
    res = len(n)
    min1 = min2 = min3 = 10**18
    a = []
    l = r = 0
    while res>=10**4:
        r =l+ 10**4
        while n[r]!=' ':
            r -= 1
        s = n[l:r]
        a.append(s)
        l = r
        res -= len(s)
    if res>0:
        a.append(n[l:len(n)])
    for i in a:
        arr = [int(x) for x in i.split()]
        if min(arr) < min1:
            min2,min3 = min1,min2
            min1 = min(arr)
            arr.remove(min1)
        if  min(arr) < min2:
            min3 = min2
            min2 = min(arr)
            arr.remove(min2)
        if min(arr) < min3:
            min3 = min(arr)
            arr.remove(min3)
        del arr
    print(min1+min2+min3)