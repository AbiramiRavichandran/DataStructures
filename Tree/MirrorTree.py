class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def mirror(self):
        lnode = self.right.mirror() if self.right else None
        rnode = self.left.mirror() if self.left else None

        self.left = lnode
        self.right = rnode

        return self

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def count_leaf_nodes(self):

        if self.left is None and self.right is None:
            return 1

        l_count = self.left.count_leaf_nodes() if self.left else 0
        r_count = self.right.count_leaf_nodes() if self.right else 0

        return l_count + r_count






if __name__ == "__main__":
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(4)

    print(root.in_order_traversal())
    root.mirror()
    print(root.in_order_traversal())
    print(root.count_leaf_nodes())
