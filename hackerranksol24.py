from __future__ import division

def average(array):
    c=float(sum(array))
    print(c)
    d=float(len(array))
    e=(c/d)
    return e

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print (result)
