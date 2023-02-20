from collections import defaultdict

def main():
    inp = list(map(int, input().split()))
    n, m = inp[0], inp[1]
    d = defaultdict(list)
    d_res = defaultdict(list)
    for i in range(n + m):
        if i < n:
            d['A'].append(input())
        else:
            d['B'].append(input())
    for i in d['B']:
        for index, val in enumerate(d['A']):
            if i == val:
                d_res[i].append(index + 1)
    for i in d_res.values():
        print(*i)
if __name__ == '__main__':
    main()