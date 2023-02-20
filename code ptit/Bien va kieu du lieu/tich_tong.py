
def ind_c(n):
    mul = 1
    for i in range(0, len(n)):
        if i % 2 == 0:
            if n[i] == '0':
                continue
            mul *= int(n[i])
    return mul


def ind_l(n):
    sum = 0
    
    for i in range(1, len(n)):
        if i % 2 != 0:
            sum += int(n[i])
    return sum

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        print(f"{ind_c(n)} {ind_l(n)}")

def main():
    solve()


if __name__ == "__main__":
    main()