def check1(s):
    for i in s:
        if int(i) != 6 and int(i) != 8:
            return False
    return True

def check2(s):
    a = [int(i) for i in s]
    for i in range(len(a)):
        if a[0] == 8: 
            return False
        if a[i] == 8 and a[i - 1] != 6 and a[i - 1] != 8:
            return False
        if i > 1 and a[i] == 8 and a[i - 1] == 8 and a[i - 2] != 6:
            return False
    return True
def solve():
    s = input()
    if check1(s) and check2(s):
        print("YES")
    else:
        print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()