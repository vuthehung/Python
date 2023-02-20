
from audioop import reverse


def gcd(a, b):
    tmp = 0
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a
def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        rever_n = ""
        for i in range(len(n) - 1, -1, -1):
            rever_n += n[i]
        if gcd(int(n), int(rever_n)) == 1:
            print("YES")
        else:
            print("NO")
def main():
    solve()

if __name__ == "__main__":
    main()