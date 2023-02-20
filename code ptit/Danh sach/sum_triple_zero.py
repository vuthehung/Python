

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = sorted(list(map(int, input().split())))
        cnt = 0
        for i in range(n):
            l = i + 1
            r = len(arr) - 1
            while l < r:
                if arr[l] + arr[r] + arr[i] == 0:
                    cnt += 1
                    l += 1
                elif arr[l] + arr[r] + arr[i] < 0:
                    l += 1
                else:
                    r -= 1
        print(cnt) 

def main():
    solve()

if __name__ == "__main__":
    main()