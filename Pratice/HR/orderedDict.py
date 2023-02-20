from collections import OrderedDict


def main():
    n = int(input())
    d = OrderedDict()
    for _ in range(n):
        item = input().split()
        item_name = ' '.join[item[:-1]]
        net_price = item[-1]
        if d.get(item_name):
            d[item_name] += net_price
        else:
            d[item_name] = net_price
    for i in d.keys():
        print(i, d[i])
if __name__ == "__main__":
    main()