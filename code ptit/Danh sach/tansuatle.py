from collections import Counter

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        l_s = sorted(l)
        cnt = Counter(l_s)
        for i in cnt:
            if cnt[i] % 2 != 0:
                print(i)
        
        

def main():
    solve()

if __name__ == "__main__":
    main()