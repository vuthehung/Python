import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
            break
    return True

def tongcs(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        sum_cs = tongcs(n)
        if prime(sum_cs):
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()