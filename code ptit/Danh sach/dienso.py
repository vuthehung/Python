
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a_s = sorted(a)
        min = a_s[0]
        max = a_s[len(a) - 1]
        cnt = 0
        for i in range(min, max + 1):
            if a.count(i) == 0:
                cnt += 1
        print(cnt)

def main():
    solve()

if __name__ == "__main__":
    solve()