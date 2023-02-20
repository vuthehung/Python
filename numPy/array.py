from audioop import reverse
import numpy

def array(arr):
    return numpy.array(arr[::-1], float)
def main():
    arr = input().split(' ')
    res = array(arr)
    print(res)
if __name__ == "__main__":
    main()