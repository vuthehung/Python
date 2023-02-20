from collections import Counter

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = []
        for _ in range(n):
            l.append(int(input()))
        l_s = sorted(l)
        cnt = Counter(l_s)
        print(cnt.most_common()[0][0])
def main():
    solve()

if __name__ == "__main__":
    main()