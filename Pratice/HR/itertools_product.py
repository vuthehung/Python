from itertools import product
def main():
    L_A = list(map(int, input().split()))
    L_B = list(map(int, input().split()))
    print(*tuple(product(L_A, L_B)))
    
if __name__ == '__main__':
    main()