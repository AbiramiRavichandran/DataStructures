class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


    def print_next(self):
        if self.left:
            self.left.print_next()
        print("Next of {0} is {1}".format(self.data, self.next.data if self.next else 0))
        if self.right:
            self.right.print_next()




def populate_next(node):
    if node:
        populate_next(node.right)

        node.next = populate_next.next
        populate_next.next = node

        populate_next(node.left)




if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(12)
    root.left.left = Node(3)

    populate_next.next = None
    populate_next(root)
    root.print_next()
