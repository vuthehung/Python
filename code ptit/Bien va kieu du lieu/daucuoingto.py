
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
        pre = n[0:3]
        pos = n[len(n) - 3:len(n)]
        if nguyento(int(pre)) and nguyento(int(pos)):
            print("YES")
        else:
            print("NO")
def main():
    solve()
if __name__ == "__main__":
    main()