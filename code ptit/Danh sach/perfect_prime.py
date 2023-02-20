
import math


def prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            break
    return True

def check1(n):
    rever = n[::-1]
    return prime(int(rever))

def check2(n):
    sum = 0
    for i in n:
        sum += int(i)
    return prime(sum)

def check3(n):
    for i in n:
        if not(prime(int(i))):
            return False
            break
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        if prime(int(n)) and check1(n) and check2(n) and check3(n):
            print("Yes")
        else:
            print("No")

def main():
    solve()

if __name__ == "__main__":
    main()
