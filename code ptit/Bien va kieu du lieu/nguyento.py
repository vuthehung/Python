import math


def nguyento(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            break
    return True

def check(n, x):
    return int(math.gcd(n, x)) == 1

def solve():
    t = int(input())
    for _ in range(t):
        sum = 0
        n = int(input())
        for i in range(n):
            if check(n, i):
                sum += 1
        if nguyento(sum):
            print("YES")
        else:
            print("NO")

def main():
    solve()
if __name__ == "__main__":
    main()