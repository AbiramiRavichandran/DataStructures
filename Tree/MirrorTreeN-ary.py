class Node:
    def __init__(self, data):
        self.data = data
        self.child = []

def print_level_wise(root):
    if not root:
        return
    q = []
    q.append(root)
    while q:
        n = len(q)
        while n:
            node = q.pop(0)
            print(node.data, end=" ")
            for i in range(len(node.child)):
                q.append(node.child[i])
            n -= 1
        print()


def get_mirror_tree(root):
    if not root:
        return
    n = len(root.child)

    for i in range(n):
        get_mirror_tree(root.child[i])

    return root.child.reverse()


if __name__ == "__main__":
    root = Node(10)
    root.child.append(Node(2))
    root.child.append(Node(34))
    root.child.append(Node(56))
    root.child.append(Node(100))
    root.child[2].child.append(Node(1))
    root.child[3].child.append(Node(7))
    root.child[3].child.append(Node(8))
    root.child[3].child.append(Node(9))

    print_level_wise(root)

    print()

    get_mirror_tree(root)
    print_level_wise(root)


