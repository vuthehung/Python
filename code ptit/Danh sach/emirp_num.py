
import math

prime = []

def sang():
    for i in range(1000001):
        prime.append(1)
    prime[0] = 0
    prime[1] = 0
    for i in range(2, 1001):
        if prime[i] == 1:
            for j in range(i * i, 1000001, i):
                prime[j] = 0

def check(x):
    res = str(x)[::-1]
    return prime[x] == 1 and prime[int(res)] == 1 and int(res) != x

def solve():
    sang()
    t = int(input())
    for _ in range(t):
        n = int(input())
        res = []
        for i in range(13, n + 1):
            rev_i = int(str(i)[::-1])
            if check(i) and rev_i <= n and rev_i > i:
                res.append(i)
                res.append(rev_i)
        print(*res)
        
        
        
def main():
    solve()
if __name__ == "__main__":
    main()