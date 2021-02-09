def print_sorted(arr, n, i=0):
    if i < n:
        print_sorted(arr, n, (i*2)+1)
        print(arr[i], end=" ")
        print_sorted(arr, n, (i*2)+2)





if __name__ == "__main__":
    arr = [4, 2, 5, 1, 3]
    print_sorted(arr, len(arr))