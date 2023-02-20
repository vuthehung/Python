from itertools import permutations
import itertools

def main():
    s, n = input().split()
    for permutation in itertools.permutations(sorted(s), int(n)):
        print("".join(permutation))
if __name__ == "__main__":
    main()