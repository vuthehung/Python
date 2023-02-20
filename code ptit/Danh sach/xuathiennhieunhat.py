from collections import Counter
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        l_s = sorted(l)
        cnt = Counter(l_s)
        ok = 0
        for i in cnt:
            if cnt[i] > (n // 2):
                ok = 1
                print(i)
                break
        if ok == 0:
            print("NO")
        

def main():
    solve()

if __name__ == "__main__":
    main()