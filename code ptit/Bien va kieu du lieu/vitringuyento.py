
import math


def nguyento(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            break
    return True

def check1(n):
    for i in range(0, len(n)):
        if (not(nguyento(i)) and (nguyento(int(n[i])))) or ((nguyento(i)) and not(nguyento(int(n[i])))):
            return False
            break
    return True
    
def check2(n):
    for i in range(0, len(n)):
        if (not(nguyento(i)) and (nguyento(int(n[i])))) or ((nguyento(i)) and not(nguyento(int(n[i])))):
            return False
            break
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        if check1(n) and check2(n):
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()