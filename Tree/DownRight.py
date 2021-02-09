class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def convert(root):
    if not root:
        return None

    convert(root.left)
    convert(root.right)

    if not root.left:
        root.left = root.right
    else:
        root.left.right = root.right

    root.right = None


def down_traversal(root):
    if not root:
        return
    print(root.data, end=" ")
    down_traversal(root.right)
    down_traversal(root.left)


        
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.left.left = Node(6)
    root.right.right.left = Node(7)
    root.right.right.right = Node(8)
    convert(root)
    down_traversal(root)