class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def insert(self, data):
        if self.data > data:
            self.left = self.left.insert(data) if self.left else Node(data)
        elif self.data < data:
            self.right = self.right.insert(data) if self.right else Node(data)
        return self

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order_traversal()

def remove_outside_range(root, min, max):
    if not root:
        return
    root.left = remove_outside_range(root.left, min, max)
    root.right = remove_outside_range(root.right, min, max)
    if root.data < min:
        rchild = root.right
        del root
        return rchild
    if root.data > max:
        lchild = root.left
        del root
        return lchild

    return root

def tree_builder(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root = root.insert(elements[i])

    return root


if __name__ == "__main__":
    tree = tree_builder([6, -13, 14, -8, 15, 13, 7])
    tree.in_order_traversal()
    print()
    remove_outside_range(tree, -10, 13)
    tree.in_order_traversal()
