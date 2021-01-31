class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def get_max_diff_util(root, res):
    if not root:
        return float('inf'), res
    if not root.left and not root.right:
        return root.data, res

    a, res = get_max_diff_util(root.left, res)
    b, res = get_max_diff_util(root.right, res)
    val = min(a, b)
    res = max(root.data - val, res)

    return min(val, root.data), res

def get_max_diff(root):
    res = float('-inf')
    val, res = get_max_diff_util(root, res)
    return res



if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)

    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)

    root.right = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)


    print(get_max_diff(root))
