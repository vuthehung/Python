


def solve():
    n, m = map(int, input().split())
    matrix = []
    max = 0
    min = int(1e8)
    for _ in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)
        for i in a:
            if max < i:
                max = i
            if min > i:
                min = i
    lucky_num = max - min            
    check = 0
    for i in matrix:
        for j in i:
            if lucky_num == j:
                check = 1
    if check == 0:
        print("NOT FOUND")
    else:
        print(lucky_num)
        for i in range(n):
            for j in range(m):
                if lucky_num == matrix[i][j]:
                    print(f"Vi tri [{i}][{j}]")
def main():
    solve()

if __name__ == "__main__":
    main()