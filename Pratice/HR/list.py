if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        s = input()
        L_str = list(s.split())
        if L_str[0] == "insert":
            L.insert(int(L_str[1]), int(L_str[2]))
        elif L_str[0] == "append":
            L.append(int(L_str[1]))
        elif L_str[0] == "remove":
            L.remove(int(L_str[1]))
        elif s == "print":
            print(L)
        elif s == "sort":
            L.sort()
        elif s == "pop":
            L.pop()
        elif s == "reverse":
            L.reverse()