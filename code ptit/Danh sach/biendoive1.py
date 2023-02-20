
def solve():
    while 1:
        n = int(input())
        if n == 0:
            break
        if n == 1:
            print("1")
        else:
            res = 1
            while n != 1:
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = n * 3 + 1
                res += 1
            print(res)

def main():
    solve()

if __name__ == "__main__":
    main()