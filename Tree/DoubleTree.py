class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order_traversal()

def get_double_tree(root):
    if not root:
        return
    get_double_tree(root.left)
    get_double_tree(root.right)

    old_left = root.left
    root.left = Node(root.data)
    root.left.left = old_left



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.in_order_traversal()

    get_double_tree(root)
    print()
    root.in_order_traversal()
