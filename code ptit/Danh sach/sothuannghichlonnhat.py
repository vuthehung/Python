
def thuannghich(x):
    res = str(x)[::-1]
    return res == str(x) and len(res) > 1

def solve():
    n, m = map(int, input().split())
    matrix = []
    max_tn = 0
    for _ in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)
        for i in a:
            if thuannghich(i) and max_tn < i:
                max_tn = i
    if max_tn == 0:
        print("NOT FOUND")
    else:
        print(max_tn)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == max_tn:
                    print(f"Vi tri [{i}][{j}]")

def main():
    solve()

if __name__ == "__main__":
    main()