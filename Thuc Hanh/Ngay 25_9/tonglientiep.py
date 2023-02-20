import math

def solve(n):
    while n % 2 == 0:
        n //= 2
    res = 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            res *= (cnt + 1)
    if n > 1:
        res *= 2
    return res - 1
    

t = int(input())
for _ in range(t):
    n = int(input()) 
    print(solve(n))   