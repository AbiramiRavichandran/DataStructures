class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def get_height(root, is_even=False):
    if not root:
        return 0
    if not root.left and not root.right:
        if is_even:
            return 1
        else:
            return 0

    left = get_height(root.left, not is_even)
    right = get_height(root.right, not is_even)

    if left == 0 and right == 0:
        return 0
    return 1 + max(left, right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)

    print(get_height(root))