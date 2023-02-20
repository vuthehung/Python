import re

n = int(input())
nmc = ""
for i in range(n):
    nmc += str(len(input().split()))
nmc = re.sub("(68)+", "1", nmc)
nmc = re.sub("7777", "2", nmc)
print(len(nmc))
for x in nmc:
    print(x)
