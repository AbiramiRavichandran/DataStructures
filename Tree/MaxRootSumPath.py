class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def has_path_sum(root, s):

    if root is None:
        return s == 0

    ans = 0
    sub_sum = s - root.data

    if sub_sum == 0 and root.left is None and root.right is None:
        return 1



    if root.left:
        ans = ans or has_path_sum(root.left, sub_sum)
    if root.right:
        ans = ans or has_path_sum(root.right, sub_sum)

    return ans






if __name__ == "__main__":

    s = 21
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.right = Node(5)
    root.left.left = Node(3)
    root.right.left = Node(2)

    print(has_path_sum(root, s))
