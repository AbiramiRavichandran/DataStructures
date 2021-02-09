class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def get_tilt(root):
    if not root:
        return 0

    l = get_tilt(root.left)
    r = get_tilt(root.right)
    
    get_tilt.tilt += abs(l - r)

    return l + r + root.data



if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(9)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.right.right = Node(7)

    get_tilt.tilt = 0
    get_tilt(root)
    print(get_tilt.tilt)