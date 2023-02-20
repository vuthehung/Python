from collections import Counter

def solve():
    l = list(input())
    counter = Counter(l)
    if counter['7'] + counter['4'] == 4 or counter['7'] + counter['4'] == 7:
        print("YES")
    else:
        print("NO")
def main():
    solve()

if __name__ == "__main__":
    main()