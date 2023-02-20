
def solve():
    n = input()

    while len(n) > 1:
        n_1 = int(n[0 : len(n) // 2])
        n_2 = int(n[len(n) // 2 : len(n)])
        sum = n_1 + n_2
        n = str(sum)
        print(sum)


def main():
    solve()

if __name__ == "__main__":
    main()