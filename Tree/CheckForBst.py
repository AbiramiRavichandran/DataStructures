class Node:
    prev = float('-inf')

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_bst(self, start, end):
        if start < self.data < end:
            l = self.left.is_bst(start, self.data) if self.left else True
            r = self.right.is_bst(self.data, end) if self.right else True
            return l and r
        return False

    def is_bst_in_order(self):
        if self.left:
            if not self.left.is_bst_in_order():
                return False
        if self.data < Node.prev:
            return False
        else:
            Node.prev = self.data
            if self.right:
                if not self.right.is_bst_in_order():
                    return False
        return True


if __name__ == "__main__":
    root = Node(80)
    root.left = Node(70)
    root.right = Node(90)
    root.left.left = Node(60)
    root.left.right = Node(75)
    root.right.left = Node(85)
    root.right.right = Node(100)

    print(root.is_bst(float('-inf'), float('inf')))
    print(root.is_bst_in_order())
