class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def get_longest_consecutive_path(root, l, data):
    if not root:
        return
    if root.data == data:
        l += 1
    else:
        l = 1
    get_longest_consecutive_path.res = max(get_longest_consecutive_path.res, l)

    get_longest_consecutive_path(root.left, l, root.data + 1)
    get_longest_consecutive_path(root.right, l, root.data + 1)


if __name__ == "__main__":
    root = Node(6)
    root.right = Node(9)
    root.right.left = Node(7)
    root.right.right = Node(10)
    root.right.right.right = Node(11)

    get_longest_consecutive_path.res = 0
    get_longest_consecutive_path(root, 0, root.data)
    print(get_longest_consecutive_path.res)
