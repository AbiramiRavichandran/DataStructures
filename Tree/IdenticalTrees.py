class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def are_identical(root1, root2):

    if are_identical.result:
        if root1 is None and root2 is None:
            return
        elif root1 is None or root2 is None:
            are_identical.result = False
            return
        else:
            if root1.data != root2.data:
                are_identical.result = False
            else:
                are_identical(root1.left, root2.left)
                are_identical(root1.right, root2.right)



if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    #root2.left.right = Node(5)

    are_identical.result = True

    are_identical(root1, root2)

    print(are_identical.result)
