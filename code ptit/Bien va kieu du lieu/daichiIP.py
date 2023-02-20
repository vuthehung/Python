
def check(s):
    for i in s:
        if i < '0' or i > '9':
            return False
    return True

def solve():
    t = int(input())
    for _ in range(t):
        a = input().split('.')
        res = []
        for i in a:
            if check(i):
                if int(i) >= 0 and int(i) <= 255:
                    res.append(i)
        if len(res) == 4:
            print("YES")
        else:
            print("NO")
        

def main():
    solve()

if __name__ == "__main__":
    main()