from collections import Counter

def solve():
    n = input()
    l = list(n)
    counter = Counter(l)
    if counter['7'] + counter['4'] == len(n):
        print("YES")
    else:
        print("NO")
def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()