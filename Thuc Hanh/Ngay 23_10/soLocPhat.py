t = int(input())

for _ in range(t):
    d = {
        '6': 0,
        '8': 0
    }
    n = int(input())
    for i in range(8, n + 1, 8):
        s = str(i)
        d['6'] += s.count('6')
        d['8'] += s.count('8')

    print(d['6'] + d['8'])