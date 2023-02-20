

def soThuanNghich(n):
    res = n[::-1]
    return n == res
def demSoChuSo(n):
    return len(n) % 2 == 0
def chuSo(n):
    for i in n:
        if int(i) % 2 != 0:
            return False
            break
    return True
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(22, n, 22):
            if soThuanNghich(str(i)) and demSoChuSo(str(i)) and chuSo(str(i)):
                print(i, end = ' ')
        print()

def main():
    solve()

if __name__ == "__main__":
    main()