
from re import S

def tichcs(n):
    mul = 1
    while n > 0:
        mul *= n % 10
        n = n // 10
    return mul


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if tichcs(l[i]) > tichcs(l[j]):
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp
                elif tichcs(l[i]) == tichcs(l[j]):
                    m1 = min(l[i], l[j])
                    m2 = max(l[i], l[j])
                    l[i] = m1
                    l[j] = m2
        print(*l)



def main():
    solve()

if __name__ == "__main__":
    main()