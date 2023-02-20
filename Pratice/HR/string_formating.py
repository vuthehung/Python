#in tu 1 den n: lan luot 4 dinh dang sau: "he10" "he 8" "he16" "he2"
from turtle import width


def print_formated(number):
    for i in range(1, number + 1):
        width = len(f"{number:b}")
        print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")
if __name__ == '__main__':
    n = int(input())
    print_formated(n)