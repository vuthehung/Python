import math

def prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    check = 0
    for i in range(len(res)):
        if prime(sum(res[:i + 1])) and prime(sum(res[i + 1:])):
            print(i)
            check = 1
            break
    if check == 0:
        print("NOT FOUND")

def main():
    solve()

if __name__ == "__main__":
    main()