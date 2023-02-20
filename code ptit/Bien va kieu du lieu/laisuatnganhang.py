
import math

def solve():
    t = int(input())
    for _ in range(t):
        n, x, m = map(float, input().split())
        year = math.log(m/n, 1 + x/100)
        if year == int(year): print(year)
        else: print(int(year) + 1)
def main():
    solve()

if __name__ == "__main__":
    main()