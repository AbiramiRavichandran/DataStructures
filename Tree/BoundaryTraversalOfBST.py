class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def print_left_boundary(root):
    if not root:
        return

    if root.left:
        print(root.data)
        print_left_boundary(root.left)
    elif root.right:
        print(root.data)
        print_left_boundary(root.right)

def print_right_boundary(root):
    if not root:
        return

    if root.right:
        print_right_boundary(root.right)
        print(root.data)
    elif root.left:
        print_right_boundary(root.left)
        print(root.data)

def print_leaves(root):
    if not root:
        return

    print_leaves(root.left)

    if root.left is None and root.right is None:
        print(root.data)

    print_leaves(root.right)



def print_boundary(root):
    if not root:
        return

    print(root.data)
    print_left_boundary(root.left)

    print_leaves(root.left)
    print_leaves(root.right)

    print_right_boundary(root.right)


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    print_boundary(root)