

def solve():
    t = int(input())
    d_cost = {
        5: 10000,
        7: 15000,
        2: 20000,
        29: 50000,
        45: 70000
    }
    d_date = dict()
    a = []
    for _ in range(t):
        tmp = list(input().split())
        if tmp[3] == "IN":
            a.append(tmp)
        d_date[tmp[4]] = 0
    date = list(d_date.keys())
    for j in date:
        for i in range(len(a)):
            if a[i][4] == j:
                d_date[j] += d_cost[int(a[i][2])]
    for i in d_date.items():
        print(f"{i[0]}: {i[1]}")


def main():
    solve()

if __name__ == "__main__":
    main()

# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021