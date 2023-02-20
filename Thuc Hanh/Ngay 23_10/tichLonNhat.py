n = int(input())

a = list(map(int, input().split()))

a.sort(reverse= True)

m = [a[0] * a[1], a[0] * a[1] * a[2], a[n - 2] * a[n - 1], a[n - 3] * a[n - 2] * a[n - 1], a[0] * a[n - 2] * a[n - 1]]

print(max(m))