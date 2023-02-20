
from collections import Counter

def check(n):
    for i in range(len(n) - 2):
        if n[i] != n[i + 2]:
            return False
            break
    return True
def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        l = list(n)
        cnt = Counter(l)
        if len(cnt) == 2 and check(n):
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()