class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_levels_within_range(root, start, end):
    if not root:
        return
    q = []
    q.append(root)
    level = 0
    while q:
        count = len(q)
        while count:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            count -= 1
            if start <= level <= end:
                print(node.data, end=" ")
        level += 1
        print()




if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    print_levels_within_range(root, 2, 3)
