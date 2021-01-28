class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_tree(arr, node, start, end):
    if start == end:
        node.data = arr[start]

    else:
        mid = (start + end) // 2

        node.left = Node(0)
        construct_tree(arr, node.left, start, mid)
        node.right = Node(0)
        construct_tree(arr, node.right, mid + 1, end)
        node.data = node.left.data + node.right.data

def upgrade(prev, curr, start, end, index, new_value):
    if start == end:
        curr.data = new_value
    else:
        mid = (start + end) // 2

        if index <= mid:
            curr.right = prev.right

            curr.left = Node(0)
            upgrade(prev.left, curr.left, start, mid, index, new_value)
        else:
            curr.left = prev.left

            curr.right = Node(0)
            upgrade(prev.right, curr.right, mid + 1, end, index, new_value)

        curr.data = curr.left.data + curr.right.data


def query(node, start, end, qs, qe):
    if qs > end or qe < start:
        return 0

    if qs <= start and qe >= end:
        return node.data

    mid = (start + end) // 2

    return query(node.left, start, mid, qs, qe) + query(node.right, mid + 1, end, qs, qe)

def print_leaves(root):
    if not root:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
    print_leaves(root.left)
    print_leaves(root.right)

def print_versions(version):
    for i in range(len(version)):
        print("version {0} : ".format(i), end="")
        print_leaves(version[i])
        print()


def print_query(version, n, qs, qe):
    for i in range(len(version)):
        print("query of range({0}, {1}) : ".format(qs, qe), query(version[i], 0, n-1, qs, qe))



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    root = Node(0)
    construct_tree(arr, root, 0, n-1)
    version = []

    version.append(root)
    version.append(Node(0))
    upgrade(version[0], version[1], 0, n-1, 4, 1)
    version.append(Node(0))
    upgrade(version[1], version[2], 0, n-1, 2, 10)

    print_versions(version)

    print_query(version, n, 0, 3)



