import numpy

def main():
    N = tuple(map(int, input().split()))
    print(numpy.zeros(N, int))
    print(numpy.ones(N, int))
if __name__ == "__main__":
    main()