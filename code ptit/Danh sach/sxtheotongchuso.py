

def tongcs(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if tongcs(l[i]) > tongcs(l[j]):
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp
                elif tongcs(l[i]) == tongcs(l[j]):
                    m1 = min(l[i], l[j])
                    m2 = max(l[i], l[j])
                    l[i] = m1
                    l[j] = m2
        print(*l)



def main():
    solve()

if __name__ == "__main__":
    main()