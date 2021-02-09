from heapq import heapify, heappop, heappush

def sort_k(arr, n, k):
    heap = arr[:k+1]
    heapify(heap)

    i = 0
    for j in range(k+1, n):
        arr[i] = heappop(heap)
        heappush(heap, arr[j])
        i += 1

    while i < n:
        arr[i] = heappop(heap)
        i += 1

    print(arr)


if __name__ == "__main__":
    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    n = len(arr)
    sort_k(arr, n, k)