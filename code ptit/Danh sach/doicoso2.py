def solve():
    a_4 = ['00', '01', '10', '11']
    a_8 = ['000', '001', '010', '011', '100', '101', '110', '111']
    a_16 = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    t = int(input())
    for _ in range(t):
        b = int(input())
        bina = input()
        if b == 2:
            print(bina)
        elif b == 4:
            tmp1 = bina
            res1 = []
            while len(tmp1) % 2 != 0:
                tmp1 = '0' + tmp1
            i = 0
            while i != len(tmp1):
                res1.append(tmp1[i:i+2])
                i += 2
            for i in range(len(res1)):
                res1[i] = str(a_4.index(res1[i]))
            print(''.join(res1))
        elif b == 8:
            tmp2 = bina
            res2 = []
            while len(tmp2) % 3 != 0:
                tmp2 = '0' + tmp2
            j = 0
            while j != len(tmp2):
                res2.append(tmp2[j:j+3])
                j += 3
            for j in range(len(res2)):
                res2[j] = str(a_8.index(res2[j]))
            print(''.join(res2))
        elif b == 16:
            tmp3 = bina
            res3 = []
            while len(tmp3) % 4 != 0:
                tmp3 = '0' + tmp3
            l = 0
            while l != len(tmp3):
                res3.append(tmp3[l:l+4])
                l += 4
            for l in range(len(res3)):
                if a_16.index(res3[l]) >= 10:
                    res3[l] = str(chr(a_16.index(res3[l]) + 55))
                else:
                    res3[l] = str(a_16.index(res3[l]))
               
            print(''.join(res3))
def main():
    solve()

if __name__ == "__main__":
    main()