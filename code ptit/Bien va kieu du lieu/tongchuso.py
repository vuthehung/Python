def sum_digit(n):
    sum = 0
    for i in n:
        sum += ord(i) - ord('0')
    return sum
def solve():
    n = input()
    cnt = 0
    tmp = n
    while len(tmp) > 1:
        tmp = str(sum_digit(tmp))
        cnt += 1
    print(cnt)

        

def main():
    solve()

if __name__ == "__main__":
    main()