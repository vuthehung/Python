
import math

def prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1

def solve():
    n, m = map(int, input().split())
    mt = list()
    for _ in range(n):
        a = list(map(int, input().split()))
        mt.extend(a)
    for i in range(n * m):
        if prime(mt[i]):
            mt[i] = 1
        else:
            mt[i] = 0
    cnt = 0
    for i in range(n * m):
        cnt += 1
        print(mt[i], end=' ')
        if cnt == m:
            print()
            cnt = 0


def main():
    solve()

if __name__ == "__main__":
    main()