def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        a = []
        for _ in range(n):
            a.append(int(input()))
        a_s = sorted(a)
        if a_s[0] != a_s[-1]:
            print(a_s[0], a_s[-1])
        else:
            print("BANG NHAU")

def main():
    solve()

if __name__ == "__main__":
    main()