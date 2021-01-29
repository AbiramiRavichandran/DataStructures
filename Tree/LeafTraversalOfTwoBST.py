class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None


def has_same_leaf_traversal(t1, t2):
    q1 = []
    q2 = []

    q1.append(t1)
    q2.append(t2)

    while q1 or q2:
        if not q1 or not q2:
            return False

        temp1 = q1.pop(0)
        while temp1 and not temp1.is_leaf():
            if temp1.left:
                q1.append(temp1.left)
            if temp1.right:
                q1.append(temp1.right)
            temp1 = q1.pop(0)

        temp2 = q2.pop(0)
        while temp2 and not temp2.is_leaf():
            if temp2.left:
                q2.append(temp2.left)
            if temp2.right:
                q2.append(temp2.right)
            temp2 = q2.pop(0)


        if (temp1 is None and temp2) or (temp2 is None and temp1):
            return False
        if temp1.data != temp2.data:
            return False

    return True


if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    root2 = Node(0)
    root2.left = Node(1)
    root2.right = Node(5)
    root2.left.right = Node(4)
    root2.right.left = Node(6)
    root2.right.right = Node(7)

    print(has_same_leaf_traversal(root1, root2))
