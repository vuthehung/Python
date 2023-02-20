
def score(x):
    if x >= 3 and x <= 4:
        return 2.5
    elif x >= 5 and x <= 6:
        return 3.0
    elif x >= 7 and x <= 9:
        return 3.5
    elif x >= 10 and x <= 12:
        return 4.0
    elif x >= 13 and x <= 15:
        return 4.5
    elif x >= 16 and x <= 19:
        return 5.0
    elif x >= 20 and x <= 22:
        return 5.5
    elif x >= 23 and x <= 26:
        return 6.0
    elif x >= 27 and x <= 29:
        return 6.5
    elif x >= 30 and x <= 32:
        return 7.0
    elif x >= 33 and x <= 34:
        return 7.5
    elif x >= 35 and x <= 36:
        return 8.0
    elif x >= 37 and x <= 28:
        return 8.5
    elif x >= 39 and x <= 40:
        return 9.0

def solve():
    t = int(input())
    for _ in range(t):
        a = input().split()
        sum = score(int(a[0])) + score(int(a[1])) + float(a[2]) + float(a[3])
        aver = str(sum / 4)
        tmp = aver.split('.')
        x = int(tmp[0])
        if tmp[1] >= '25' and tmp[1] < '75':
            tmp[1] = '5'
        elif tmp[1] >= '75':
            tmp[0] = str(x + 1)
            tmp[1] = '0'
        elif tmp[1] < '25':
            tmp[1] = '0'
            
        print('.'.join(tmp))


def main():
    solve()

if __name__ == "__main__":
    main()