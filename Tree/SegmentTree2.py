import sys
from math import log2, ceil

int_max = sys.maxsize


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_st_util(st, ss, se, si, arr):
    if ss == se:
        st[si] = arr[ss]
        return st[si]

    mid = (ss + se) // 2

    st[si] = min(construct_st_util(st, ss, mid, si * 2 + 1, arr), construct_st_util(st, mid + 1, se, si * 2 + 2, arr))

    return st[si]



def construct_st(arr, n):
    height = ceil(log2(n))

    size = 2 * height**2 - 1
    print(size)

    st = [None] * size

    construct_st_util(st, 0, n-1, 0, arr)

    return st


def get_min_util(st, ss, se, qs, qe, si):
    if qs <= ss and qe >= se:
        return st[si]

    if se < qs or ss > qe:
        return int_max

    mid = (ss + se) // 2

    return min(get_min_util(st, ss, mid, qs, qe, si*2+1), get_min_util(st, mid + 1, se, qs, qe, si*2+2))

def get_min(st, qs, qe, n):

    if qs < 0 or qe > n-1:
        return -1

    return get_min_util(st, 0, n-1, qs, qe, 0)



if __name__ == "__main__":

    arr = [1, 3, 2, 7, 9, 11]
    n = len(arr)

    # Build segment tree from given array
    st = construct_st(arr, n)

    print(st)

    qs = 0
    qe = 1

    print(get_min(st, 0, 1, n))
