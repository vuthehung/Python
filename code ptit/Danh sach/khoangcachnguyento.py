import math

def prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            break
    return True

def solve():
    n, x = map(int, input().split())
    l_prime = []
    i = 2
    while len(l_prime) < n:
        if prime(i):
            l_prime.append(i)
        i += 1
    l_res = []
    l_res.append(x)
    for j in range(1, n + 1):
        l_res.append(l_res[j - 1] + l_prime[j - 1])
    print(*l_res)
def main():
    solve()

if __name__ == "__main__":
    main()