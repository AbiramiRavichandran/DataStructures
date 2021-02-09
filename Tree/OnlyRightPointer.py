class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def pre_order_traversal(self):
        print(self.data, end=" ")

        if self.right:
            self.right.pre_order_traversal()

def modify_tree(root):
    right = root.right
    rightMost = root

    if root.left:
        rightMost = modify_tree(root.left)
        root.right = root.left
        root.left = None
    if not right:
        return rightMost
    rightMost.right = right
    rightMost = modify_tree(right)
    return rightMost



if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)

    modify_tree(root)
    root.pre_order_traversal()