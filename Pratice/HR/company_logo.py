from collections import Counter

if __name__ == "__main__":
    s = input()
    s1 = sorted(s)
    c = Counter(s1)
    for i in c.most_common(3):
        print(*i)