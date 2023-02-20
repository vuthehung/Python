def gt(n):
    res = 1
    for i in range(1, n + 1):   
        res *= i
    return res

def solve(n):
    s = str(n)
    res = 0
    for i in s:
        res += gt(int(i))
    return res == n

t = int(input())
for _ in range(t):
    n = int(input())
    if(solve(n)):
        print("Yes")
    else:
        print("No")