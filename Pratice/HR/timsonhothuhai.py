if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    L = list(arr)
    L.sort()
    L.reverse()
    print(L)
    tmp = L[0]
    for i in range(1, n):
        if L[i] < tmp:
            tmp = L[i]
            break
    print(tmp)