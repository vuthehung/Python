from collections import Counter

def main():
    x = int(input())
    size_shoes = list(map(int, input().split()))
    n = int(input())
    counter = Counter(size_shoes)
    total_money_earned = 0
    for _ in range(n):
        custom = list(map(int, input().split()))
        if counter[custom[0]] != 0:
            counter[custom[0]] -= 1
            total_money_earned += custom[1]
    print(total_money_earned)
if __name__ == '__main__':
    main()