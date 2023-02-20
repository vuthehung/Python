
def solve():
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        cnt = 0
        i = 1
        while p * i <= n:
            tmp = p * i
            while tmp % p == 0:
                cnt += 1
                tmp /= p
            i += 1
        print(cnt)

def main():
    solve()

if __name__ == "__main__":
    main()