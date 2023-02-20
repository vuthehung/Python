
if __name__ == '__main__':  
    L = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        L += [[name, score]]
    L = sorted(L, key=lambda x : x[1])
    tmp = L[0][1]
    for i in range(n):
        if L[i][1] > tmp:
            tmp = L[i][1]
            break
    L1 = []
    cnt = 0
    for i in range(n):
        if L[i][1] == tmp:
            L1 += [L[i][0]]
            cnt += 1
    L1 = sorted(L1)
    for i in range(cnt):
        print(L1[i])