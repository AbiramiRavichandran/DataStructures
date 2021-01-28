class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    else:
        return root1.data == root2.data and are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)

def is_sub_tree(t, s):
    if not s:
        return True
    if not t:
        return False
    if are_identical(t, s):
        return True
    else:
        return is_sub_tree(t.left, s) or is_sub_tree(t.right, s)




if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    # root2 = Node(1)
    # root2.left = Node(2)
    # root2.right = Node(3)
    # root2.left.left = Node(4)
    # root2.left.right = Node(5)

    root2 = Node(5)
    # root2.left = Node(4)
    # root2.right = Node(5)
    # root2.left.left = Node(4)
    # root2.left.right = Node(5)





    print(is_sub_tree(root1, root2))
