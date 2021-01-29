class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def count_single(root):
    if not root:
        return 0
    res = 0
    if (not root.left or (root.left and root.left.data == root.data)) and (not root.right or (root.right and root.right.data == root.data)):
        res = 1
    return res + count_single(root.left) + count_single(root.right)





if __name__ == "__main__":
    root = Node(5)
    root.left = Node(1)
    root.right = Node(5)
    root.left.left = Node(5)
    root.left.right = Node(5)
    root.right.right = Node(5)

    print(count_single(root))
