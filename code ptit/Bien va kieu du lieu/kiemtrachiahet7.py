
def reverse_num(n):
    res = str(n)
    rever = res[::-1]
    return int(rever)
    
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        limit = 1001
        
        if n % 7 == 0:
            print(n)
        else:
            check = 0
            while limit > 0:
                n = n + reverse_num(n)
                if n % 7 == 0:
                    check = 1
                    print(n)
                    break
            if check == 0:
                print("-1")
def main():
    solve()

if __name__ == "__main__":
    main()