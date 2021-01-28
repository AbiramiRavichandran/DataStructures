class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_mirror(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

def is_foldable(root):
    if not root:
        return
    return is_mirror(root.left, root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.left.right = Node(5)

    print(is_foldable(root))