def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapify(arr, n, i):
        root = i
        l = (i * 2) + 1
        r = (i * 2) + 2
        if l < n and arr[root] > arr[l]:
            root = l
        if r < n and arr[root] > arr[r]:
            root = r
        if i != root:
            swap(arr, i, root)
            heapify(arr, n, root)




def connect_ropes(arr):
    n = len(arr)
    i = n // 2 - 1
    while i >= 0:
        heapify(arr, n, i)
        i -= 1

    print(arr)

    min = 0
    while len(arr) > 0:
        if arr[0] > min:
            swap(arr, -1, 0)
            print("{0}, {1}".format(min, arr[-1]))
            min += arr[-1]
            del arr[-1]
            heapify(arr, len(arr), 0)
        else:
            arr.append(min)
            min = 0
            n = len(arr)
            heapify(arr, n, n - 1)


    print(min)


if __name__ == "__main__":
    arr = [4, 3, 2, 6]
    connect_ropes(arr)