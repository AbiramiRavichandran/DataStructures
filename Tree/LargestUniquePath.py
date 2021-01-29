class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def get_max_path(root, hash):
    if not root:
        return len(hash)

    if root.data in hash:
        hash[root.data] += 1
    else:
        hash[root.data] = 1

    max_path = max(get_max_path(root.left, hash), get_max_path(root.right, hash))
    hash[root.data] -= 1

    if hash[root.data] == 0:
        del hash[root.data]

    return max_path



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    hash = {}
    print(get_max_path(root, hash))