def countDigits(n, digit):
    if n <= 0:
        return 0
    count = 0
    if digit == 0:
        i = 1
        while i <= n//10:
            unit = i*10
            count += (n//unit-1)*i+min(i, max(0, n % unit-digit*i+1))
            i *= 10
    else:
        i = 1
        while i <= n:
            unit = i*10
            count += n//unit * i + min(i, max(0, n % unit-digit*i+1))
            i *= 10
    return count


def Solve():
    l, r = map(int, input().split())
    for i in range(0, 10):
        print(countDigits(r, i) - countDigits(l-1, i), end=" ")
    print()


for _ in range(int(input())):
    Solve()
