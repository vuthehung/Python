def convert(n, b):
    res = ""
    tmp = n
    while tmp > 0:
        du = tmp % b
        if du >= 10:
            res += str(chr(du + 55))
        else:
            res += str(du)
        tmp = tmp // b
    print(''.join(reversed(res)))
def solve():
    t = int(input())
    for _ in range(t):
        n, b = map(int, input().split())
        convert(n, b)

def main():
    solve()

if __name__ == "__main__":
    main()