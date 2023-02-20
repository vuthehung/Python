from collections import OrderedDict

def main():
    n = int(input())
    d = OrderedDict()
    for _ in range(n):
        word = input()
        if d.get(word):
            d[word] += 1
        else:
            d[word] = 1
    print(len(d))
    print(*d.values())
if __name__ == "__main__":
    main()