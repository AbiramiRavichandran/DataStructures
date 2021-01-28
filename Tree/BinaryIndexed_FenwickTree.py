
def get_sum(bit_tree, i):
    s = 0
    i += 1
    while i > 0:
        s += bit_tree[i]
        # removing the last set bit of the current index to get the parent
        i -= i & (-i)

    return s


def update_bit(bit_tree, n, i, val):
    i += 1

    while i < n:
        bit_tree[i] += val
        # incrementing the last set bit of the current index to get next index
        i += i & (-i)




def construct_bit(arr, n):

    bit_tree = [0] * (n+1)

    for i in range(n):
        update_bit(bit_tree, n, i, arr[i])

    return bit_tree


if __name__ == "__main__":
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bit_tree = construct_bit(arr, len(arr))
    print(get_sum(bit_tree, 5))
    arr[3] += 6
    update_bit(bit_tree, len(arr), 3, 6)
    print(get_sum(bit_tree, 5))
