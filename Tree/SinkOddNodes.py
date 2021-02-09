class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def sink_odd_node(root):
    if not root or (root.left is None and root.right is None):
        return

    sink_odd_node(root.left)
    sink_odd_node(root.right)

    if root.left and not(root.left.data & 1):
        root.left.data, root.data = root.data, root.left.data
        sink_odd_node(root.left)
    if root.right and not (root.right.data & 1):
        root.right.data, root.data = root.data, root.right.data
        sink_odd_node(root.right)


def print_level_order(root):
    q = [root]

    while q:

        nodeCount = len(q)

        while nodeCount:
            node = q[0]
            print(node.data, end=" ")
            q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodeCount -= 1

        print()


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(9)
    root.right.right = Node(10)
    sink_odd_node(root)
    print_level_order(root)
