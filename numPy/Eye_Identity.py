import numpy

numpy.set_printoptions(legacy='1.13')
def main():
    r, c = map(int, input().split())
    print(numpy.eye(r, c))
if __name__ == "__main__":
    main()