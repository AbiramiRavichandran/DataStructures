class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def ceil(root, key):
    if not root:
        return -1
    if root.data == key:
        return root.data
    if root.data < key:
        return ceil(root.right, key)

    val = ceil(root.left, key)
    return val if val >= key else root.data

def floor(root, key):
    if not root:
        return -1
    if root.data == key:
        return root.data

    if root.data > key:
        return floor(root.left, key)

    val = floor(root.right, key)
    return val if val <= key and val != -1 else root.data



if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(10)

    print(ceil(root, 8))
    print(floor(root, 8))