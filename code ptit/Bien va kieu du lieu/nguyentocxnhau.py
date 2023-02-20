import math

def solve():
    cnt = 0
    n, k = map(int, input().split())
    for i in range(int(math.pow(10, k - 1)), int(math.pow(10, k))):
        if(int(math.gcd(n, i))) == 1:
            cnt += 1
            print(i, end = ' ')
            if cnt == 10:
                print()
                cnt = 0

def main():
    solve()

if __name__ == "__main__":
    main()