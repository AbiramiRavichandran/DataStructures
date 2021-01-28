class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def level_order_traversal(root):
    if not root:
        return
    q = []
    q.append(root)
    while q:
        count = len(q)
        while count:
            node = q.pop(0)
            if node.children:
                q += node.children
            print(node.data, end=" ")
            count -= 1
        print()



if __name__ == "__main__":
    root = Node(10)
    root.children.append(Node(2))
    root.children.append(Node(34))
    root.children.append(Node(56))
    root.children.append(Node(100))
    root.children[0].children.append(Node(77))
    root.children[0].children.append(Node(88))
    root.children[2].children.append(Node(1))
    root.children[3].children.append(Node(7))
    root.children[3].children.append(Node(8))
    root.children[3].children.append(Node(9))

    level_order_traversal(root)