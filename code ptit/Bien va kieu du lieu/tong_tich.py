
def ind_c(n):
    sum = 0
    for i in range(0, len(n)):
        if i % 2 == 0:
            sum += int(n[i])
    return sum

def check(n):
    for i in range(0, len(n)):
        if i % 2 != 0:
            if n[i] != '0':
                return False
                break
    return True

def ind_l(n):
    mul = 1
    if check(n):
        return 0
    for i in range(1, len(n)):
        if i % 2 != 0:
            if n[i] == '0':
                continue
            mul *= int(n[i])
    return mul

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        print(f"{ind_c(n)} {ind_l(n)}")

def main():
    solve()


if __name__ == "__main__":
    main()