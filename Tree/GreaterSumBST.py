global sum_of_tree

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


def greater_sum_tree(root):
    if not root:
        return

    greater_sum_tree(root.right)
    greater_sum_tree.sum += root.data
    root.data = greater_sum_tree.sum - root.data

    greater_sum_tree(root.left)



if __name__ == "__main__":
    root = Node(11)
    root.left = Node(2)
    root.right = Node(29)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.left = Node(35)


    root.in_order_traversal()
    print()
    greater_sum_tree.sum = 0
    greater_sum_tree(root)
    root.in_order_traversal()