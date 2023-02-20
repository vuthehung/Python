import math
def solve():
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        print(int(math.gcd(a, b)))

def main():
    solve()

if __name__ == "__main__":
    main()