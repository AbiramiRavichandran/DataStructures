def heapify(arr, i, n):
    root = i
    l = (i * 2) + 1
    r = (i * 2) + 2

    if l < n and arr[l] > arr[root]:
        root = l
    if r < n and arr[r] > arr[root]:
        root = r

    if root != i:
        arr[root], arr[i] = arr[i], arr[root]
        heapify(arr, root, n)



def heap_sort(arr):
    n = len(arr)
    i = n // 2 -1
    while i >= 0:
        heapify(arr, i, n)
        i -= 1

    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)
    print(arr)



if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7, 10, 3]
    heap_sort(arr)
