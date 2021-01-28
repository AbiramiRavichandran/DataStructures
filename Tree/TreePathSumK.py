class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printKPath(root, k, path=[]):
    if not root:
        return
    path.append(root.data)

    s = 0
    n = len(path)
    i = n - 1
    while i >= 0:
        s += path[i]
        if s == k:
            print(" ".join(str(p) for p in path[i:]))
        i -= 1
    printKPath(root.left, k, path)
    printKPath(root.right, k, path)

    path.pop()



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(2)

    k = 5
    printKPath(root, k)