class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order_traversal()

def get_max(arr, start, end):
    max_index = start
    for i in range(start + 1, end):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def construct_bt(arr, start, end):
    if start > end:
        return
    max_index = get_max(arr, start, end)

    root = Node(arr[max_index])
    root.left = construct_bt(arr, start, max_index - 1)
    root.right = construct_bt(arr, max_index + 1, end)

    return root


if __name__ == "__main__":
    in_order = [1, 5, 10, 40, 30, 15, 28, 20]
    root = construct_bt(in_order, 0, len(in_order)-1)
    root.in_order_traversal()
