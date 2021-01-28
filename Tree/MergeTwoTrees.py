class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order_traversal()

    @classmethod
    def merge_trees(cls, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        t1.data += t2.data
        t1.left = Node.merge_trees(t1.left, t2.left)
        t2.right = Node.merge_trees(t1.right, t2.right)
        return t1



if __name__ == "__main__":

    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(6)

    root2 = Node(4)
    root2.left = Node(1)
    root2.right = Node(7)
    root2.left.left = Node(3)
    root2.right.left = Node(2)
    root2.right.right = Node(6)

    root3 = Node.merge_trees(root1, root2)
    root3.in_order_traversal()