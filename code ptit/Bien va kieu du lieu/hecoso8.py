
def solve():
    a = ['000', '001', '010', '011', '100', '101', '110', '111']
    n = input()
    tmp = n
    while len(tmp) % 3 != 0:
        tmp = '0' + tmp
    i = 0
    res = []
    while i != len(tmp):
        res.append(tmp[i : i + 3])
        i += 3
    for i in range(len(res)):
        res[i] = str(a.index(res[i]))
    print(''.join(res))
def main():
    solve()

if __name__ == "__main__":
    main()