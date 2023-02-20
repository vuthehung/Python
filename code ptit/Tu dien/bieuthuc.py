t = int(input())
for _ in range(t) :
    s = input()
    res = []
    ind = 1
    for i in s:
        if i == '(':
            print(ind, end= ' ')
            res.append(ind)
            ind += 1
        elif i == ')':
            print(res[-1], end= ' ')
            res.pop()
    print()