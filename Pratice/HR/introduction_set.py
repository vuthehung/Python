def averge(arr):
    sum_set = sum(set(arr))
    len_set = len(set(arr))
    return sum_set / len_set 
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    res = averge(arr)
    print(res)
