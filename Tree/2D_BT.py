class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_2D(root, space=0):
    if not root:
        return
    space += 10
    print_2D(root.right, space)
    print()
    for i in range(space):
        print(end=" ")
    print(root.data)
    print_2D(root.left, space)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    print_2D(root)