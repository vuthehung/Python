
def solve():
    n = int(input())
    matrix = []
    for _ in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)
    k = int(input())
    sum_up = 0
    sum_under = 0
    for i in range(1, n):
        for j in range(i):
            sum_under += matrix[i][j]
    for i in range(n):
        for j in range(i + 1, n):
            sum_up += matrix[i][j]
    limit = abs(sum_up - sum_under)
    if limit <= k:
        print("YES")
    else:
        print("NO")
    print(limit)

    
def main():
    solve()

if __name__ == "__main__":
    main()