import itertools

def main():
    s, n = input().split()
    for i in range(1, int(n) + 1):
        for j in itertools.combinations(sorted(s), i):
            print("".join(j))
if __name__ == "__main__":
    main()