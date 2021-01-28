from math import log2,ceil


# st[ss..se], si - index of current node
def construct_st_util(arr, ss, se, st, si):

    # if the array has only one element, add the element to the current node and return it
    if ss == se:
        st[si] = arr[ss]
        return arr[ss]

    # if there are more than one element, recurse to left and right sub trees and add the sum of child nodes to the
    # current node
    mid = (ss + se) // 2

    st[si] = construct_st_util(arr, ss, mid, st, si*2+1) + construct_st_util(arr, mid+1, se, st, si*2+2)

    return st[si]


def construct_st(arr, n):
    #find height
    height = ceil(log2(n))

    #find max size
    max_size = 2 * (2**height) - 1

    #allocate memory
    st = [0] * max_size

    # filling the allocated memory
    construct_st_util(arr, 0, n-1, st, 0)

    return st


#si - current node, ss,se - range represented by si
#qs, qe - query range
def get_sum_util(st, ss, se, qs, qe, si):
    # if query range is part of the given range then return the current element
    if qs <= ss and qe >= se:
        return st[si]

    #return 0 if its out of range
    if se < qs or ss > qe:
        return 0

    mid = (ss + se) // 2

    return get_sum_util(st, ss, mid, qs, qe, si*2+1) + get_sum_util(st, mid+1, se, qs, qe, si*2+2)

def get_sum(st, n, qs, qe):
    if qs < 0 or qe > n-1 or qs > qe:
        return -1

    return get_sum_util(st, 0, n-1, qs, qe, 0)


def update_value(st, arr, n, i, new_val):
    if i < 0 or i > n-1:
        return

    diff = new_val - arr[i]
    arr[i] = new_val

    update_value_util(st, 0, n-1, i, diff, 0)



def update_value_util(st, ss, se, i, diff, si):
    if i < ss or i > se:
        return

    st[si] = st[si] + diff

    if ss != se:
        mid = (ss + se) // 2
        update_value_util(st, ss, mid, i, diff, si*2+1)
        update_value_util(st, mid+1, se, i, diff, si*2+2)






if __name__ == "__main__" :

    arr = [1, 2, 3, 4, 5]
    n = len(arr)

    st = construct_st(arr, n)
    print(st)

    print("sum : ", get_sum(st, n, 1, 3))

    update_value(st, arr, n, 1, 10)

    print(st)