def Tower(n, a, b, c):
    if n == 1:
        print(f"{a} -> {c}")
        return
    Tower(n - 1, a, c, b)
    Tower(1, a, b, c)
    Tower(n - 1, b, a, c)

def solve():
    n = int(input())
    a = 'A'
    b = 'B'
    c = 'C'
    Tower(n, a, b, c)

def main():
    solve()

if __name__ == "__main__":
    main()