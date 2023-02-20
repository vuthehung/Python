import math

def prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1

def solve():
    n, m = map(int, input().split())
    matrix = []
    max_prime = 0
    for _ in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)
        for i in a:
            if prime(i) and max_prime < i:
                max_prime = i
    if max_prime == 0:
        print("NOT FOUND")
    else:
        print(max_prime)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == max_prime:
                    print(f"Vi tri [{i}][{j}]")

def main():
    solve()

if __name__ == "__main__":
    main()