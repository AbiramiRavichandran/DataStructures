class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_symmetric(root):
    if not root:
        return
    if not root.left and not root.right:
        return True
    q = []
    q.append(root)

    while q:
        count = len(q)
        while count:
            node = q.pop(0)
            if node.left and node.right:
                q.append(node.left)
                q.append(node.right)
            elif node.left or node.right:
                return False
            count -= 1
        temp = q.copy()
        while temp:
            temp_left = temp.pop(0)
            temp_right = temp.pop()
            if temp_left.data != temp_right.data:
                return False
    return True







if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    print(is_symmetric(root))