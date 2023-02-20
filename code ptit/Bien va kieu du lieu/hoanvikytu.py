
import itertools

def solve():
    n = input()
    for i in itertools.permutations(n, len(n)):
        for j in i:
            print(j, end='')
        print()
           

def main():
    solve()

if __name__ == "__main__":
    main()