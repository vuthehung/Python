import math
from collections import Counter

def prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            break
    return True

def solve():
    n = int(input())
    l = list(map(int, input().split()))
    cnt = Counter(l)
    for i in cnt:
        if prime(i):
            print(f"{i} {cnt[i]}")

def main():
    solve()

if __name__ == "__main__":
    main()