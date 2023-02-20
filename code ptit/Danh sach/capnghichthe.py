
def solve():
    n = int(input())
    l = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if i < j and l[i] > l[j]:
                cnt += 1
    print(cnt)

def main():
    solve()

if __name__ == "__main__":
    main()