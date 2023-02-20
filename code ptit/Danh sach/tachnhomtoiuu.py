n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(n-1):
    if arr[i+1]-arr[i] > k:
        ans += 1
print(ans+1)
