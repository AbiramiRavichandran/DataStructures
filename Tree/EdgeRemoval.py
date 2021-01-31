class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def get_size(self):
        l_size = self.left.get_size() if self.left else 0
        r_size = self.right.get_size() if self.right else 0

        return l_size + r_size + 1


def check_rec(root, n):
    if not root:
        return 0
    c = check_rec(root.left, n) + 1 + check_rec(root.right, n)
    if c == n - c:
        check_rec.res = True
    return c


def check(root):
    n = root.get_size()
    check_rec.res = False
    check_rec(root, n)
    print(check_rec.res)





if __name__ == "__main__":
    root = Node(5)
    root.left = Node(1)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(4)
    check(root)