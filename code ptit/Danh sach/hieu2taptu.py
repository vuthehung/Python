def solve():
    f1 = open('DATA1.in', 'r')
    f2 = open('DATA2.in', 'r')
    l1 = []
    l2 = []
    for l in f1:
        for i in l.split():
            if i.lower() not in l1:
                l1.append(i.lower())
    for l in f2:
        for i in l.split():
            if i.lower() not in l2:
                l2.append(i.lower())

    for i in sorted(l1):
        if i not in l2:
            print(i, end= ' ')
    print()
    for i in sorted(l2):
        if i not in l1:
            print(i, end= ' ')

if __name__ == "__main__":
    solve()