import math

prime = []
def sangNgto():
    for i in range(1000001):
        prime.append(1)

    prime[0] = 0
    prime[1] = 0

    for i in range(2, 1001):
        if prime[i] == 1:
            for j in range(i * i, 1000001, i):
                prime[j] = 0

sangNgto()
n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse= True)
mxNotNgto = 0
res = 0
for i in a:
    step = 0
    while(prime[i + step] == 0 and prime[i - step] == 0):
        step += 1
    res = max(res, step)
    
print(res)
