
def tich_cs(n):
    multi = 1
    for i in n:
        if i == '0':
            continue
        multi *= int(i)
    return multi

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        print(tich_cs(n))

def main():
    solve()

if __name__ == "__main__":
    main()