
def solve():
    s = input()
    countUp = 0
    countLow = 0
    for i in range(len(s)):
        if s[i].isupper():
            countUp += 1
        elif s[i].islower():
            countLow += 1
    if countLow >= countUp:
        print(s.lower())
    else:
        print(s.upper())
def main():
    solve()

if __name__ == "__main__":
    main()