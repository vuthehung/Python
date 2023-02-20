
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
    return nguyento(len(n))

def check2(n):
    cnt_prime = 0
    for i in n:
        if nguyento(int(i)):
            cnt_prime += 1
    return cnt_prime > (len(n) - cnt_prime)

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