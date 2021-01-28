class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def flip_tree(root):
    if not root:
        return None
    if not root.left and not root.right:
        return root
    flipped_node = flip_tree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None

    return flipped_node


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    print(root.in_order_traversal())
    flip = flip_tree(root)
    print(flip.in_order_traversal())