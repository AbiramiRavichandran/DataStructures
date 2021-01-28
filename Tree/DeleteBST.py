class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def delete_bst(root):
    if not root:
        return None
    q = []
    q.append(root)
    while q:
        node = q.pop()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        node = None

    print("Tree Deleted")

if __name__ == "__main__":
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    delete_bst(root)