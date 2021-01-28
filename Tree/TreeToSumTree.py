class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()


def sum_tree(root):
    if not root:
        return 0
    old_val = root.data
    root.data = sum_tree(root.left) + sum_tree(root.right)
    return root.data + old_val




if __name__ == "__main__":
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)

    sum_tree(root)
    root.in_order_traversal()
