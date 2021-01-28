class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        next = self.nextRight.data if self.nextRight else None
        print(self.data, "--> ", next)
        if self.right:
            self.right.in_order_traversal()

    def level_order_traversal(self, is_root=True):
        if is_root:
            print(self.data)
        if self.left:
            next = self.left.nextRight.data if self.left.nextRight else None
            print(self.left.data, " --> ", next)
        if self.right:
            next = self.right.nextRight.data if self.right.nextRight else None
            print(self.right.data, " --> ", next)
        if self.left:
            self.left.level_order_traversal(False)
        if self.right:
            self.right.level_order_traversal(False)


    def connect_nodes(self):
        q = []
        q.append(self)

        while q:
            count = len(q)
            while count:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                count -= 1
            for i in range(len(q)-1):
                q[i].nextRight = q[i+1]




if __name__ == "__main__":
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.left = Node('F')

    root.connect_nodes()

    root.level_order_traversal()

