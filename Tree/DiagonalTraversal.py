class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def diagonal_util(root, d):
    if not root:
        return
    try:
        hash_map[d].append(root.data)
    except KeyError:
        hash_map[d] = [root.data]

    diagonal_util(root.left, d+1)
    diagonal_util(root.right, d)


def diagonal_traversal(root):

    diagonal_util(root, 0)
    print(hash_map)

def diagonal_print_iterative(root):
    if not root:
        return

    q = []
    q.append(root)
    q.append(None)

    while q:
        temp = q.pop(0)
        if not temp:
            if not len(q):
                return
            print()
            q.append(None)
        else:
            while temp:
                print(temp.data, end=" ")
                if temp.left:
                    q.append(temp.left)
                temp = temp.right

if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)

    hash_map = dict()

    diagonal_traversal(root)
    diagonal_print_iterative(root)