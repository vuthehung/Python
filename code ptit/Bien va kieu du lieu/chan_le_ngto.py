
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
    for i in range(0, len(n), 2):
        if int(n[i]) % 2 != 0:
            return False
            break
    return True
    
def check2(n):
    for i in range(1, len(n), 2):
        if int(n[i]) % 2 == 0:
            return False
            break
    return True

def check3(n):
    sum = 0
    for i in n:
        sum += int(i)
    return nguyento(sum)

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        if check1(n) and check2(n) and check3(n):
            print("YES")
        else:
            print("NO")        

def main():
    solve()
if __name__ == "__main__":
    main()