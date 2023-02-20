
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a = sorted(a)
        b = sorted(b)
        cnt = 0
        for i in range(n):
            if a[i] <= b[i]:
                cnt += 1
        if cnt == n:
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()