import math
def solve():
    n = int(input())
    l = list(map(int, input().split()))
    l_s = sorted(l)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if int(math.gcd(l_s[i], l_s[j])) == 1:
                print(f"{l_s[i]} {l_s[j]}")

def main():
    solve()

if __name__ == "__main__":
    main()