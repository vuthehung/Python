import math


def solve():
    a, k, n = map(int, input().split())
    n = int(n / k) + 1
    res = -1
    for i in range(n):
        x = i * k - a
        if x > 0:
            res = 1
            print(x, end = ' ')
    if res == -1:
        print("-1")
def main():
    solve()

if __name__ == "__main__":
    main()