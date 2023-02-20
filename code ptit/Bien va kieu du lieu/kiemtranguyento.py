
import math

def nguyento(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            break
    return True


def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        res = n[len(n) - 4 : len(n)]
        if nguyento(int(res)):
            print("YES")
        else:
            print("NO")
def main():
    solve()
if __name__ == "__main__":
    main()