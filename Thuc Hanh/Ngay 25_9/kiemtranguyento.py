import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

n, m = map(int, input().split())
a = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)):
        if prime(tmp[i]):
            tmp[i] = 1
        else:
            tmp[i] = 0
    a.append(tmp)

for i in a:
    print(*i)
