
import math


def check(x):
    if x <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
                break
    return True
def solve():
    t = int(input())
    for _ in range(t):
        a1, b1 = map(int, input().split())
        tmp = 0
        while b1 != 0:
            tmp = a1 % b1
            a1 = b1
            b1 = tmp
        string_num = str(a1)
        n = 0
        for i in range(len(string_num)):
            n += int(string_num[i])
        if check(n):
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()