class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def get_total_sum(self):
        l = self.left.get_total_sum() if self.left else 0
        r = self.right.get_total_sum() if self.right else 0

        return l + r + self.data


def get_uncover_sum_left(root):
    if not root:
        return 0
    if root.left:
        return root.data + get_uncover_sum_left(root.left)
    elif root.right:
        return root.data + get_uncover_sum_left(root.right)
    else:
        return root.data


def get_uncover_sum_right(root):
    if not root:
        return 0
    if root.right:
        return root.data + get_uncover_sum_right(root.right)
    elif root.left:
        return root.data + get_uncover_sum_right(root.left)
    else:
        return root.data


def get_uncover_sum(root):
    if not root:
        return 0
    return get_uncover_sum_left(root.left) + get_uncover_sum_right(root.right) + root.data

def is_sum_same(root):
    t_s = root.get_total_sum()
    u_s = get_uncover_sum(root)
    print(t_s)
    print(u_s)
    if t_s - u_s == u_s:
        print("True")
    else:
        print("False")



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

    is_sum_same(root)