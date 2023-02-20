
def solve():
    n = int(input())
    l = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        if l[i] != l[i + 1]:
            cnt += 1
    print(cnt)
def main():
    solve()

if __name__ == "__main__":
    main()